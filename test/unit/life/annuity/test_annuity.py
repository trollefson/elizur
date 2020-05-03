"""
Expected test values for level annuities, increasing_annuity_pv,
and decreasing_annuity_fv are from a Texas Instruments BA II Plus
"""
import numpy as np
import pytest

import elizur.life.annuity as ann


@pytest.mark.parametrize(
    "interest_rates, expected",
    [
        (0.07, 0.935),
        ([0.07, 0.06, 0.05], np.array([0.93457944, 0.94339623, 0.95238095])),
        ((0.07, 0.06, 0.05), np.array([0.93457944, 0.94339623, 0.95238095])),
        (np.array((0.07, 0.06, 0.05)), np.array([0.93457944, 0.94339623, 0.95238095])),
    ]
)
def test_discount_factor(interest_rates, expected):
    assert np.allclose(
        ann.discount_factor(interest_rates),
        expected,
        atol=1e-03
    )


@pytest.mark.parametrize(
    "discount_factors, expected",
    [
        (0.0654206, 0.07),
        ([0.0654206, 0.057, 0.048], np.array([0.07, 0.06, 0.05])),
        ((0.0654206, 0.057, 0.048), np.array([0.07, 0.06, 0.05])),
        (np.array((0.0654206, 0.057, 0.048)), np.array([0.07, 0.06, 0.05])),
    ]
)
def test_interest_rate(discount_factors, expected):
    assert np.allclose(
        ann.interest_rate(discount_factors),
        expected,
        atol=1e-03
    )


@pytest.mark.parametrize(
    "interest_rates, expected",
    [
        (0.07, 0.065),
        ([0.07, 0.06, 0.05], np.array([0.0654206, 0.057, 0.048])),
        ((0.07, 0.06, 0.05), np.array([0.0654206, 0.057, 0.048])),
        (np.array((0.07, 0.06, 0.05)), np.array([0.0654206, 0.057, 0.048])),
    ]
)
def test_discount_rate(interest_rates, expected):
    assert np.allclose(
        ann.discount_rate(interest_rates),
        expected,
        atol=1e-03
    )


@pytest.mark.parametrize(
    "periods, interest_rates, expected",
    [
        (10, 0.07, 7.024),
        ([10, 20, 30], [0.07, 0.06, 0.05], np.array([7.024, 11.47, 15.372])),
        ((10, 20, 30), (0.07, 0.06, 0.05), np.array([7.024, 11.47, 15.372])),
        (np.array((10, 20, 30)), np.array((0.07, 0.06, 0.05)), np.array([7.024, 11.47, 15.372])),
    ]
)
def test_annuity_pv(periods, interest_rates, expected):
    assert np.allclose(
        ann.annuity_pv(n=periods, i=interest_rates),
        expected,
        atol=1e-03
    )


@pytest.mark.parametrize(
    "periods, interest_rates, expected",
    [
        (10, 0.07, 7.515),
        ([10, 20, 30], [0.07, 0.06, 0.05], np.array([7.515, 12.158, 16.141])),
        ((10, 20, 30), (0.07, 0.06, 0.05), np.array([7.515, 12.158, 16.141])),
        (np.array((10, 20, 30)), np.array((0.07, 0.06, 0.05)), np.array([7.515, 12.158, 16.141])),
    ]
)
def test_annuity_due_pv(periods, interest_rates, expected):
    assert np.allclose(
        ann.annuity_due_pv(n=periods, i=interest_rates),
        expected,
        atol=1e-03
    )


@pytest.mark.parametrize(
    "interest_rates, expected",
    [
        (0.07, 14.286),
        ([0.07, 0.06, 0.05], np.array([14.286, 16.667, 20])),
        ((0.07, 0.06, 0.05), np.array([14.286, 16.667, 20])),
        (np.array((0.07, 0.06, 0.05)), np.array([14.286, 16.667, 20])),
    ]
)
def test_perpetuity_pv(interest_rates, expected):
    assert np.allclose(
        ann.perpetuity_pv(i=interest_rates),
        expected,
        atol=1e-03
    )


@pytest.mark.parametrize(
    "interest_rates, expected",
    [
        (0.07, 15.286),
        ([0.07, 0.06, 0.05], np.array([15.286, 17.667, 21])),
        ((0.07, 0.06, 0.05), np.array([15.286, 17.667, 21])),
        (np.array((0.07, 0.06, 0.05)), np.array([15.286, 17.667, 21])),
    ]
)
def test_perpetuity_due_pv(interest_rates, expected):
    assert np.allclose(
        ann.perpetuity_due_pv(i=interest_rates),
        expected,
        atol=1e-03
    )


@pytest.mark.parametrize(
    "periods, interest_rates, expected",
    [
        (10, 0.07, 13.816),
        ([10, 20, 30], [0.07, 0.06, 0.05], np.array([13.816, 36.786, 66.439])),
        ((10, 20, 30), (0.07, 0.06, 0.05), np.array([13.816, 36.786, 66.439])),
        (np.array((10, 20, 30)), np.array((0.07, 0.06, 0.05)), np.array([13.816, 36.786, 66.439])),
    ]
)
def test_annuity_fv(periods, interest_rates, expected):
    assert np.allclose(
        ann.annuity_fv(n=periods, i=interest_rates),
        expected,
        atol=1e-03
    )


@pytest.mark.parametrize(
    "periods, interest_rates, expected",
    [
        (10, 0.07, 34.739),
        ([10, 20, 30], [0.07, 0.06, 0.05], np.array([34.739, 98.700, 183.995])),
        ((10, 20, 30), (0.07, 0.06, 0.05), np.array([34.739, 98.700, 183.995])),
        (np.array((10, 20, 30)), np.array((0.07, 0.06, 0.05)), np.array([34.739, 98.700, 183.995])),
    ]
)
def test_increasing_annuity_pv(periods, interest_rates, expected):
    assert np.allclose(
        ann.increasing_annuity_pv(n=periods, i=interest_rates),
        expected,
        atol=1e-03
    )


@pytest.mark.parametrize(
    "periods, interest_rates, expected",
    [
        (10, 0.07, 37.171),
        ([10, 20, 30], [0.07, 0.06, 0.05], np.array([37.171, 104.622, 193.195])),
        ((10, 20, 30), (0.07, 0.06, 0.05), np.array([37.171, 104.622, 193.195])),
        (np.array((10, 20, 30)), np.array((0.07, 0.06, 0.05)), np.array([37.171, 104.622, 193.195])),
    ]
)
def test_increasing_annuity_due_pv(periods, interest_rates, expected):
    assert np.allclose(
        ann.increasing_annuity_due_pv(n=periods, i=interest_rates),
        expected,
        atol=1e-03
    )


@pytest.mark.parametrize(
    "periods, interest_rates, expected",
    [
        (10, 0.07, 68.337),
        ([10, 20, 30], [0.07, 0.06, 0.05], np.array([68.337, 316.545, 795.216])),
        ((10, 20, 30), (0.07, 0.06, 0.05), np.array([68.337, 316.545, 795.216])),
        (np.array((10, 20, 30)), np.array((0.07, 0.06, 0.05)), np.array([68.337, 316.545, 795.216])),
    ]
)
def test_increasing_annuity_fv(periods, interest_rates, expected):
    assert np.allclose(
        ann.increasing_annuity_fv(n=periods, i=interest_rates),
        expected,
        atol=1e-03
    )


@pytest.mark.parametrize(
    "periods, interest_rates, expected",
    [
        (10, 0.07, 73.121),
        ([10, 20, 30], [0.07, 0.06, 0.05], np.array([73.121, 335.538, 834.977])),
        ((10, 20, 30), (0.07, 0.06, 0.05), np.array([73.121, 335.538, 834.977])),
        (np.array((10, 20, 30)), np.array((0.07, 0.06, 0.05)), np.array([73.121, 335.538, 834.977])),
    ]
)
def test_increasing_annuity_due_fv(periods, interest_rates, expected):
    assert np.allclose(
        ann.increasing_annuity_due_fv(n=periods, i=interest_rates),
        expected,
        atol=1e-03
    )


@pytest.mark.parametrize(
    "periods, interest_rates, expected",
    [
        (10, 0.07, 42.520),
        ([10, 20, 30], [0.07, 0.06, 0.05], np.array([42.520, 142.168, 292.551])),
        ((10, 20, 30), (0.07, 0.06, 0.05), np.array([42.520, 142.168, 292.551])),
        (np.array((10, 20, 30)), np.array((0.07, 0.06, 0.05)), np.array([42.520, 142.168, 292.551])),
    ]
)
def test_decreasing_annuity_pv(periods, interest_rates, expected):
    assert np.allclose(
        ann.decreasing_annuity_pv(n=periods, i=interest_rates),
        expected,
        atol=1e-03
    )


@pytest.mark.parametrize(
    "periods, interest_rates, expected",
    [
        (10, 0.07, 45.497),
        ([10, 20, 30], [0.07, 0.06, 0.05], np.array([45.497, 150.698, 307.179])),
        ((10, 20, 30), (0.07, 0.06, 0.05), np.array([45.497, 150.698, 307.179])),
        (np.array((10, 20, 30)), np.array((0.07, 0.06, 0.05)), np.array([45.497, 150.698, 307.179])),
    ]
)
def test_decreasing_annuity_due_pv(periods, interest_rates, expected):
    assert np.allclose(
        ann.decreasing_annuity_due_pv(n=periods, i=interest_rates),
        expected,
        atol=1e-03
    )


@pytest.mark.parametrize(
    "periods, interest_rates, expected",
    [
        (10, 0.07, 83.644),
        ([10, 20, 30], [0.07, 0.06, 0.05], np.array([83.644, 455.952, 1264.388])),
        ((10, 20, 30), (0.07, 0.06, 0.05), np.array([83.644, 455.952, 1264.388])),
        (np.array((10, 20, 30)), np.array((0.07, 0.06, 0.05)), np.array([83.644, 455.952, 1264.388])),
    ]
)
def test_decreasing_annuity_fv(periods, interest_rates, expected):
    assert np.allclose(
        ann.decreasing_annuity_fv(n=periods, i=interest_rates),
        expected,
        atol=1e-03
    )


@pytest.mark.parametrize(
    "periods, interest_rates, expected",
    [
        (10, 0.07, 89.499),
        ([10, 20, 30], [0.07, 0.06, 0.05], np.array([89.499, 483.309, 1327.608])),
        ((10, 20, 30), (0.07, 0.06, 0.05), np.array([89.499, 483.309, 1327.608])),
        (np.array((10, 20, 30)), np.array((0.07, 0.06, 0.05)), np.array([89.499, 483.309, 1327.608])),
    ]
)
def test_decreasing_annuity_due_fv(periods, interest_rates, expected):
    assert np.allclose(
        ann.decreasing_annuity_due_fv(n=periods, i=interest_rates),
        expected,
        atol=1e-03
    )


@pytest.mark.parametrize(
    "periods, interest_rates, payment_growth_rates, expected",
    [
        (
            10, 0.07, 0.03, 7.921
        ),
        (
            [10, 20, 30], [0.07, 0.06, 0.05], [0.03, 0.04, 0.08],
            np.array([7.921, 15.83987234, 44.27572926])
        ),
        (
            (10, 20, 30), (0.07, 0.06, 0.05), (0.03, 0.04, 0.08),
            np.array([7.921, 15.83987234, 44.27572926])
        ),
        (
            np.array((10, 20, 30)), np.array((0.07, 0.06, 0.05)), np.array((0.03, 0.04, 0.08)),
            np.array([7.921, 15.83987234, 44.27572926])
        ),
    ]
)
def test_geo_increasing_annuity_pv(periods, interest_rates, payment_growth_rates, expected):
    assert np.allclose(
        ann.geo_increasing_annuity_pv(n=periods, i=interest_rates, k=payment_growth_rates),
        expected,
        atol=1e-03
    )


@pytest.mark.parametrize(
    "periods, interest_rates, payment_growth_rates, expected",
    [
        (
            10, 0.07, 0, 7.024
        ),
        (
            [10, 20, 30], [0.07, 0.06, 0.05], [0, 0, 0],
            np.array([7.024, 11.46992122, 15.37245103])
        ),
        (
            (10, 20, 30), (0.07, 0.06, 0.05), (0, 0, 0),
            np.array([7.024, 11.46992122, 15.37245103])
        ),
        (
            np.array((10, 20, 30)), np.array((0.07, 0.06, 0.05)), np.array((0, 0, 0)),
            np.array([7.024, 11.46992122, 15.37245103])
        ),
    ]
)
def test_geo_increasing_annuity_pv__payment_growth_rate_is_zero(periods, interest_rates, payment_growth_rates, expected):
    assert np.allclose(
        ann.geo_increasing_annuity_pv(n=periods, i=interest_rates, k=payment_growth_rates),
        expected,
        atol=1e-03
    )


@pytest.mark.parametrize(
    "periods, interest_rates, payment_growth_rates, expected",
    [
        (
            10, 0.07, 0.07, 9.346
        ),
        (
            [10, 20, 30], [0.07, 0.06, 0.05], [0.07, 0.06, 0.05],
            np.array([9.346, 18.86792453, 28.57142857])
        ),
        (
            (10, 20, 30), (0.07, 0.06, 0.05), (0.07, 0.06, 0.05),
            np.array([9.346, 18.86792453, 28.57142857])
        ),
        (
            np.array((10, 20, 30)), np.array((0.07, 0.06, 0.05)), np.array((0.07, 0.06, 0.05)),
            np.array([9.346, 18.86792453, 28.57142857])
        ),
    ]
)
def test_geo_increasing_annuity_pv__payment_growth_rate_equals_interest_rate(periods, interest_rates, payment_growth_rates, expected):
    assert np.allclose(
        ann.geo_increasing_annuity_pv(n=periods, i=interest_rates, k=payment_growth_rates),
        expected,
        atol=1e-03
    )
