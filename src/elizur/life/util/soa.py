import csv
from typing import TypedDict


class SoaTableMetadata(TypedDict, total=False):
    """Metadata parsed from an SOA CSV mortality table header."""

    min_age: int
    max_age: int
    table_line_start: int
    name: str
    description: str
    author: str
    reference: str
    comments: str
    content_type: str
    study_nation: str
    table_increment: str
    scaling_factor: str
    soa_table_identity: str


class SoaTable(TypedDict):
    """Parsed SOA mortality table with metadata and qx values."""

    metadata: SoaTableMetadata
    values: tuple[float, ...]


def read_soa_csv_mort_table(
    file_path: str, encoding: str = "Windows-1252", delimiter: str = ","
) -> SoaTable:
    """Parse an SOA CSV mortality table file.

    Args:
        file_path: The full file system path to the csv.
        encoding: The text encoding of the csv data. Defaults to 'Windows-1252'.
        delimiter: The delimiter of the csv data. Defaults to ','.

    Returns:
        A SoaTable with 'metadata' and 'values' keys.
    """
    raw_csv = _open_soa_csv_mort_table(
        file_path, encoding=encoding, delimiter=delimiter
    )
    return _process_soa_csv_mort_table(raw_csv)


def _open_soa_csv_mort_table(
    file_path: str, encoding: str = "Windows-1252", delimiter: str = ","
) -> list[list[str]]:
    """Read an SOA CSV mortality table file into a list of rows.

    Args:
        file_path: The full system path to the SOA csv table.
        encoding: The text encoding of the csv data. Defaults to 'Windows-1252'.
        delimiter: The delimiter of the csv data. Defaults to ','.

    Returns:
        A list of rows, each row being a list of column strings.
    """
    with open(file_path, encoding=encoding) as f:
        return list(csv.reader(f, delimiter=delimiter))


def _process_soa_csv_mort_table(raw_csv: list[list[str]]) -> SoaTable:
    """Parse a raw SOA CSV into a structured SoaTable.

    Args:
        raw_csv: A list of rows from the SOA CSV file.

    Returns:
        A SoaTable with 'metadata' and 'values' keys.
    """
    metadata: SoaTableMetadata = {}  # type: ignore[typeddict-item]
    for index, row in enumerate(raw_csv):
        if not row:
            continue
        match row[0]:
            case "Row, Column (if applicable)->MinScaleValue:":
                metadata["min_age"] = int(row[1])
            case "Row, Column (if applicable)->MaxScaleValue:":
                metadata["max_age"] = int(row[1])
            case "Row\\Column":
                metadata["table_line_start"] = index + 1
            case "Table Name:":
                metadata["name"] = row[1]
            case "Table Description:":
                metadata["description"] = row[1]
            case "Provider Name:":
                metadata["author"] = row[1]
            case "Table Reference:":
                metadata["reference"] = row[1]
            case "Comments:":
                metadata["comments"] = row[1]
            case "Content Type:":
                metadata["content_type"] = row[1]
            case "Nation:":
                metadata["study_nation"] = row[1]
            case "Row, Column (if applicable)->Increment:":
                metadata["table_increment"] = row[1]
            case "Scaling Factor:":
                metadata["scaling_factor"] = row[1]
            case "Table Identity":
                metadata["soa_table_identity"] = row[1]

    table_start = metadata["table_line_start"]
    table_end = table_start + metadata["max_age"] - metadata["min_age"] + 1
    values = tuple(float(row[1]) for row in raw_csv[table_start:table_end])
    return SoaTable(metadata=metadata, values=values)
