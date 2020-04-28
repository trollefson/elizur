from typing import Callable, Tuple

from elizur.life.annuity import discount_factor
from elizur.life.util import (
    validate_age,
    validate_age_and_interest,
    validate_age_and_interval,
    validate_age_interest_and_interval,
)


class LifeTable:
    # pylint: disable=too-many-public-methods
    """
    Given an input tuple of failure probabilities this class is capable
    of calculating common actuarial functions such as qx, px, lx, dx,
    ex, mx, w, nqx, npx, nlx, ndx, nmx, tqxn, Dx, Sx, Nx, Cx, Mx, Rx, actuarial
    present value of annuities, and actuarial present value of insurances.

    Args:
        table: collection of failure probabilities in sequentiali
               order, e.g. (1q0, 2q1, ..., 100q99)
        initial_pop: the size of the initial population (l0)
    """

    def __init__(
        self,
        table: Tuple[float],
        name: str = "",
        description: str = "",
        initial_pop: int = 100000,
    ):
        self._qxs = table
        self._lxs = self._set_lxs(initial_pop)
        self.name = name
        self.description = description

    def _set_lxs(self, l0: int) -> Tuple[float]:
        """
        Args:
            l0: the size of the initial population
        """
        lxs = [l0]
        for qx in self._qxs:
            lxs.append(lxs[-1] * (1 - qx))
        return tuple(lxs)

    @property
    def w(self) -> int:
        """
        Returns:
            The limiting age of the life table
        """
        return self.get_lxs().index(0) - 1

    @validate_age
    def qx(self, x: int) -> float:
        """
        Args:
            x: start age

        Returns:
            The probability of failure between the ages x and x + 1
        """
        return self._qxs[x]

    @validate_age
    def px(self, x: int) -> float:
        """
        Args:
            x: start age

        Returns:
            The probability of survival between the ages x and x + 1
        """
        return 1 - self._qxs[x]

    @validate_age
    def lx(self, x: int) -> float:
        """
        Args:
            x: age

        Returns:
            The population size at age x.  This is the same thing as the
            number of person years lived between age x and x + 1.
        """
        return self._lxs[x]

    @validate_age
    def dx(self, x: int) -> float:
        """
        Args:
            x: start age

        Returns:
            The number of failures between ages x and x + 1
        """
        return self.lx(x) - self.lx(x + 1)

    @validate_age
    def ex(self, x: int) -> float:
        """
        Args:
            x: start age

        Returns:
            The curtate life expectation at age x
        """
        return sum([self.lx(t + x) / self.lx(x) for t in range(1, self.w - x)])

    @validate_age
    def mx(self, x: int) -> float:
        """
        Args:
            x: start age
        Returns:
            The central failure rate between ages x and x + 1
        """
        return self.dx(x) / self.lx(x)

    @validate_age_and_interval
    def nqx(self, n: int, x: int) -> float:
        """
        Args:
            n: width of failure interval in years
            x: start age

        Returns:
            The probability of failure between ages x and x + n
        """
        return (self.lx(x) - self.lx(n + x)) / self.lx(x)

    @validate_age_and_interval
    def npx(self, n: int, x: int) -> float:
        """
        Args:
            n: width of survival interval in years
            x: start age

        Returns:
            The probability of survival between ages x and x + n
        """
        return self.lx(n + x) / self.lx(x)

    @validate_age_and_interval
    def nlx(self, n: int, x: int) -> float:
        """
        Args:
            n: width of failure interval in years
            x: start age

        Returns:
            The number of person years lived between ages x and x + n
        """
        return sum([self._lxs[x + i] for i in range(n)])

    @validate_age_and_interval
    def ndx(self, n: int, x: int) -> float:
        """
        Args:
            n: width of failure interval in years
            x: start age

        Returns:
            The number of failures between ages x and x + n
        """
        return sum([self.dx(x + i) for i in range(n)])

    @validate_age_and_interval
    def nmx(self, n: int, x: int) -> float:
        """
        Args:
            x: start age

        Returns:
            The central failure rate between ages x and x + n
        """
        return self.ndx(n, x) / self.nlx(n, x)

    def tqxn(self, t: int, n: int, x: int) -> float:
        """
        Args:
            t: width of the failure interval in years
            n: width of the survival interval in years
            x: start age

        Returns:
            The probability of surviving from age x to x + n and
            then failing between age x + n and age x + n + t
        """
        if x < 0 or n <= 0 or t <= 0:
            return 0.0
        return self.npx(x, n) * self.nqx(t, x + n)

    def get_qxs(self) -> Tuple[float]:
        """
        Returns:
            A tuple of the failure
            probabilities (qxs), e.g., (0q1, 2q1, ..., 100q99)
        """
        return self._qxs

    def get_pxs(self) -> Tuple[float]:
        """
        Returns:
            A tuple of the survival
            probabilities (pxs), e.g., (0p1, 2p1, ..., 100p99)
        """
        return tuple(map(lambda x: 1 - x, self._qxs))

    def get_lxs(self) -> Tuple[float]:
        """
        Returns:
            A tuple of the population counts (lxs)
        """
        return self._lxs

    @validate_age_and_interest
    def Dx(self, x: int, i: float) -> float:
        """
        Actuarial commutation function Dx

        Args:
            x: start age
            i: interest rate
        Returns:
            Population at age x discounted for x years
        """
        return self.lx(x) * discount_factor(i) ** x

    @validate_age_and_interest
    def Nx(self, x: int, i: float) -> float:
        """
        Actuarial commutation function Nx

        Args:
            x: start age
            i: interest rate
        Returns:
            Sum of Ds from age x and onward
        """
        return sum([self.Dx(n, i) for n in range(x, self.w + 1)])

    @validate_age_and_interest
    def Sx(self, x: int, i: float) -> float:
        """
        Actuarial commutation function Sx

        Args:
            x: start age
            i: interest rate
        Returns:
            Sum of Ns from age x and onward
        """
        return sum([self.Nx(n, i) for n in range(x, self.w + 1)])

    @validate_age_and_interest
    def Cx(self, x: int, i: float) -> float:
        """
        Actuarial commutation function Cx

        Args:
            x: start age
            i: interest rate
        Returns:
            Failures between x and x + 1 discounted for x years
        """
        return (self.lx(x) - self.lx(x + 1)) * discount_factor(i) ** (x + 1)

    @validate_age_and_interest
    def Mx(self, x: int, i: float) -> float:
        """
        Actuarial commutation function Mx

        Args:
            x: start age
            i: interest rate
        Returns:
            Sum of Cs from age x and onward
        """
        return sum([self.Cx(t, i) for t in range(x, self.w + 1)])

    @validate_age_and_interest
    def Rx(self, x: int, i: float) -> float:
        """
        Actuarial commutation function Rx

        Args:
            x: start age
            i: interest rate
        Returns:
            Sum of Ms from age x and onward
        """
        return sum([self.Mx(t, i) for t in range(x, self.w + 1)])

    @validate_age_and_interest
    def Ax(self, x: int, i: float) -> float:
        """
        Args:
            x: start age
            i: interest rate
        Returns:
            Actuarial present value of level whole insurance
        """
        return self.Mx(x, i) / self.Dx(x, i)

    @validate_age_interest_and_interval
    def Axn(self, x: int, i: float, n: int) -> float:
        """
        Args:
            x: start age
            i: interest rate
            n: number of periods in the temporary insurance
        Returns:
            Actuarial present value of level temporary insurance
        """
        return (self.Mx(x, i) - self.Mx(x + n, i)) / self.Dx(x, i)

    @validate_age_and_interest
    def IAx(self, x: int, i: float) -> float:
        """
        Args:
            x: start age
            i: interest rate
        Returns:
            Actuarial present value of increasing whole insurance
        """
        return self.Rx(x, i) / self.Dx(x, i)

    @validate_age_interest_and_interval
    def IAxn(self, x: int, i: float, n: int) -> float:
        """
        Args:
            x: start age
            i: interest rate
            n: number of periods in the temporary insurance
        Returns:
            Actuarial present value of increasing temporary insurance
        """
        return (self.Rx(x, i) - self.Rx(x + n, i) - n * self.Mx(x + n, i)) / self.Dx(
            x, i
        )

    @validate_age_and_interest
    def ax(self, x: int, i: float) -> float:
        """
        Args:
            x: start age
            i: interest rate
        Returns:
            Actuarial present value of a level perpetuity
        """
        return self.Nx(x + 1, i) / self.Dx(x, i)

    @validate_age_interest_and_interval
    def axn(self, x: int, i: float, n: int) -> float:
        """
        Args:
            x: start age
            i: interest rate
            n: length of payments
        Returns:
            Actuarial present value of a temporary annuity
        """
        return (self.Nx(x + 1, i) - self.Nx(x + n + 1, i)) / self.Dx(x, i)

    @validate_age_and_interest
    def ax_due(self, x: int, i: float) -> float:
        """
        Args:
            x: start age
            i: interest rate
        Returns:
            Actuarial present value of a level perpetuity due
        """
        return self.Nx(x, i) / self.Dx(x, i)

    @validate_age_interest_and_interval
    def axn_due(self, x: int, i: float, n: int) -> float:
        """
        Args:
            x: start age
            i: interest rate
            n: length of payments
        Returns:
            Actuarial present value of a temporary annuity due
        """
        return (self.Nx(x, i) - self.Nx(x + n, i)) / self.Dx(x, i)


EXAMPLE_TABLE = (
    0.006271,
    0.00041799999999999997,
    0.00028100000000000005,
    0.000201,
    0.00017,
    0.000163,
    0.000127,
    0.000123,
    0.000133,
    0.000132,
    0.000126,
    0.00013000000000000002,
    0.000145,
    0.000186,
    0.00020999999999999998,
    0.000253,
    0.000389,
    0.00044,
    0.00046600000000000005,
    0.000457,
    0.00045400000000000003,
    0.000502,
    0.000467,
    0.000453,
    0.000486,
    0.000498,
    0.00051,
    0.000507,
    0.000565,
    0.0005989999999999999,
    0.000632,
    0.0006680000000000001,
    0.0007239999999999999,
    0.000786,
    0.000853,
    0.000958,
    0.001034,
    0.0011200000000000001,
    0.001221,
    0.001433,
    0.0014930000000000002,
    0.001653,
    0.00175,
    0.0019950000000000002,
    0.002091,
    0.0023039999999999996,
    0.002376,
    0.002577,
    0.002859,
    0.0030310000000000003,
    0.003194,
    0.003522,
    0.003634,
    0.004142000000000001,
    0.0044340000000000004,
    0.0050999999999999995,
    0.005006,
    0.005886,
    0.006441,
    0.007266,
    0.007575999999999999,
    0.008476000000000001,
    0.009201,
    0.010101,
    0.011149,
    0.012107,
    0.013059,
    0.014570999999999999,
    0.015590999999999999,
    0.017396000000000002,
    0.018991,
    0.020454,
    0.022525,
    0.024633,
    0.027135000000000003,
    0.030098,
    0.032631,
    0.036094,
    0.039472,
    0.044109999999999996,
    0.0493,
    0.053298000000000005,
    0.062179000000000005,
    0.06455,
    0.07505500000000001,
    0.083221,
    0.091996,
    0.10139,
    0.111404,
    0.122037,
    0.13328,
    0.145119,
    0.157532,
    0.170488,
    0.183953,
    0.19788,
    0.21221700000000002,
    0.226905,
    0.241875,
    0.257053,
    1.0,
)
