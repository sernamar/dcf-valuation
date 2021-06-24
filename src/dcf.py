from statistics import mean, median, stdev

from matplotlib import pyplot
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


def simulate_cash_flow_values(cash_flow_data, number_of_simulations=1):
    """Simulate cash flow values from their mean and standard deviation.
The function returns a list of numpy arrays with cash flow values.

Example:
    Input:
        cash_flow_data: [[100, 20], [-500, 10]]
        number_of_simulations: 3

    Output: [array([113.36222158,  77.39297513,  77.15350701]),
 array([-506.58408186, -503.27855081, -500.37690891])]"""
    if cash_flow_data and number_of_simulations > 0:
        simulated = [get_random_numbers(mean, standard_deviation,
                                        number_of_simulations)
                     for mean, standard_deviation in cash_flow_data]
    else:
        simulated = []
    return simulated


def combine_cash_flow_simulations(simulations):
    cash_flow_values = []
    if simulations:
        number_of_simulations = len(simulations[0])
        for i in range(number_of_simulations):
            cash_flow_values.append([item[i] for item in simulations])

    return cash_flow_values


def simulate_dcf(cash_flow_data, discount_rate, number_of_simulations):
    simulated = combine_cash_flow_simulations(simulate_cash_flow_values(
        cash_flow_data, number_of_simulations))
    return [compute_dcf(cash_flow_values, discount_rate)
            for cash_flow_values in simulated]


def print_basic_statistics(data):
    print("Mean:", round(mean(data)))
    print("Median:", round(median(data)))
    print("Standard Deviation:", round(stdev(data)))


if __name__ == '__main__':
    cash_flow_data = [[10000, 1000], [10000, 1000], [10000, 1000],
                      [10000, 5000], [11000, 1500], [11000, 1500],
                      [11000, 1500], [11000, 7000], [12000, 2000],
                      [12000 + 200000, 50000]]

    discount_rate = .05

    number_of_simulations = 1000

    estimated_dcf = simulate_dcf(
        cash_flow_data, discount_rate, number_of_simulations)

    print_basic_statistics(estimated_dcf)

    pyplot.hist(estimated_dcf)
    pyplot.show()
