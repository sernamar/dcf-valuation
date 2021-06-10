def compute_dcf(cash_flow_values, discount_rate):
    dcf = 0
    for year, cash_flow in enumerate(cash_flow_values):
        dcf = dcf + cash_flow / pow(1 + discount_rate, year + 1)
    return dcf


if __name__ == '__main__':
    cash_flow_values = [1000000, 1000000, 4000000, 4000000, 6000000]
    discount_rate = .05
    dcf = compute_dcf(cash_flow_values, discount_rate)
    print(f"Discounted Cash Flow = {dcf}")
