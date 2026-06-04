import functools
from collections.abc import Callable
from typing import TypeVar

F = TypeVar("F", bound=Callable[..., object])


class InvalidInterval(Exception):
    """Raised when an actuarial interval input (n or t) is invalid."""


class InvalidAge(Exception):
    """Raised when an actuarial age input (x) is invalid."""


def _get_args_dict(fn: Callable[..., object], args: tuple, kwargs: dict) -> dict:
    """Map positional and keyword arguments to their parameter names.

    Traverses the ``__wrapped__`` chain set by ``functools.wraps`` to reach
    the original unwrapped function, so stacked decorators resolve the correct
    parameter names regardless of wrapping depth.

    Args:
        fn: The (possibly wrapped) function whose parameter names are used.
        args: Positional arguments passed to the wrapper.
        kwargs: Keyword arguments passed to the wrapper.

    Returns:
        A dict mapping parameter names to their argument values.
    """
    original = fn
    while hasattr(original, "__wrapped__"):
        original = original.__wrapped__
    args_names = original.__code__.co_varnames[: original.__code__.co_argcount]
    return {**dict(zip(args_names, args)), **kwargs}


def validate_age(func: F) -> F:
    """Validate that the age argument ``x`` is non-negative.

    Args:
        func: A method that accepts an age parameter named ``x``.

    Returns:
        The wrapped function with age validation applied.

    Raises:
        InvalidAge: If ``x`` is less than 0.
    """

    @functools.wraps(func)
    def validated_func(*args: object, **kwargs: object) -> object:
        args_dict = _get_args_dict(func, args, kwargs)
        if args_dict["x"] < 0:
            raise InvalidAge("Start age must be greater than or equal to 0!")
        return func(*args, **kwargs)

    return validated_func  # type: ignore[return-value]


def validate_interval(func: F) -> F:
    """Validate that the interval argument ``n`` is positive.

    Args:
        func: A method that accepts an interval parameter named ``n``.

    Returns:
        The wrapped function with interval validation applied.

    Raises:
        InvalidInterval: If ``n`` is less than or equal to 0.
    """

    @functools.wraps(func)
    def validated_func(*args: object, **kwargs: object) -> object:
        args_dict = _get_args_dict(func, args, kwargs)
        if args_dict["n"] <= 0:
            raise InvalidInterval("Interval must be greater than 0!")
        return func(*args, **kwargs)

    return validated_func  # type: ignore[return-value]


def validate_t_interval(func: F) -> F:
    """Validate that the failure interval argument ``t`` is positive.

    Args:
        func: A method that accepts a failure interval parameter named ``t``.

    Returns:
        The wrapped function with failure interval validation applied.

    Raises:
        InvalidInterval: If ``t`` is less than or equal to 0.
    """

    @functools.wraps(func)
    def validated_func(*args: object, **kwargs: object) -> object:
        args_dict = _get_args_dict(func, args, kwargs)
        if args_dict["t"] <= 0:
            raise InvalidInterval("Failure interval must be greater than 0!")
        return func(*args, **kwargs)

    return validated_func  # type: ignore[return-value]
