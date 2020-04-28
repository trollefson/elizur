# pylint: disable=redefined-outer-name,missing-docstring

from os.path import join

import pytest

from elizur.life.table import LifeTable
from elizur.life.util import read_soa_csv_mort_table
from elizur.life.util.soa import _open_soa_csv_mort_table, _process_soa_csv_mort_table


EXPECTED_QXS = (
    0.00501,
    0.00337,
    0.0026,
    0.0022,
    0.00196,
    0.0018,
    0.00164,
    0.00147,
    0.00127,
    0.00111,
    0.00103,
    0.00103,
    0.00107,
    0.00115,
    0.00121,
    0.00123,
    0.00127,
    0.00131,
    0.00136,
    0.0014,
    0.00146,
    0.00152,
    0.00159,
    0.00165,
    0.00174,
    0.00182,
    0.00192,
    0.00203,
    0.00215,
    0.00228,
    0.00242,
    0.00258,
    0.00275,
    0.00295,
    0.00315,
    0.00338,
    0.00363,
    0.0039,
    0.00421,
    0.00453,
    0.00489,
    0.00528,
    0.00571,
    0.00618,
    0.00669,
    0.00725,
    0.00786,
    0.00852,
    0.00926,
    0.01005,
    0.01092,
    0.01186,
    0.01289,
    0.01402,
    0.01524,
    0.01658,
    0.01803,
    0.01961,
    0.02134,
    0.02321,
    0.02525,
    0.02748,
    0.02988,
    0.03251,
    0.03537,
    0.03847,
    0.04183,
    0.04548,
    0.04945,
    0.05375,
    0.05841,
    0.06345,
    0.06892,
    0.07483,
    0.08123,
    0.08814,
    0.09559,
    0.10364,
    0.1123,
    0.12163,
    0.13166,
    0.14243,
    0.15397,
    0.16634,
    0.17954,
    0.19364,
    0.20863,
    0.2246,
    0.24147,
    0.25928,
    0.27798,
    0.29755,
    0.31776,
    0.33846,
    0.3583,
    0.39994,
    0.48251,
    0.61759,
    0.77724,
    1.0,
)


@pytest.fixture
def soa_csv_path():
    return join("test", "unit", "life", "util", "mortality_table_1.csv")


def test__open_soa_csv_mort_table__file_path(soa_csv_path):
    csv_table = _open_soa_csv_mort_table(file_path=soa_csv_path)
    assert isinstance(csv_table, list)


def test__process_soa_csv_mort_table(soa_csv_path):
    csv_table = _open_soa_csv_mort_table(file_path=soa_csv_path)
    csv_table = _process_soa_csv_mort_table(csv_table)
    assert csv_table["metadata"]["name"] == "1941 CSO Basic Table, ANB"
    assert csv_table["values"] == EXPECTED_QXS


def test__process_soa_csv_mort_table__can_pass_values_to_life_table(soa_csv_path):
    csv_table = _open_soa_csv_mort_table(file_path=soa_csv_path)
    csv_table = _process_soa_csv_mort_table(csv_table)
    life_table = LifeTable(csv_table["values"])
    assert life_table.get_qxs() == EXPECTED_QXS


def test_read_soa_csv_mort_table(soa_csv_path):
    csv_table = read_soa_csv_mort_table(soa_csv_path)
    life_table = LifeTable(csv_table["values"])
    assert life_table.get_qxs() == EXPECTED_QXS
