def discount_factor(i: float) -> float:
    """
    Args:
        i: interest rate in decimal form
    Returns:
        The related discount factor
    """
    return (1 + i) ** -1


def interest_rate(d: float) -> float:
    """
    Args:
        d: discount rate in decimal form
    Returns:
        The related interest rate in decimal form
    """
    return d / (1 - d)


def discount_rate(i: float) -> float:
    """
    Args:
        i: interest rate in decimal form
    Returns:
        The related discount rate
    """
    return i / (1 + i)


def annuity_pv(n: int, i: float) -> float:
    """
    Args:
        n: years
        i: periodic interest rate in decimal form
    Returns:
        Present value of annuity of n years with an interest rate of i
    """
    return (1 - discount_factor(i) ** n) / i


def annuity_due_pv(n: int, i: float) -> float:
    """
    Args:
        n: years
        i: periodic interest rate in decimal form
    Returns:
        Present value of annuity of n years with an interest rate of i
    """
    return (1 - discount_factor(i) ** n) / discount_rate(i)


def perpetuity_pv(i: float) -> float:
    """
    Args:
        i: periodic interest rate in decimal form
    Returns:
        Present value of a perpetuity with an interest rate of i
    """
    return i ** -1


def perpetuity_due_pv(i: float) -> float:
    """
    Args:
        i: periodic interest rate in decimal form
    Returns:
        Present value of a perpetuity due with an interest rate of i
    """
    return discount_rate(i) ** -1


def annuity_fv(n: int, i: float) -> float:
    """
    Args:
        n: years
        i: periodic interest rate in decimal form
    Returns:
        Future value of annuity of n years with an interest rate of i
    """
    return annuity_pv(n, i) * (1 + i) ** n


def annuity_due_fv(n: int, i: float) -> float:
    """
    Args:
        n: years
        i: periodic interest rate in decimal form
    Returns:
        Future value of annuity of n years with an interest rate of i
    """
    return annuity_due_pv(n, i) * (1 + i) ** n


def increasing_annuity_pv(n: int, i: float) -> float:
    """
    Args:
        n: years
        i: periodic interest rate in decimal form
    Returns:
        Present value of an increasing annuity of n years with
        an interest rate of i.  It is assumed that the annuity payment
        increments by 1 each period.
    """
    return (annuity_due_pv(n, i) - n * discount_factor(i) ** n) / i


def increasing_annuity_fv(n: int, i: float) -> float:
    """
    Args:
        n: years
        i: periodic interest rate in decimal form
    Returns:
        Future value of an increasing annuity of n years with
        an interest rate of i.  It is assumed that the annuity payment
        increments by 1 each period.
    """
    return (annuity_due_fv(n, i) - n) / i


def increasing_annuity_due_pv(n: int, i: float) -> float:
    """
    Args:
        n: years
        i: periodic interest rate in decimal form
    Returns:
        Present value of an increasing annuity due of n years with
        an interest rate of i.  It is assumed that the annuity payment
        increments by 1 each period.
    """
    return (1 + i) * increasing_annuity_pv(n, i)


def increasing_annuity_due_fv(n: int, i: float) -> float:
    """
    Args:
        n: years
        i: periodic interest rate in decimal form
    Returns:
        Future value of an increasing annuity due of n years with
        an interest rate of i.  It is assumed that the annuity payment
        increments by 1 each period.
    """
    return increasing_annuity_due_pv(n, i) * (1 + i) ** n


def decreasing_annuity_pv(n: int, i: float) -> float:
    """
    Args:
        n: years
        i: periodic interest rate in decimal form
    Returns:
        Present value of a decreasing annuity of n years with
        an interest rate of i.  It is assumed that the annuity payment
        decrements by 1 each period.
    """
    return (n - annuity_pv(n, i)) / i


def decreasing_annuity_fv(n: int, i: float) -> float:
    """
    Args:
        n: years
        i: periodic interest rate in decimal form
    Returns:
        Future value of a decreasing annuity of n years with
        an interest rate of i.  It is assumed that the annuity payment
        decrements by 1 each period.
    """
    return (n * (1 + i) ** n - annuity_fv(n, i)) / i


def decreasing_annuity_due_pv(n: int, i: float) -> float:
    """
    Args:
        n: years
        i: periodic interest rate in decimal form
    Returns:
        Present value of a decreasing annuity due of n years with
        an interest rate of i.  It is assumed that the annuity payment
        decrements by 1 each period.
    """
    return (1 + i) * decreasing_annuity_pv(n, i)


def decreasing_annuity_due_fv(n: int, i: float) -> float:
    """
    Args:
        n: years
        i: periodic interest rate in decimal form
    Returns:
        Future value of a decreasing annuity due of n years with
        an interest rate of i.  It is assumed that the annuity payment
        decrements by 1 each period.
    """
    return decreasing_annuity_due_pv(n, i) * (1 + i) ** n


def geo_increasing_annuity_pv(n: int, i: int, k: int) -> float:
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
    if k == 0:
        return annuity_pv(n, i)
    if k == i:
        return n * discount_factor(i)
    return (1 - ((1 + k) / (1 + i)) ** n) / (i - k)
