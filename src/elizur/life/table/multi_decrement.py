from collections.abc import Iterable

import numpy as np
import polars as pl

from elizur.life.table.table import LifeTable
from elizur.life.util.validators import InvalidAge, InvalidInterval


class MultiDecrementTable:
    """Two-decrement life table combining mortality and lapse decrements.

    Applies the independent decrements assumption with the UDD (Uniform
    Distribution of Deaths) approximation to convert single-decrement
    probabilities into multi-decrement probabilities.  This is the
    standard actuarial approach for IFRS 17 cashflow projection models
    where policies exit either by death or voluntary lapse.

    Under UDD, the multi-decrement probabilities are approximated as:

        q^(d)_x ≈ q'(d)_x × (1 - q'(w)_x / 2)
        q^(w)_x ≈ q'(w)_x × (1 - q'(d)_x / 2)
        q^(τ)_x  = 1 - (1 - q'(d)_x) × (1 - q'(w)_x)

    where q'(d) and q'(w) are the single-decrement (independent) mortality
    and lapse probabilities respectively.

    Args:
        mortality: Single-decrement mortality ``LifeTable``.  The lapse
            rates must be aligned to the same age indices as this table.
        lapse_rates: Annual lapse (withdrawal) rates indexed by age,
            starting from age 0.  Must have the same length as the
            mortality table.

    Raises:
        ValueError: If ``lapse_rates`` length does not match the
            mortality table size.
    """

    def __init__(
        self,
        mortality: LifeTable,
        lapse_rates: Iterable[float] | np.ndarray,
    ) -> None:
        self._mortality = mortality
        self._lapse_rates = np.array(lapse_rates, dtype=float)

        if self._lapse_rates.size != mortality.table_size:
            raise ValueError(
                f"lapse_rates length ({self._lapse_rates.size}) must equal "
                f"mortality table size ({mortality.table_size})."
            )

        qd = mortality.qxs
        qw = self._lapse_rates

        # UDD multi-decrement approximations
        self._qx_d: np.ndarray = qd * (1.0 - qw / 2.0)
        self._qx_w: np.ndarray = qw * (1.0 - qd / 2.0)
        self._qx_tau: np.ndarray = 1.0 - (1.0 - qd) * (1.0 - qw)
        self._px_tau: np.ndarray = 1.0 - self._qx_tau

        # Lives in multi-decrement table
        radix = mortality.lxs[0]
        self._lx_tau: np.ndarray = (
            radix * np.insert(np.cumprod(self._px_tau), 0, 1.0)[: mortality.table_size]
        )
        self._dx_d: np.ndarray = self._lx_tau * self._qx_d
        self._dx_w: np.ndarray = self._lx_tau * self._qx_w

    @property
    def table_size(self) -> int:
        """Number of ages in the table."""
        return self._mortality.table_size

    def _validate_age(self, x: int) -> None:
        if x < 0:
            raise InvalidAge("Start age must be greater than or equal to 0!")

    def _validate_interval(self, n: int) -> None:
        if n <= 0:
            raise InvalidInterval("Interval must be greater than 0!")

    def qx_d(self, x: int) -> float:
        """Multi-decrement probability of death at age x.

        Args:
            x: Attained age.

        Returns:
            Probability of decrement by death between age x and x + 1
            in the multi-decrement table.

        Raises:
            InvalidAge: If x is negative.
        """
        self._validate_age(x)
        if x >= self.table_size:
            return 1.0
        return float(self._qx_d[x])

    def qx_w(self, x: int) -> float:
        """Multi-decrement probability of lapse at age x.

        Args:
            x: Attained age.

        Returns:
            Probability of decrement by lapse between age x and x + 1
            in the multi-decrement table.

        Raises:
            InvalidAge: If x is negative.
        """
        self._validate_age(x)
        if x >= self.table_size:
            return 0.0
        return float(self._qx_w[x])

    def qx_tau(self, x: int) -> float:
        """Total multi-decrement probability at age x.

        Args:
            x: Attained age.

        Returns:
            Probability of decrement by any cause between age x and x + 1.

        Raises:
            InvalidAge: If x is negative.
        """
        self._validate_age(x)
        if x >= self.table_size:
            return 1.0
        return float(self._qx_tau[x])

    def px_tau(self, x: int) -> float:
        """Total multi-decrement survival probability at age x.

        Args:
            x: Attained age.

        Returns:
            Probability of surviving all decrements between age x and x + 1.

        Raises:
            InvalidAge: If x is negative.
        """
        self._validate_age(x)
        if x >= self.table_size:
            return 0.0
        return float(self._px_tau[x])

    def lx_tau(self, x: int) -> float:
        """Expected number of lives in the multi-decrement table at age x.

        Args:
            x: Attained age.

        Returns:
            Expected lives at age x under both mortality and lapse decrements.

        Raises:
            InvalidAge: If x is negative.
        """
        self._validate_age(x)
        if x >= self.table_size:
            return 0.0
        return float(self._lx_tau[x])

    def dx_d(self, x: int) -> float:
        """Expected deaths between age x and x + 1 in the multi-decrement table.

        Args:
            x: Attained age.

        Returns:
            Expected number of deaths between age x and x + 1.

        Raises:
            InvalidAge: If x is negative.
        """
        self._validate_age(x)
        if x >= self.table_size:
            return 0.0
        return float(self._dx_d[x])

    def dx_w(self, x: int) -> float:
        """Expected lapses between age x and x + 1 in the multi-decrement table.

        Args:
            x: Attained age.

        Returns:
            Expected number of lapses between age x and x + 1.

        Raises:
            InvalidAge: If x is negative.
        """
        self._validate_age(x)
        if x >= self.table_size:
            return 0.0
        return float(self._dx_w[x])

    def npx_tau(self, n: int, x: int) -> float:
        """Probability of surviving all decrements for n years from age x.

        Args:
            n: Number of years.
            x: Starting age.

        Returns:
            Probability of surviving both mortality and lapse decrements
            from age x to age x + n.

        Raises:
            InvalidAge: If x is negative.
            InvalidInterval: If n is not positive.
        """
        self._validate_age(x)
        self._validate_interval(n)
        if x >= self.table_size:
            return 0.0
        lx = self.lx_tau(x)
        if lx == 0.0:
            return 0.0
        lxn = self.lx_tau(x + n) if x + n < self.table_size else 0.0
        return lxn / lx

    def to_frame(self) -> pl.DataFrame:
        """Export the multi-decrement table as a Polars DataFrame.

        Each row represents one age from 0 to ω-1.  The resulting DataFrame
        includes both the original single-decrement rates and the computed
        multi-decrement probabilities, making it suitable for joining against
        policy-level DataFrames in projection engines.

        Returns:
            A Polars DataFrame with columns:

            - ``age``: integer age from 0 to table_size - 1
            - ``qx_prime_d``: single-decrement mortality rate q'(d)_x
            - ``qx_prime_w``: single-decrement lapse rate q'(w)_x
            - ``qx_d``: multi-decrement mortality probability q^(d)_x
            - ``qx_w``: multi-decrement lapse probability q^(w)_x
            - ``qx_tau``: total decrement probability q^(τ)_x
            - ``px_tau``: total survival probability p^(τ)_x
            - ``lx_tau``: expected lives in multi-decrement table
            - ``dx_d``: expected deaths in multi-decrement table
            - ``dx_w``: expected lapses in multi-decrement table
        """
        size = self.table_size
        return pl.DataFrame(
            {
                "age": list(range(size)),
                "qx_prime_d": self._mortality.qxs.tolist(),
                "qx_prime_w": self._lapse_rates.tolist(),
                "qx_d": self._qx_d.tolist(),
                "qx_w": self._qx_w.tolist(),
                "qx_tau": self._qx_tau.tolist(),
                "px_tau": self._px_tau.tolist(),
                "lx_tau": self._lx_tau.tolist(),
                "dx_d": self._dx_d.tolist(),
                "dx_w": self._dx_w.tolist(),
            }
        )
