from src.dcf import (combine_cash_flow_simulations, compute_dcf,
                     get_random_numbers, simulate_cash_flow_values)


def test_compute_dcf():
    cash_flow_values = [1000000, 1000000, 4000000, 4000000, 6000000]
    discount_rate = .05
    expected = 13306728
    assert round(compute_dcf(cash_flow_values, discount_rate)) == expected


def test_get_random_numbers():
    # check that we get the right number of elements
    assert len(get_random_numbers(size=0)) == 0
    assert len(get_random_numbers(size=1)) == 1
    assert len(get_random_numbers(size=4)) == 4


def test_simulate_cash_flow_values():
    cash_flow_data = [[100, 20], [-500, 10]]
    size = 3

    simulations = simulate_cash_flow_values(cash_flow_data, size)
    number_of_years = len(cash_flow_data)

    assert len(simulations) == number_of_years
    assert len(simulations[0]) == size


def test_combine_cash_flow_simulations():
    simulations = [[1, 2, 3], [4, 5, 6]]
    expected = [[1, 4], [2, 5], [3, 6]]
    assert combine_cash_flow_simulations(simulations) == expected
