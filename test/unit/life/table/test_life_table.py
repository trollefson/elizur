# pylint: disable=redefined-outer-name

import pytest

from elizur.life.annuity import discount_factor
from elizur.life.table import LifeTable
from elizur.life.util import InvalidAge, InvalidInterval


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


L0 = 100000


@pytest.fixture
def life_table():
    return LifeTable(TEST_TABLE)


def test_life_table__w(life_table):
    assert life_table.w == len(TEST_TABLE) - 1


def test_life_table__qx(life_table):
    assert life_table.qx(0) == TEST_TABLE[0]
    assert life_table.qx(life_table.w) == 1
    assert life_table.qx(7) == TEST_TABLE[7]


def test_life_table__px(life_table):
    assert life_table.px(0) == 1 - TEST_TABLE[0]
    assert life_table.px(life_table.w) == 0
    assert life_table.px(7) == 1 - TEST_TABLE[7]


def test_life_table__lx(life_table):
    assert life_table.lx(0) == L0
    assert life_table.lx(1) == L0 * (1 - TEST_TABLE[0])


def test_life_table__dx(life_table):
    l1 = L0 * (1 - TEST_TABLE[0])
    l2 = l1 * (1 - TEST_TABLE[1])
    assert life_table.dx(1) == l1 - l2


def test_life_table__ex(life_table):
    assert life_table.ex(life_table.w) == 0
    assert round(life_table.ex(life_table.w - 2), 7) == 0.75812500


def test_life_table__mx(life_table):
    l1 = L0 * (1 - TEST_TABLE[0])
    l2 = l1 * (1 - TEST_TABLE[1])
    d2 = l1 - l2
    assert life_table.mx(1) == d2 / l1


def test_life_table__nqx(life_table):
    l1 = L0 * (1 - TEST_TABLE[0])
    l2 = l1 * (1 - TEST_TABLE[1])
    l3 = l2 * (1 - TEST_TABLE[2])
    assert life_table.nqx(2, 1) == (l1 - l3) / l1


def test_life_table__npx(life_table):
    l1 = L0 * (1 - TEST_TABLE[0])
    l2 = l1 * (1 - TEST_TABLE[1])
    l3 = l2 * (1 - TEST_TABLE[2])
    assert life_table.npx(2, 1) == l3 / l1


def test_life_table__nlx(life_table):
    l1 = L0 * (1 - TEST_TABLE[0])
    l2 = l1 * (1 - TEST_TABLE[1])
    assert life_table.nlx(2, 1) == l1 + l2


def test_life_table__ndx(life_table):
    l1 = L0 * (1 - TEST_TABLE[0])
    l2 = l1 * (1 - TEST_TABLE[1])
    l3 = l2 * (1 - TEST_TABLE[2])
    d1 = l1 - l2
    d2 = l2 - l3
    assert life_table.ndx(2, 1) == d2 + d1


def test_life_table__nmx(life_table):
    l1 = L0 * (1 - TEST_TABLE[0])
    l2 = l1 * (1 - TEST_TABLE[1])
    l3 = l2 * (1 - TEST_TABLE[2])
    d1 = l1 - l2
    d2 = l2 - l3
    assert life_table.nmx(2, 1) == (d2 + d1) / (l2 + l1)


def test_life_table__tqxn(life_table):
    l1 = L0 * (1 - TEST_TABLE[0])
    l2 = l1 * (1 - TEST_TABLE[1])
    l3 = l2 * (1 - TEST_TABLE[2])
    _1p1 = l2 / l1
    _1q2 = (l2 - l3) / l2
    assert life_table.tqxn(1, 1, 1) == _1p1 * _1q2


def test_life_table__mx_invalid_x(life_table):
    with pytest.raises(InvalidAge):
        life_table.mx(-7)


def test_life_table__ex_invalid_x(life_table):
    with pytest.raises(InvalidAge):
        life_table.ex(-7)


def test_life_table__dx_invalid_x(life_table):
    with pytest.raises(InvalidAge):
        life_table.dx(-7)


def test_life_table__lx_invalid_x(life_table):
    with pytest.raises(InvalidAge):
        life_table.lx(-7)


def test_life_table__px_invalid_x(life_table):
    with pytest.raises(InvalidAge):
        life_table.px(-7)


def test_life_table__qx_invalid_x(life_table):
    with pytest.raises(InvalidAge):
        life_table.qx(-7)


def test_life_table__nqx_invalid_x_n(life_table):
    with pytest.raises(InvalidInterval):
        life_table.nqx(-2, 1)
    with pytest.raises(InvalidAge):
        life_table.nqx(2, -1)
    with pytest.raises(InvalidAge):
        life_table.nqx(-2, -1)
    with pytest.raises(InvalidAge):
        life_table.nqx(0, -1)
    with pytest.raises(InvalidInterval):
        life_table.nqx(0, 1)


def test_life_table__npx_invalid_x_n(life_table):
    with pytest.raises(InvalidInterval):
        life_table.npx(-2, 1)
    with pytest.raises(InvalidAge):
        life_table.npx(2, -1)
    with pytest.raises(InvalidAge):
        life_table.npx(-2, -1)
    with pytest.raises(InvalidAge):
        life_table.npx(0, -1)
    with pytest.raises(InvalidInterval):
        life_table.npx(0, 1)


def test_life_table__nlx_invalid_x_n(life_table):
    with pytest.raises(InvalidInterval):
        life_table.nlx(-2, 1) == 0
    with pytest.raises(InvalidAge):
        life_table.nlx(2, -1) == 0
    with pytest.raises(InvalidAge):
        life_table.nlx(-2, -1) == 0
    with pytest.raises(InvalidAge):
        life_table.nlx(0, -1) == 0
    with pytest.raises(InvalidInterval):
        life_table.nlx(0, 1) == 0


def test_life_table__ndx_invalid_x_n(life_table):
    with pytest.raises(InvalidInterval):
        life_table.ndx(-2, 1) == 0
    with pytest.raises(InvalidAge):
        life_table.ndx(2, -1) == 0
    with pytest.raises(InvalidAge):
        life_table.ndx(-2, -1) == 0
    with pytest.raises(InvalidAge):
        life_table.ndx(0, -1) == 0
    with pytest.raises(InvalidInterval):
        life_table.ndx(0, 1) == 0


def test_life_table__nmx_invalid_x_n(life_table):
    with pytest.raises(InvalidInterval):
        life_table.nmx(-2, 1) == 0
    with pytest.raises(InvalidAge):
        life_table.nmx(2, -1) == 0
    with pytest.raises(InvalidAge):
        life_table.nmx(-2, -1) == 0
    with pytest.raises(InvalidAge):
        life_table.nmx(0, -1) == 0
    with pytest.raises(InvalidInterval):
        life_table.nmx(0, 1) == 0


def test_life_table__tqxn_invalid_x_n_t(life_table):
    with pytest.raises(InvalidInterval):
        life_table.tqxn(-2, 1, 1) == 0
    with pytest.raises(InvalidInterval):
        life_table.tqxn(2, -1, 1) == 0
    with pytest.raises(InvalidAge):
        life_table.tqxn(2, 1, -1) == 0
    with pytest.raises(InvalidInterval):
        life_table.tqxn(-1, -1, 1) == 0
    with pytest.raises(InvalidAge):
        life_table.tqxn(-1, 1, -1) == 0
    with pytest.raises(InvalidAge):
        life_table.tqxn(1, -1, -1) == 0
    with pytest.raises(InvalidInterval):
        life_table.tqxn(-2, -1, 0) == 0
    with pytest.raises(InvalidInterval):
        life_table.tqxn(0, 2, 2) == 0
    with pytest.raises(InvalidInterval):
        life_table.tqxn(0, 0, 2) == 0
    with pytest.raises(InvalidInterval):
        life_table.tqxn(0, 0, 0) == 0


def test_life_table__get_qxs(life_table):
    actual = life_table.get_qxs()
    for i, e in enumerate(TEST_TABLE):
        assert e == actual[i]


def test_life_table__get_pxs(life_table):
    expected = map(lambda x: 1 - x, TEST_TABLE)
    actual = life_table.get_pxs()
    for i, e in enumerate(expected):
        assert e == actual[i]


def test_life_table__get_lxs(life_table):
    test_lxs = [L0]
    for i in TEST_TABLE:
        test_lxs.append(test_lxs[-1] * (1 - i))
    lxs = life_table.get_lxs()
    for index in range(len(lxs)):
        assert round(lxs[index], 7) == round(test_lxs[index], 7)


def test_life_table__can_have_name():
    life_table = LifeTable(TEST_TABLE, name="test table", description="my test table")
    assert life_table.name == "test table"


def test_life_table__can_have_description():
    life_table = LifeTable(TEST_TABLE, name="test table", description="my test table")
    assert life_table.description == "my test table"


def test_life_table__Dx(life_table):
    expected = life_table.get_lxs()[10] * 1.07**-10
    assert round(expected, 7) == round(life_table.Dx(10, 0.07), 7)


def test_life_table__Dx_invalid_age(life_table):
    with pytest.raises(InvalidAge):
        life_table.Dx(-1, 0.07)


def test_life_table__Nx(life_table):
    expected = (
        life_table.Dx(98, 0.07) + life_table.Dx(99, 0.07) + life_table.Dx(100, 0.07)
    )
    assert expected == life_table.Nx(98, 0.07)


def test_life_table__Nx_invalid_age(life_table):
    with pytest.raises(InvalidAge):
        life_table.Nx(-1, 0.07)


def test_life_table__Sx(life_table):
    expected = (
        life_table.Nx(98, 0.07) + life_table.Nx(99, 0.07) + life_table.Nx(100, 0.07)
    )
    assert expected == life_table.Sx(98, 0.07)


def test_life_table__Sx_invalid_age(life_table):
    with pytest.raises(InvalidAge):
        life_table.Sx(-1, 0.07)


def test_life_table__Cx(life_table):
    lxs = life_table.get_lxs()
    expected = (lxs[10] - lxs[11]) * (1.07) ** -11
    assert round(expected, 7) == round(life_table.Cx(10, 0.07), 7)


def test_life_table__Cx_invalid_age(life_table):
    with pytest.raises(InvalidAge):
        life_table.Cx(-1, 0.07)


def test_life_table__Mx(life_table):
    expected = (
        life_table.Cx(98, 0.07) + life_table.Cx(99, 0.07) + life_table.Cx(100, 0.07)
    )
    assert round(expected, 7) == round(life_table.Mx(98, 0.07), 7)


def test_life_table__Mx_invalid_age(life_table):
    with pytest.raises(InvalidAge):
        life_table.Mx(-1, 0.07)


def test_life_table__Rx(life_table):
    expected = (
        life_table.Mx(98, 0.07) + life_table.Mx(99, 0.07) + life_table.Mx(100, 0.07)
    )
    assert round(expected, 7) == round(life_table.Rx(98, 0.07), 7)


def test_life_table__Rx_invalid_age(life_table):
    with pytest.raises(InvalidAge):
        life_table.Rx(-1, 0.07)


def test_life_table__Dx_as_annuity_pv(life_table):
    lxs = life_table.get_lxs()
    expected = (
        discount_factor(0.07) * (lxs[1] / lxs[0])
        + (discount_factor(0.07) ** 2) * (lxs[2] / lxs[0])
        + (discount_factor(0.07) ** 3) * (lxs[3] / lxs[0])
    )
    actual = (
        (life_table.Dx(1, 0.07) / life_table.Dx(0, 0.07))
        + (life_table.Dx(2, 0.07) / life_table.Dx(0, 0.07))
        + (life_table.Dx(3, 0.07) / life_table.Dx(0, 0.07))
    )
    assert expected == actual


def test_life_table__Nx_and_Dx_as_annuity_due_pv(life_table):
    lxs = life_table.get_lxs()
    expected = (
        1
        + discount_factor(0.07) * (lxs[1] / lxs[0])
        + (discount_factor(0.07) ** 2) * (lxs[2] / lxs[0])
    )
    actual = (life_table.Nx(0, 0.07) - life_table.Nx(3, 0.07)) / life_table.Dx(0, 0.07)
    assert round(expected, 7) == round(actual, 7)


def test_life_table__Mx_and_Dx_as_term_insurance_pv(life_table):
    expected = (
        (life_table.qx(0) * discount_factor(0.07))
        + (life_table.qx(1) * life_table.px(0) * discount_factor(0.07) ** (2))
        + (
            life_table.qx(2)
            * life_table.px(1)
            * life_table.px(0)
            * discount_factor(0.07) ** 3
        )
    )
    actual = (life_table.Mx(0, 0.07) - life_table.Mx(3, 0.07)) / life_table.Dx(0, 0.07)
    assert round(expected, 7) == round(actual, 7)


def test_life_table__Rx_Mx_and_Dx_as_term_increasing_insurance_pv(life_table):
    expected = (
        (life_table.qx(0) * discount_factor(0.07))
        + (2 * life_table.qx(1) * life_table.px(0) * discount_factor(0.07) ** (2))
        + (
            3
            * life_table.qx(2)
            * life_table.px(1)
            * life_table.px(0)
            * discount_factor(0.07) ** 3
        )
    )
    actual = (
        life_table.Rx(0, 0.07) - life_table.Rx(3, 0.07) - 3 * life_table.Mx(3, 0.07)
    ) / life_table.Dx(0, 0.07)
    assert round(expected, 7) == round(actual, 7)


def test_life_table__Ax(life_table):
    expected = life_table.Mx(0, 0.07) / life_table.Dx(0, 0.07)
    actual = life_table.Ax(0, 0.07)
    assert round(expected, 7) == round(actual, 7)


def test_life_table__Axn(life_table):
    expected = (
        (life_table.qx(0) * discount_factor(0.07))
        + (life_table.qx(1) * life_table.px(0) * discount_factor(0.07) ** (2))
        + (
            life_table.qx(2)
            * life_table.px(1)
            * life_table.px(0)
            * discount_factor(0.07) ** 3
        )
    )
    actual = life_table.Axn(0, 0.07, 3)
    assert round(expected, 7) == round(actual, 7)


def test_life_table__IAx(life_table):
    expected = life_table.Rx(0, 0.07) / life_table.Dx(0, 0.07)
    actual = life_table.IAx(0, 0.07)
    assert round(expected, 7) == round(actual, 7)


def test_life_table__IAxn(life_table):
    expected = (
        (life_table.qx(0) * discount_factor(0.07))
        + (2 * life_table.qx(1) * life_table.px(0) * discount_factor(0.07) ** (2))
        + (
            3
            * life_table.qx(2)
            * life_table.px(1)
            * life_table.px(0)
            * discount_factor(0.07) ** 3
        )
    )
    actual = life_table.IAxn(0, 0.07, 3)
    assert round(expected, 7) == round(actual, 7)


def test_life_table__ax(life_table):
    expected = life_table.Nx(1, 0.07) / life_table.Dx(0, 0.07)
    actual = life_table.ax(0, 0.07)
    assert round(actual, 7) == round(expected, 7)


def test_life_table__axn(life_table):
    lxs = life_table.get_lxs()
    expected = (
        discount_factor(0.07) * (lxs[1] / lxs[0])
        + (discount_factor(0.07) ** 2) * (lxs[2] / lxs[0])
        + (discount_factor(0.07) ** 3) * (lxs[3] / lxs[0])
    )
    actual = life_table.axn(0, 0.07, 3)
    assert round(expected, 7) == round(actual, 7)


def test_life_table__ax_due(life_table):
    expected = life_table.Nx(0, 0.07) / life_table.Dx(0, 0.07)
    actual = life_table.ax_due(0, 0.07)
    assert round(actual, 7) == round(expected, 7)


def test_life_table__axn_due(life_table):
    lxs = life_table.get_lxs()
    expected = (
        1
        + discount_factor(0.07) * (lxs[1] / lxs[0])
        + (discount_factor(0.07) ** 2) * (lxs[2] / lxs[0])
    )
    actual = life_table.axn_due(0, 0.07, 3)
    assert round(expected, 7) == round(actual, 7)


def test_life_table__qxs(life_table):
    qxs = life_table.qxs
    for index in range(qxs.size):
        assert qxs[index] == life_table.qx(index)


def test_life_table__pxs(life_table):
    pxs = life_table.pxs
    for index in range(pxs.size):
        assert pxs[index] == life_table.px(index)


def test_life_table__lxs(life_table):
    lxs = life_table.lxs
    for index in range(lxs.size):
        assert lxs[index] == life_table.lx(index)


def test_life_table__npxs(life_table):
    npxs = life_table.npxs(10)
    for index in range(npxs.size):
        assert npxs[index] == life_table.npx(10, index)


def test_life_table__nqxs(life_table):
    nqxs = life_table.nqxs(10)
    for index in range(nqxs.size):
        assert nqxs[index] == life_table.nqx(10, index)


def test_life_table__tqxns(life_table):
    tqxns = life_table.tqxns(5, 10)
    for index in range(tqxns.size):
        assert tqxns[index] == life_table.tqxn(5, 10, index)


def test_life_table__qx_bounds(life_table):
    assert life_table.qx(1000) == 1
    assert life_table.qx(life_table.table_size) == 1


def test_life_table__px_bounds(life_table):
    assert life_table.px(1000) == 0
    assert life_table.px(life_table.table_size) == 0


def test_life_table__lx_bounds(life_table):
    assert life_table.lx(1000) == 0
    assert life_table.lx(life_table.table_size) == 0


def test_life_table__dx_bounds(life_table):
    assert life_table.dx(1000) == 0
    assert life_table.dx(life_table.table_size) == 0


def test_life_table__mx_bounds(life_table):
    assert life_table.mx(1000) == 1
    assert life_table.mx(life_table.table_size) == 1


def test_life_table__ex_bounds(life_table):
    assert life_table.ex(1000) == 0
    assert life_table.ex(life_table.table_size) == 0


def test_life_table__nqx_bounds(life_table):
    assert life_table.nqx(5, life_table.table_size) == 1
    assert life_table.nqx(5, life_table.table_size - 3) == 1
    assert life_table.nqx(5, life_table.table_size - 5) == 1
    assert life_table.nqx(5, life_table.table_size - 6) != 1


def test_life_table__npx_bounds(life_table):
    assert life_table.npx(5, life_table.table_size) == 0
    assert life_table.npx(5, life_table.table_size - 3) == 0
    assert life_table.npx(5, life_table.table_size - 5) == 0
    assert life_table.npx(5, life_table.table_size - 6) != 0


def test_life_table__nmx_bounds(life_table):
    assert life_table.nmx(5, life_table.table_size) == 1
    assert life_table.nmx(5, life_table.table_size - 3) != 1


def test_life_table__tqxn_bounds(life_table):
    assert life_table.tqxn(5, 10, life_table.table_size) == 1
    assert life_table.tqxn(5, 10, life_table.table_size - 10) == 0
    assert life_table.tqxn(5, 10, life_table.table_size - 9) == 0
    assert life_table.tqxn(5, 10, life_table.table_size - 15) == 1
    assert life_table.tqxn(8, 10, life_table.table_size - 15) == 1
