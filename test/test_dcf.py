from src.dcf import compute_dcf


def test_dcf():
    cash_flow_values = [1000000, 1000000, 4000000, 4000000, 6000000]
    discount_rate = .05
    expected = 13306728
    assert expected == round(compute_dcf(cash_flow_values, discount_rate))
