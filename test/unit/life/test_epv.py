# pylint: disable=redefined-outer-name
import numpy as np
import pytest

from elizur.life import expected_present_value, InvalidEPVInputs
from elizur.life.table import LifeTable


TEST_TABLE = (
    0.006271,
    0.00041799999999999997,
    0.00028100000000000005,
    0.000201,
    0.00017,
    0.000163,
    0.000127,
    0.000123,
    0.000133,
    0.000132,
    0.000126,
    0.00013000000000000002,
    0.000145,
    0.000186,
    0.00020999999999999998,
    0.000253,
    0.000389,
    0.00044,
    0.00046600000000000005,
    0.000457,
    0.00045400000000000003,
    0.000502,
    0.000467,
    0.000453,
    0.000486,
    0.000498,
    0.00051,
    0.000507,
    0.000565,
    0.0005989999999999999,
    0.000632,
    0.0006680000000000001,
    0.0007239999999999999,
    0.000786,
    0.000853,
    0.000958,
    0.001034,
    0.0011200000000000001,
    0.001221,
    0.001433,
    0.0014930000000000002,
    0.001653,
    0.00175,
    0.0019950000000000002,
    0.002091,
    0.0023039999999999996,
    0.002376,
    0.002577,
    0.002859,
    0.0030310000000000003,
    0.003194,
    0.003522,
    0.003634,
    0.004142000000000001,
    0.0044340000000000004,
    0.0050999999999999995,
    0.005006,
    0.005886,
    0.006441,
    0.007266,
    0.007575999999999999,
    0.008476000000000001,
    0.009201,
    0.010101,
    0.011149,
    0.012107,
    0.013059,
    0.014570999999999999,
    0.015590999999999999,
    0.017396000000000002,
    0.018991,
    0.020454,
    0.022525,
    0.024633,
    0.027135000000000003,
    0.030098,
    0.032631,
    0.036094,
    0.039472,
    0.044109999999999996,
    0.0493,
    0.053298000000000005,
    0.062179000000000005,
    0.06455,
    0.07505500000000001,
    0.083221,
    0.091996,
    0.10139,
    0.111404,
    0.122037,
    0.13328,
    0.145119,
    0.157532,
    0.170488,
    0.183953,
    0.19788,
    0.21221700000000002,
    0.226905,
    0.241875,
    0.257053,
    1.0,
)


@pytest.fixture
def life_table():
    return LifeTable(TEST_TABLE)


def test_expected_present_value__n_is_3(life_table):
    n = 3
    probabilities = life_table.get_pxs()[:n]
    cash_flows = tuple([1] * n)
    interest_rates = tuple([0.07] * n)

    epv = expected_present_value(cash_flows, probabilities, interest_rates)

    expected = life_table.axn(0, 0.07, n)
    percent_error = abs(((expected - epv) / expected) * 100)
    assert percent_error < 0.5


def test_expected_present_value__n_is_10(life_table):
    n = 10
    probabilities = life_table.get_pxs()[:n]
    cash_flows = tuple([1] * n)
    interest_rates = tuple([0.07] * n)

    epv = expected_present_value(cash_flows, probabilities, interest_rates)

    expected = life_table.axn(0, 0.07, n)
    percent_error = abs(((expected - epv) / expected) * 100)
    assert percent_error < 1


def test_expected_present_value__n_is_100(life_table):
    n = 100
    probabilities = life_table.get_pxs()[:n]
    cash_flows = tuple([1] * n)
    interest_rates = tuple([0.07] * n)

    epv = expected_present_value(cash_flows, probabilities, interest_rates)

    expected = life_table.axn(0, 0.07, n)
    percent_error = abs(((expected - epv) / expected) * 100)
    assert percent_error < 1.5


def test_expected_present_value__array(life_table):
    n = 100
    probabilities = np.array(life_table.get_pxs()[:n])
    cash_flows = np.array(tuple([1] * n))
    interest_rates = np.array(tuple([0.07] * n))

    epv = expected_present_value(cash_flows, probabilities, interest_rates)

    expected = life_table.axn(0, 0.07, n)
    percent_error = abs(((expected - epv) / expected) * 100)
    assert percent_error < 1.5


def test_expected_present_value__matrix(life_table):
    n = 100
    probabilities = np.array(
        [life_table.get_pxs()[:n], life_table.get_pxs()[:n], life_table.get_pxs()[:n]]
    )
    cash_flows = np.array([tuple([1] * n), tuple([1] * n), tuple([1] * n)])
    interest_rates = np.array([tuple([0.07] * n), tuple([0.06] * n), tuple([0.05] * n)])

    epv = expected_present_value(cash_flows, probabilities, interest_rates)

    expecteds = np.array(
        [
            life_table.axn(0, 0.07, n),
            life_table.axn(0, 0.06, n),
            life_table.axn(0, 0.05, n),
        ]
    )
    for i, expected in enumerate(expecteds):
        percent_error = abs(((expected - epv[i]) / expected) * 100)
        assert percent_error < 3


def test_expected_present_value__raises_InvalidEPVInputs_when_lengths_do_not_match(
    life_table,
):
    n = 100
    probabilities = life_table.get_pxs()[:n]
    cash_flows = tuple([1] * (n + 1))
    interest_rates = tuple([0.07] * n)

    try:
        expected_present_value(cash_flows, probabilities, interest_rates)
        assert False
    except InvalidEPVInputs:
        assert True


def test_expected_present_value__raises_InvalidEPVInputs_when_ndim_greater_than_2(
    life_table,
):
    n = 100
    probabilities = life_table.get_pxs()[:n]
    cash_flows = np.array([[tuple([1] * n), tuple([1] * n), tuple([1] * n)]])
    interest_rates = tuple([0.07] * n)

    try:
        expected_present_value(cash_flows, probabilities, interest_rates)
        assert False
    except InvalidEPVInputs:
        assert True
