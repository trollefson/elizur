import numbers
from typing import Iterable, Union

import numpy as np


def discount_factor(
    i: Union[float, Iterable, np.array]
) -> Union[float, Iterable, np.array]:
    """
    Args:
        i: interest rate in decimal form
    Returns:
        The related discount factor
    """
    return np.divide(1, np.add(1, i))


def interest_rate(
    d: Union[float, Iterable, np.array]
) -> Union[float, Iterable, np.array]:
    """
    Args:
        d: discount rate in decimal form
    Returns:
        The related interest rate in decimal form
    """
    return np.divide(d, np.subtract(1, d))


def discount_rate(
    i: Union[float, Iterable, np.array]
) -> Union[float, Iterable, np.array]:
    """
    Args:
        i: interest rate in decimal form
    Returns:
        The related discount rate
    """
    return np.divide(i, np.add(1, i))


def annuity_pv(
    n: Union[int, Iterable, np.array], i: Union[float, Iterable, np.array]
) -> Union[float, Iterable, np.array]:
    """
    Args:
        n: years
        i: periodic interest rate in decimal form
    Returns:
        Present value of annuity of n years with an interest rate of i
    """
    return np.divide(1 - np.power(discount_factor(i), n), i)


def annuity_due_pv(
    n: Union[int, Iterable, np.array], i: Union[float, Iterable, np.array]
) -> Union[float, Iterable, np.array]:
    """
    Args:
        n: years
        i: periodic interest rate in decimal form
    Returns:
        Present value of annuity of n years with an interest rate of i
    """
    return np.divide(1 - np.power(discount_factor(i), n), discount_rate(i))


def perpetuity_pv(
    i: Union[float, Iterable, np.array]
) -> Union[float, Iterable, np.array]:
    """
    Args:
        i: periodic interest rate in decimal form
    Returns:
        Present value of a perpetuity with an interest rate of i
    """
    return np.divide(1, i)


def perpetuity_due_pv(
    i: Union[float, Iterable, np.array]
) -> Union[float, Iterable, np.array]:
    """
    Args:
        i: periodic interest rate in decimal form
    Returns:
        Present value of a perpetuity due with an interest rate of i
    """
    return np.divide(1, discount_rate(i))


def annuity_fv(
    n: Union[int, Iterable, np.array], i: Union[float, Iterable, np.array]
) -> Union[float, Iterable, np.array]:
    """
    Args:
        n: years
        i: periodic interest rate in decimal form
    Returns:
        Future value of annuity of n years with an interest rate of i
    """
    return np.multiply(annuity_pv(n, i), np.power(np.add(1, i), n))


def annuity_due_fv(
    n: Union[int, Iterable, np.array], i: Union[float, Iterable, np.array]
) -> Union[float, Iterable, np.array]:
    """
    Args:
        n: years
        i: periodic interest rate in decimal form
    Returns:
        Future value of annuity of n years with an interest rate of i
    """
    return np.multiply(annuity_due_pv(n, i), np.power(np.add(1, i), n))


def increasing_annuity_pv(
    n: Union[int, Iterable, np.array], i: Union[float, Iterable, np.array]
) -> Union[float, Iterable, np.array]:
    """
    Args:
        n: years
        i: periodic interest rate in decimal form
    Returns:
        Present value of an increasing annuity of n years with
        an interest rate of i.  It is assumed that the annuity payment
        increments by 1 each period.
    """
    return np.divide(
        annuity_due_pv(n, i) - np.multiply(n, np.power(discount_factor(i), n)), i
    )


def increasing_annuity_fv(
    n: Union[int, Iterable, np.array], i: Union[float, Iterable, np.array]
) -> Union[float, Iterable, np.array]:
    """
    Args:
        n: years
        i: periodic interest rate in decimal form
    Returns:
        Future value of an increasing annuity of n years with
        an interest rate of i.  It is assumed that the annuity payment
        increments by 1 each period.
    """
    return np.divide(annuity_due_fv(n, i) - n, i)


def increasing_annuity_due_pv(
    n: Union[int, Iterable, np.array], i: Union[float, Iterable, np.array]
) -> Union[float, Iterable, np.array]:
    """
    Args:
        n: years
        i: periodic interest rate in decimal form
    Returns:
        Present value of an increasing annuity due of n years with
        an interest rate of i.  It is assumed that the annuity payment
        increments by 1 each period.
    """
    return np.multiply(np.add(1, i), increasing_annuity_pv(n, i))


def increasing_annuity_due_fv(
    n: Union[int, Iterable, np.array], i: Union[float, Iterable, np.array]
) -> Union[float, Iterable, np.array]:
    """
    Args:
        n: years
        i: periodic interest rate in decimal form
    Returns:
        Future value of an increasing annuity due of n years with
        an interest rate of i.  It is assumed that the annuity payment
        increments by 1 each period.
    """
    return np.multiply(increasing_annuity_due_pv(n, i), np.power(np.add(1, i), n))


def decreasing_annuity_pv(
    n: Union[int, Iterable, np.array], i: Union[float, Iterable, np.array]
) -> Union[float, Iterable, np.array]:
    """
    Args:
        n: years
        i: periodic interest rate in decimal form
    Returns:
        Present value of a decreasing annuity of n years with
        an interest rate of i.  It is assumed that the annuity payment
        decrements by 1 each period.
    """
    return np.divide(n - annuity_pv(n, i), i)


def decreasing_annuity_fv(
    n: Union[int, Iterable, np.array], i: Union[float, Iterable, np.array]
) -> Union[float, Iterable, np.array]:
    """
    Args:
        n: years
        i: periodic interest rate in decimal form
    Returns:
        Future value of a decreasing annuity of n years with
        an interest rate of i.  It is assumed that the annuity payment
        decrements by 1 each period.
    """
    return np.divide(np.multiply(n, np.power(np.add(1, i), n)) - annuity_fv(n, i), i)


def decreasing_annuity_due_pv(
    n: Union[int, Iterable, np.array], i: Union[float, Iterable, np.array]
) -> Union[float, Iterable, np.array]:
    """
    Args:
        n: years
        i: periodic interest rate in decimal form
    Returns:
        Present value of a decreasing annuity due of n years with
        an interest rate of i.  It is assumed that the annuity payment
        decrements by 1 each period.
    """
    return np.multiply(np.add(1, i), decreasing_annuity_pv(n, i))


def decreasing_annuity_due_fv(
    n: Union[int, Iterable, np.array], i: Union[float, Iterable, np.array]
) -> Union[float, Iterable, np.array]:
    """
    Args:
        n: years
        i: periodic interest rate in decimal form
    Returns:
        Future value of a decreasing annuity due of n years with
        an interest rate of i.  It is assumed that the annuity payment
        decrements by 1 each period.
    """
    return np.multiply(decreasing_annuity_due_pv(n, i), np.power(np.add(1, i), n))


def geo_increasing_annuity_pv(
    n: Union[int, Iterable, np.array],
    i: Union[int, Iterable, np.array],
    k: Union[int, Iterable, np.array],
) -> Union[float, Iterable, np.array]:
    """
    Args:
        n: years
        i: periodic interest rate in decimal form
        k: periodic payment growth rate
    Returns:
        Present value of a geometrically increasing annuity of
        n years with an interest rate of i and payment growth rate
        of k.
    """
    result = []
    n = list(n) if not isinstance(n, numbers.Number) else [n]
    i = list(i) if not isinstance(i, numbers.Number) else [i]
    k = list(k) if not isinstance(k, numbers.Number) else [k]
    for index, growth_rate in enumerate(k):
        if growth_rate == 0:
            result.append(annuity_pv(n, i))
        elif growth_rate == i[index]:
            result.append(np.multiply(n, discount_factor(i)))
        else:
            result.append(
                np.divide(
                    1 - np.power(np.divide(np.add(1, k), np.add(1, i)), n),
                    np.subtract(i, k),
                )
            )
    return np.array(result) if len(result) > 1 else result[0]
