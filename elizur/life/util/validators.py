from typing import Callable

import makefun


class InvalidInterval(Exception):
    """
    Custom exception raised for invalid input intervals (n)
    """


class InvalidAge(Exception):
    """
    Custom exception raised for invalid input ages (x)
    """


def _get_args_dict(fn, args, kwargs):
    args_names = fn.__code__.co_varnames[: fn.__code__.co_argcount]
    return {**dict(zip(args_names, args)), **kwargs}


def validate_age(func: Callable) -> Callable:
    # pylint: disable=unused-argument
    """
    Decorator for validating methods using actuarial notation
    age input

    Args:
        func: function with inputs to validate

    Returns:
        The passed in function wrapped with input validation
    """

    @makefun.wraps(func)
    def validated_func(*args, **kwargs):
        """
        Args:
            contains an argument named 'x' for age
        """
        args_dict = _get_args_dict(func, args, kwargs)
        if args_dict["x"] < 0:
            raise InvalidAge("Start age must be greater than or equal to 0!")
        return func(*args, **kwargs)

    validated_func.__doc__ = func.__doc__
    return validated_func


def validate_interval(func: Callable) -> Callable:
    # pylint: disable=unused-argument
    """
    Decorator for validating methods using actuarial notation
    interval input

    Args:
        func: function with inputs to validate

    Returns:
        The passed in function wrapped with input validation
    """

    @makefun.wraps(func)
    def validated_func(*args, **kwargs):
        """
        Args:
            contains an argument named 'n' for interval
        """
        args_dict = _get_args_dict(func, args, kwargs)
        if args_dict["n"] <= 0:
            raise InvalidInterval("Interval must be greater than 0!")
        return func(*args, **kwargs)

    validated_func.__doc__ = func.__doc__
    return validated_func


def validate_t_interval(func: Callable) -> Callable:
    # pylint: disable=unused-argument
    """
    Decorator for validating methods using actuarial notation
    interval input

    Args:
        func: function with inputs to validate

    Returns:
        The passed in function wrapped with input validation
    """

    @makefun.wraps(func)
    def validated_func(*args, **kwargs):
        """
        Args:
            contains an argument named 't' for failure interval
        """
        args_dict = _get_args_dict(func, args, kwargs)
        if args_dict["t"] <= 0:
            raise InvalidInterval("Failure interval must be greater than 0!")
        return func(*args, **kwargs)

    validated_func.__doc__ = func.__doc__
    return validated_func
