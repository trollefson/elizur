from typing import Tuple

from elizur.life.annuity import discount_factor


class InvalidEPVInputs(Exception):
    """
    Custom exception raised for invalid expected present value inputs.
    """


def expected_present_value(
    cash_flows: Tuple[float], probabilities: Tuple[float], interest_rates: Tuple[float]
) -> float:
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

        The two methods of calculated the present value of an annuity are the same
    """
    cf_length, p_length, i_length = (
        len(cash_flows),
        len(probabilities),
        len(interest_rates),
    )
    if cf_length != p_length or p_length != i_length or cf_length != i_length:
        raise InvalidEPVInputs(
            "The length of the inputs do not match! The cash "
            f"flow vector length is {cf_length}, the probability vector length is {p_length}, "
            f"the interest rate vector length is {i_length}!"
        )

    # Math: x=0 to n E [CFx * px * [y=0 to x # Vx]]
    epv = 0
    for i, cf in enumerate(cash_flows):
        if probabilities[i] == 0:
            continue
        cumulative_factor = probabilities[i]
        for z in range(0, i + 1):
            cumulative_factor *= discount_factor(interest_rates[z])
        epv += cumulative_factor * cf
    return epv
