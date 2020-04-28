import csv
from typing import Callable, Dict, List


def read_soa_csv_mort_table(
    file_path, encoding: str = "Windows-1252", delimiter: str = ","
) -> Dict:
    """
    Args:
        file_path: The full file system path to the csv
        encoding: The text encoding of the csv data.  It defaults to 'Windows-1252'.
        delimiter: The delimiter of the csv data.  It defaults to ','.

    Returns:
        A dictionary with a 'values' and 'metadata' key.
    """
    raw_csv = _open_soa_csv_mort_table(
        file_path, encoding=encoding, delimiter=delimiter
    )
    processed_csv = _process_soa_csv_mort_table(raw_csv)
    return processed_csv


def _open_soa_csv_mort_table(
    file_path: str, encoding: str = "Windows-1252", delimiter: str = ","
) -> List[List[str]]:
    """
    Args:
        file_path: The full system path to the SOA csv table.
        url: The full HTTP url to the SOA csv table.
        encoding: The text encoding of the csv data.  It defaults to 'Windows-1252'.
        delimiter: The delimiter of the csv data.  It defaults to ','.

    Returns:
        A list of lists representing the csv table.  Each interior
        list has two elements representing the first and second
        columns.
    """
    encoded_csv = open(file_path, encoding=encoding)
    raw_csv = list(csv.reader(encoded_csv, delimiter=delimiter))
    return raw_csv


def _process_soa_csv_mort_table(raw_csv: List[List[str]]) -> Dict:
    """
    Args:
        raw_csv: A list of lists representing the csv table.  Each interior
                 list has two elements representing the first and second
                 columns.

    Returns:
        A dictionary with a 'values' and 'metadata' key.
    """
    # pylint: disable=too-many-branches
    table = {"metadata": {}, "values": ()}
    for index, row in enumerate(raw_csv):
        if row:
            if row[0] == "Row, Column (if applicable)->MinScaleValue:":
                table["metadata"]["min_age"] = int(row[1])
            elif row[0] == "Row, Column (if applicable)->MaxScaleValue:":
                table["metadata"]["max_age"] = int(row[1])
            elif row[0] == "Row\\Column":
                table["metadata"]["table_line_start"] = index + 1
            elif row[0] == "Table Name:":
                table["metadata"]["name"] = row[1]
            elif row[0] == "Table Description:":
                table["metadata"]["description"] = row[1]
            elif row[0] == "Provider Name:":
                table["metadata"]["author"] = row[1]
            elif row[0] == "Table Reference:":
                table["metadata"]["reference"] = row[1]
            elif row[0] == "Comments:":
                table["metadata"]["comments"] = row[1]
            elif row[0] == "Content Type:":
                table["metadata"]["content_type"] = row[1]
            elif row[0] == "Nation:":
                table["metadata"]["study_nation"] = row[1]
            elif row[0] == "Row, Column (if applicable)->Increment:":
                table["metadata"]["table_increment"] = row[1]
            elif row[0] == "Scaling Factor:":
                table["metadata"]["scaling_factor"] = row[1]
            elif row[0] == "Table Identity":
                table["metadata"]["soa_table_identity"] = row[1]
    table_start = table["metadata"]["table_line_start"]
    max_age = table["metadata"]["max_age"]
    min_age = table["metadata"]["min_age"]
    table_end = table_start + max_age - min_age + 1
    table["values"] = tuple([float(row[1]) for row in raw_csv[table_start:table_end]])
    return table


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
