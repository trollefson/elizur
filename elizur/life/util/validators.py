from typing import Callable


class InvalidInterval(Exception):
    """
    Custom exception raised for invalid input intervals (n)
    """


class InvalidInterestRate(Exception):
    """
    Custom exception raised for invalid input interest rates (i)
    """


class InvalidStartAge(Exception):
    """
    Custom exception raised for invalid input ages (x)
    """


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

    def validated_func(*args, **kwargs):
        """
        Args:
            arg[1] (int): age
        """
        if args[1] < 0:
            return 0.0
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

    def validated_func(*args, **kwargs):
        """
        Args:
            arg[1] (int): interval
        """
        if args[1] < 0:
            return 0.0
        return func(*args, **kwargs)

    validated_func.__doc__ = func.__doc__

    return validated_func


def validate_age_and_interval(func: Callable) -> Callable:
    # pylint: disable=unused-argument
    """
    Decorator for validating methods using actuarial notation
    age and interval input

    Args:
        func: function with inputs to validate

    Returns:
        The passed in function wrapped with input validation
    """

    def validated_func(*args, **kwargs):
        """
        Args:
            args[1] (int): age
            args[2] (int): interval
        """
        if args[1] <= 0 or args[2] < 0:
            return 0.0
        return func(*args, **kwargs)

    validated_func.__doc__ = func.__doc__

    return validated_func


def validate_age_and_interest(func: Callable) -> Callable:
    # pylint: disable=unused-argument
    """
    Decorator for validating methods using actuarial notation
    age and interest input

    Args:
        func: function with inputs to validate

    Returns:
        The passed in function wrapped with input validation
    """

    def validated_func(*args, **kwargs):
        """
        Args:
            args[1] (int): age
            args[2] (float): interest

        Raises:
            InvalidStartAge
            InvalidInterestRate
        """
        if args[1] < 0:
            raise InvalidStartAge("Start age must be greater than or equal to 0!")
        if args[2] < 0.0:
            raise InvalidInterestRate("Interest rate must be greater than 0!")
        return func(*args, **kwargs)

    validated_func.__doc__ = func.__doc__

    return validated_func


def validate_age_interest_and_interval(func: Callable) -> Callable:
    # pylint: disable=unused-argument
    """
    Decorator for validating methods using actuarial notation
    age, interest, and interval input

    Args:
        func: function with inputs to validate

    Returns:
        The passed in function wrapped with input validation
    """

    def validated_func(*args, **kwargs):
        """
        Args:
            args[1] (int): age
            args[2] (float): interest
            args[3] (int): interval

        Raises:
            InvalidStartAge
            InvalidInterestRate
            InvalidInterval
        """
        if args[1] < 0:
            raise InvalidStartAge("Start age must be greater than or equal to 0!")
        if args[2] < 0.0:
            raise InvalidInterestRate("Interest rate must be greater than 0!")
        if args[3] < 0:
            raise InvalidInterval(
                "Length of payments must be greater than or equal to 0!"
            )
        return func(*args, **kwargs)

    validated_func.__doc__ = func.__doc__

    return validated_func
