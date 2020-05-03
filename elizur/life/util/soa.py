import csv
from typing import Dict, List


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
