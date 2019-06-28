"""
Expected test values for level annuities, increasing_annuity_pv,
and decreasing_annuity_fv are from a Texas Instruments BA II Plus
"""
import elizur.life.annuity as ann


def test_discount_factor():
    assert round(ann.discount_factor(0.07), 7) == 0.9345794


def test_interest_rate():
    assert round(ann.interest_rate(0.0654206), 7) == 0.07


def test_discount_rate():
    assert round(ann.discount_rate(0.07), 7) == 0.0654206


def test_annuity_pv():
    assert round(ann.annuity_pv(n=10, i=0.07), 7) == 7.0235815


def test_annuity_due_pv():
    assert round(ann.annuity_due_pv(n=10, i=0.07), 7) == 7.5152322


def test_perpetuity_pv():
    assert round(ann.perpetuity_pv(i=0.07), 7) == 14.2857143


def test_perpetuity_due_pv():
    assert round(ann.perpetuity_due_pv(i=0.07), 7) == 15.2857143


def test_annuity_fv():
    assert round(ann.annuity_fv(n=10, i=0.07), 7) == 13.8164480


def test_increasing_annuity_pv():
    assert round(ann.increasing_annuity_pv(n=10, i=0.07), 7) == 34.7391332


def test_increasing_annuity_due_pv():
    assert round(ann.increasing_annuity_due_pv(n=10, i=0.07), 7) == 37.1708726


def test_increasing_annuity_fv():
    assert round(ann.increasing_annuity_fv(n=10, i=0.07), 7) == 68.3371331


def test_increasing_annuity_due_fv():
    assert round(ann.increasing_annuity_due_fv(n=10, i=0.07), 7) == 73.1207324


def test_decreasing_annuity_pv():
    assert round(ann.decreasing_annuity_pv(n=10, i=0.07), 7) == 42.5202637


def test_decreasing_annuity_due_pv():
    assert round(ann.decreasing_annuity_due_pv(n=10, i=0.07), 7) == 45.4966822


def test_decreasing_annuity_fv():
    assert round(ann.decreasing_annuity_fv(n=10, i=0.07), 7) == 83.6437945


def test_decreasing_annuity_due_fv():
    assert round(ann.decreasing_annuity_due_fv(n=10, i=0.07), 7) == 89.4988601


def test_geo_increasing_annuity_pv__payment_growth_rate_is_zero():
    assert round(ann.geo_increasing_annuity_pv(n=10, i=0.07, k=0.00), 7) == 7.0235815


def test_geo_increasing_annuity_pv__payment_growth_rate_equals_interest_rate():
    assert round(ann.geo_increasing_annuity_pv(n=10, i=0.07, k=0.07), 7) == 9.3457944


def test_geo_increasing_annuity_pv():
    assert round(ann.geo_increasing_annuity_pv(n=10, i=0.07, k=0.03), 7) == 7.9205265
