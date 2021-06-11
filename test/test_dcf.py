from src.dcf import compute_dcf, get_random_numbers


def test_dcf():
    cash_flow_values = [1000000, 1000000, 4000000, 4000000, 6000000]
    discount_rate = .05
    expected = 13306728
    assert expected == round(compute_dcf(cash_flow_values, discount_rate))


def test_get_random_numbers():
    # check that we get the right number of elements
    assert 0 == len(get_random_numbers(size=0))
    assert 1 == len(get_random_numbers(size=1))
    assert 4 == len(get_random_numbers(size=4))
