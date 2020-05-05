from typing import Iterable, Union

import numpy as np

from elizur.life.annuity import discount_factor


class InvalidEPVInputs(Exception):
    """
    Custom exception raised for invalid expected present value inputs.
    """


def expected_present_value(
    cash_flows: Union[Iterable, np.ndarray],
    probabilities: Union[Iterable, np.ndarray],
    interest_rates: Union[Iterable, np.ndarray],
) -> Union[float, np.ndarray]:
    """
    This function is useful for calculating variable streams of cash flows,
    interest rates, and probabilities.

    Args:
        cash_flows: payouts from time 0 to n, where time n is the last
        possible payout, e.g., (cf0, cf1, cf2, ..., cfn-1, cfn)
        probabilities: probability of a cash flow occuring from time
                       0 to n, e.g., (1p0, 2p1, 3p2, ..., npn-1)
        interest_rates: collection of interest rates to use for
                        discounting, where each interest rate is for one
                        period, e.g., (i0to1, i1to2, ..., in-1ton)

    Returns:
        The expected present value

    Example:
        Given the probabilities: 1p0 = 0.98, 2p1=0.94, 3p2=0.91

        annuity(x=0, i=0.07, n=3)

        expected_present_value((1, 1, 1), (0.98, 0.94, 0.91), (0.07, 0.07, 0.07))

        The two methods of calculating the present value of an annuity are the same

        Additionally a two-dimensional arrays of inputs can be provided to perform
        multiple expected present values at once.  The work flows below produce the
        same results:

        expected_present_value((1, 1, 1), (0.98, 0.94, 0.91), (0.07, 0.07, 0.07))

        expected_present_value((1, 1, 1), (0.88, 0.84, 0.81), (0.06, 0.06, 0.06))

        expected_present_value((1, 1, 1), (0.78, 0.74, 0.71), (0.05, 0.05, 0.05))

        expected_present_value(
            np.array([
                [1, 1, 1],
                [1, 1, 1],
                [1, 1, 1]
            ]),
            np.array([
                [0.98, 0.96, 0.91],
                [0.88, 0.86, 0.81],
                [0.78, 0.76, 0.71]
            ]),
            np.array([
                [0.07, 0.07, 0.07],
                [0.06, 0.06, 0.06],
                [0.05, 0.05, 0.05]
            ])
        )
    """
    cash_flows = np.array(cash_flows)
    probabilities = np.array(probabilities)
    interest_rates = np.array(interest_rates)

    if not cash_flows.size == probabilities.size == interest_rates.size:
        raise InvalidEPVInputs(
            "The shape of the inputs do not match! The cash "
            f"flow shape is {cash_flows.shape}, the probability "
            f"shape is {probabilities.shape}, "
            f"the interest rate shape is {interest_rates.shape}!"
        )
    if cash_flows.ndim > 2 or probabilities.ndim > 2 or interest_rates.ndim > 2:
        raise InvalidEPVInputs(
            "The dimensions of the inputs are too high! The cash "
            f"flow number of dimensions is {cash_flows.ndim}, the probability "
            f"number of dimensions is {probabilities.ndim}, "
            f"the interest rate number of dimensions is {interest_rates.ndim}! "
            "The number of dimensions for each input must be less than 3."
        )

    discount_factors = discount_factor(interest_rates)
    if interest_rates.ndim == 1:
        cumulative_product = np.nancumprod(discount_factors)
        epv = np.nansum(
            np.multiply(np.multiply(cash_flows, probabilities), cumulative_product)
        )
    else:
        cumulative_product = np.apply_along_axis(np.nancumprod, 1, discount_factors)
        epv = np.apply_along_axis(
            np.nansum,
            1,
            np.multiply(np.multiply(cash_flows, probabilities), cumulative_product),
        )
    return epv
