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


def generate_cash_flow_values(mean_and_standard_deviation, size=1):
    """Generate a list of numpy arrays with cash flow values generated with their
mean and standard deviation.

Example:
    Input:  [[1000, 50], [1010, 80]]
    Output: [array([ 954.43264945,  985.02731123, 1013.48890123]),
 array([1068.63236401, 1045.83419035,  903.87104662])]"""
    return [get_random_numbers(mean, standard_deviation, size)
            for mean, standard_deviation in mean_and_standard_deviation]


if __name__ == '__main__':
    cash_flow_values = [1000000, 1000000, 4000000, 4000000, 6000000]
    discount_rate = .05
    dcf = compute_dcf(cash_flow_values, discount_rate)
    print(f"Discounted Cash Flow = {dcf}")
    print("Standard random numbers =", get_random_numbers(0, 1, 5))
