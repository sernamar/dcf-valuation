from matplotlib import pyplot as plt
from numpy.random import default_rng


def compute_dcf(cash_flow_values, discount_rate):
    dcf = 0
    for year, cash_flow in enumerate(cash_flow_values):
        dcf = dcf + cash_flow / pow(1 + discount_rate, year + 1)
    return dcf


def get_random_numbers(mean=0, standard_deviation=1, size=None):
    "Generate one or more normal random numbers."
    rng = default_rng()
    return rng.normal(mean, standard_deviation, size)


def simulate_cash_flow_values(cash_flow_data, size=1):
    """Simulate cash flow values from their mean and standard deviation.
The function returns a list of numpy arrays with cash flow values.

Example:
    Input:
        cash_flow_data: [[100, 20], [-500, 10]]
        size: 3

    Output: [array([113.36222158,  77.39297513,  77.15350701]),
 array([-506.58408186, -503.27855081, -500.37690891])]"""
    simulated = [get_random_numbers(mean, standard_deviation, size)
                 for mean, standard_deviation in cash_flow_data]
    return simulated


def combine_cash_flow_simulations(simulations):
    cash_flow_values = []
    if (simulations != []):
        number_of_simulations = len(simulations[0])
        for i in range(number_of_simulations):
            cash_flow_values.append([item[i] for item in simulations])

    return cash_flow_values


def simulate_dcf(cash_flow_data, discount_rate, number_of_simulations):
    simulated = combine_cash_flow_simulations(simulate_cash_flow_values(
        cash_flow_data, number_of_simulations))
    return list(map(lambda x: compute_dcf(x, discount_rate), simulated))


if __name__ == '__main__':
    cash_flow_data = [[100, 3], [100, 5], [400, 7], [400, 9], [600, 11]]
    discount_rate = .05

    number_of_simulations = 1000

    dcf = simulate_dcf(cash_flow_data, discount_rate, number_of_simulations)

    plt.hist(dcf)
    plt.show()
