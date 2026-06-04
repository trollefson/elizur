import pytest

from elizur.life.table import LifeTable, MultiDecrementTable
from elizur.life.util import InvalidAge, InvalidInterval

MORTALITY = (0.01, 0.02, 0.03, 0.04, 1.0)
LAPSES = (0.05, 0.04, 0.03, 0.02, 0.0)


@pytest.fixture(scope="module")
def mortality_table():
    return LifeTable(MORTALITY)


@pytest.fixture(scope="module")
def mdt(mortality_table):
    return MultiDecrementTable(mortality_table, LAPSES)


def test_multi_decrement__qx_tau_equals_combined_decrements(mdt):
    for age in range(len(MORTALITY) - 1):
        qd = MORTALITY[age]
        qw = LAPSES[age]
        expected = 1.0 - (1.0 - qd) * (1.0 - qw)
        assert round(mdt.qx_tau(age), 10) == round(expected, 10)


def test_multi_decrement__qx_d_udd_approximation(mdt):
    for age in range(len(MORTALITY) - 1):
        qd = MORTALITY[age]
        qw = LAPSES[age]
        expected = qd * (1.0 - qw / 2.0)
        assert round(mdt.qx_d(age), 10) == round(expected, 10)


def test_multi_decrement__qx_w_udd_approximation(mdt):
    for age in range(len(MORTALITY) - 1):
        qd = MORTALITY[age]
        qw = LAPSES[age]
        expected = qw * (1.0 - qd / 2.0)
        assert round(mdt.qx_w(age), 10) == round(expected, 10)


def test_multi_decrement__px_tau_is_complement_of_qx_tau(mdt):
    for age in range(len(MORTALITY) - 1):
        assert round(mdt.px_tau(age) + mdt.qx_tau(age), 10) == 1.0


def test_multi_decrement__lx_tau_decreases_monotonically(mdt):
    lx_values = [mdt.lx_tau(age) for age in range(len(MORTALITY))]
    assert all(lx_values[i] >= lx_values[i + 1] for i in range(len(lx_values) - 1))


def test_multi_decrement__dx_d_and_dx_w_sum_to_total_decrements(mdt):
    for age in range(len(MORTALITY) - 1):
        total_dx = mdt.lx_tau(age) * mdt.qx_tau(age)
        assert round(mdt.dx_d(age) + mdt.dx_w(age), 8) == round(total_dx, 8)


def test_multi_decrement__npx_tau_consistent_with_lx(mdt):
    assert round(mdt.npx_tau(2, 0), 10) == round(
        mdt.lx_tau(2) / mdt.lx_tau(0), 10
    )


def test_multi_decrement__qx_d_out_of_bounds_returns_one(mdt):
    assert mdt.qx_d(1000) == 1.0


def test_multi_decrement__qx_w_out_of_bounds_returns_zero(mdt):
    assert mdt.qx_w(1000) == 0.0


def test_multi_decrement__lx_tau_out_of_bounds_returns_zero(mdt):
    assert mdt.lx_tau(1000) == 0.0


def test_multi_decrement__qx_d_invalid_age_raises(mdt):
    with pytest.raises(InvalidAge):
        mdt.qx_d(-1)


def test_multi_decrement__qx_w_invalid_age_raises(mdt):
    with pytest.raises(InvalidAge):
        mdt.qx_w(-1)


def test_multi_decrement__npx_tau_invalid_interval_raises(mdt):
    with pytest.raises(InvalidInterval):
        mdt.npx_tau(0, 0)


def test_multi_decrement__mismatched_lapse_rates_raises():
    table = LifeTable(MORTALITY)
    with pytest.raises(ValueError):
        MultiDecrementTable(table, [0.05, 0.04])


def test_multi_decrement__to_frame_shape(mdt):
    frame = mdt.to_frame()
    assert frame.shape == (mdt.table_size, 10)


def test_multi_decrement__to_frame_columns(mdt):
    frame = mdt.to_frame()
    assert frame.columns == [
        "age", "qx_prime_d", "qx_prime_w",
        "qx_d", "qx_w", "qx_tau", "px_tau",
        "lx_tau", "dx_d", "dx_w",
    ]


def test_multi_decrement__to_frame_qx_tau_matches_method(mdt):
    frame = mdt.to_frame()
    for age, val in enumerate(frame["qx_tau"].to_list()):
        assert round(val, 10) == round(mdt.qx_tau(age), 10)


def test_multi_decrement__to_frame_lx_tau_matches_method(mdt):
    frame = mdt.to_frame()
    for age, val in enumerate(frame["lx_tau"].to_list()):
        assert round(val, 6) == round(mdt.lx_tau(age), 6)
