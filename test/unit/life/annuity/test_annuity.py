"""
Expected test values for level annuities, increasing_annuity_pv,
and decreasing_annuity_fv are from a Texas Instruments BA II Plus
"""
import numpy as np

import elizur.life.annuity as ann


def test_discount_factor():
    assert np.round(ann.discount_factor(0.07), 3) == 0.935


def test_discount_factor__array():
    assert np.allclose(
        ann.discount_factor(np.array([0.07, 0.06, 0.05])),
        np.array([0.93457944, 0.94339623, 0.95238095]),
        atol=1e-03,
    )


def test_interest_rate():
    assert np.round(ann.interest_rate(0.0654206), 3) == 0.07


def test_interest_rate__array():
    assert np.allclose(
        ann.interest_rate(np.array([0.0654206, 0.057, 0.048])),
        np.array([0.07, 0.06, 0.05]),
        atol=1e-03,
    )


def test_discount_rate():
    assert np.round(ann.discount_rate(0.07), 3) == 0.065


def test_discount_rate__array():
    assert np.allclose(
        ann.discount_rate(np.array([0.07, 0.06, 0.05])),
        np.array([0.0654206, 0.057, 0.048]),
        atol=1e-03,
    )


def test_annuity_pv():
    assert np.round(ann.annuity_pv(n=10, i=0.07), 3) == 7.024


def test_annuity_pv__array():
    assert np.allclose(
        ann.annuity_pv(n=np.array([10, 20, 30]), i=np.array([0.07, 0.06, 0.05])),
        np.array([7.024, 11.47, 15.372]),
        atol=1e-03,
    )


def test_annuity_due_pv():
    assert np.round(ann.annuity_due_pv(n=10, i=0.07), 3) == 7.515


def test_annuity_due_pv__array():
    assert np.allclose(
        ann.annuity_due_pv(n=np.array([10, 20, 30]), i=np.array([0.07, 0.06, 0.05])),
        np.array([7.515, 11.47, 15.372]),
        np.array([7.515, 12.158, 16.141]),
        atol=1e-03,
    )


def test_perpetuity_pv():
    assert np.round(ann.perpetuity_pv(i=0.07), 3) == 14.286


def test_perpetuity_pv__array():
    assert np.allclose(
        ann.perpetuity_pv(i=np.array([0.07, 0.06, 0.05])),
        np.array([14.286, 16.667, 20]),
        atol=1e-03,
    )


def test_perpetuity_due_pv():
    assert np.round(ann.perpetuity_due_pv(i=0.07), 3) == 15.286


def test_perpetuity_due_pv__array():
    assert np.allclose(
        ann.perpetuity_due_pv(i=np.array([0.07, 0.06, 0.05])),
        np.array([15.286, 17.667, 21]),
        atol=1e-03,
    )


def test_annuity_fv():
    assert np.round(ann.annuity_fv(n=10, i=0.07), 3) == 13.816


def test_annuity_fv__array():
    assert np.allclose(
        ann.annuity_fv(n=np.array([10, 20, 30]), i=np.array([0.07, 0.06, 0.05])),
        np.array([13.816, 36.786, 66.439]),
        atol=1e-03,
    )


def test_increasing_annuity_pv():
    assert np.round(ann.increasing_annuity_pv(n=10, i=0.07), 3) == 34.739


def test_increasing_annuity_pv__array():
    assert np.allclose(
        ann.increasing_annuity_pv(
            n=np.array([10, 20, 30]), i=np.array([0.07, 0.06, 0.05])
        ),
        np.array([34.739, 98.700, 183.995]),
        atol=1e-03,
    )


def test_increasing_annuity_due_pv():
    assert np.round(ann.increasing_annuity_due_pv(n=10, i=0.07), 3) == 37.171


def test_increasing_annuity_due_pv__array():
    assert np.allclose(
        ann.increasing_annuity_due_pv(
            n=np.array([10, 20, 30]), i=np.array([0.07, 0.06, 0.05])
        ),
        np.array([37.171, 104.622, 193.195]),
        atol=1e-03,
    )


def test_increasing_annuity_fv():
    assert np.round(ann.increasing_annuity_fv(n=10, i=0.07), 3) == 68.337


def test_increasing_annuity_fv__array():
    assert np.allclose(
        ann.increasing_annuity_fv(
            n=np.array([10, 20, 30]), i=np.array([0.07, 0.06, 0.05])
        ),
        np.array([68.337, 316.545, 795.216]),
        atol=1e-03,
    )


def test_increasing_annuity_due_fv():
    assert np.round(ann.increasing_annuity_due_fv(n=10, i=0.07), 3) == 73.121


def test_increasing_annuity_due_fv__array():
    assert np.allclose(
        ann.increasing_annuity_due_fv(
            n=np.array([10, 20, 30]), i=np.array([0.07, 0.06, 0.05])
        ),
        np.array([73.121, 335.538, 834.977]),
        atol=1e-03,
    )


def test_decreasing_annuity_pv():
    assert np.round(ann.decreasing_annuity_pv(n=10, i=0.07), 3) == 42.520


def test_decreasing_annuity_pv__array():
    assert np.allclose(
        ann.decreasing_annuity_pv(
            n=np.array([10, 20, 30]), i=np.array([0.07, 0.06, 0.05])
        ),
        np.array([42.520, 142.168, 292.551]),
        atol=1e-03,
    )


def test_decreasing_annuity_due_pv():
    assert np.round(ann.decreasing_annuity_due_pv(n=10, i=0.07), 3) == 45.497


def test_decreasing_annuity_due_pv__array():
    assert np.allclose(
        ann.decreasing_annuity_due_pv(
            n=np.array([10, 20, 30]), i=np.array([0.07, 0.06, 0.05])
        ),
        np.array([45.497, 150.698, 307.179]),
        atol=1e-03,
    )


def test_decreasing_annuity_fv():
    assert np.round(ann.decreasing_annuity_fv(n=10, i=0.07), 3) == 83.644


def test_decreasing_annuity_fv__array():
    assert np.allclose(
        ann.decreasing_annuity_fv(
            n=np.array([10, 20, 30]), i=np.array([0.07, 0.06, 0.05])
        ),
        np.array([83.644, 455.952, 1264.388]),
        atol=1e-03,
    )


def test_decreasing_annuity_due_fv():
    assert np.round(ann.decreasing_annuity_due_fv(n=10, i=0.07), 3) == 89.499


def test_decreasing_annuity_due_fv__array():
    assert np.allclose(
        ann.decreasing_annuity_due_fv(
            n=np.array([10, 20, 30]), i=np.array([0.07, 0.06, 0.05])
        ),
        np.array([89.499, 483.309, 1327.608]),
        atol=1e-03,
    )


def test_geo_increasing_annuity_pv__payment_growth_rate_is_zero():
    assert np.round(ann.geo_increasing_annuity_pv(n=10, i=0.07, k=0.00), 3) == 7.024


def test_geo_increasing_annuity_pv__array_payment_growth_rate_is_zero():
    assert np.allclose(
        ann.geo_increasing_annuity_pv(
            n=np.array([10, 20, 30]),
            i=np.array([0.07, 0.06, 0.05]),
            k=np.array([0, 0, 0]),
        ),
        np.array([7.024]),
        atol=1e-03,
    )


def test_geo_increasing_annuity_pv__payment_growth_rate_equals_interest_rate():
    assert np.round(ann.geo_increasing_annuity_pv(n=10, i=0.07, k=0.07), 3) == 9.346


def test_geo_increasing_annuity_pv__array_payment_growth_rate_equals_interest_rate():
    assert np.allclose(
        ann.geo_increasing_annuity_pv(
            n=np.array([10, 20, 30]),
            i=np.array([0.07, 0.06, 0.05]),
            k=np.array([0.07, 0.06, 0.05]),
        ),
        np.array([9.346]),
        atol=1e-03,
    )


def test_geo_increasing_annuity_pv():
    assert np.round(ann.geo_increasing_annuity_pv(n=10, i=0.07, k=0.03), 3) == 7.921


def test_geo_increasing_annuity_pv__array():
    assert np.allclose(
        ann.geo_increasing_annuity_pv(
            n=np.array([10, 20, 30]),
            i=np.array([0.07, 0.06, 0.05]),
            k=np.array([0.03, 0.04, 0.08]),
        ),
        np.array([7.921, 15.83987234, 44.27572926]),
        atol=1e-03,
    )
