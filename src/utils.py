def time_to_decimal_hour(time_str):
    """
    Convert a time string in "h-m-s" format to a decimal hour.

    :param time_str: A string in "h-m-s" format (hours, minutes, seconds).
    :return: A decimal hour.
    """
    try:
        hours, minutes, seconds = map(float, time_str.split("-"))
        decimal_hour = hours + minutes / 60 + seconds / 3600
        return decimal_hour
    except ValueError:
        raise ValueError(
            "Invalid time format. Use 'h-m-s' format, e.g., '2-30-45' for 2 hours, 30 minutes, and 45 seconds."
        )


def calculate_y_graph(x, m_values, b_values, x_ranges):
    for i, (x_start, x_end) in enumerate(x_ranges):
        if x_start <= x <= x_end:
            m = m_values[i]
            b = b_values[i]
            return m * x + b
    raise ValueError(f"No matching x range found for x = {x}")


x_ranges = [(7, 8), (8, 9), (9, 13), (13, 14), (14, 15), (15, 20), (20, 21), (21, 22)]
m_values_CO2 = [
    1186.1614497528835,
    -430.97199341021405,
    -211.53212520593084,
    1158.48434925865,
    -549.5881383855028,
    -133.64085667215815,
    1114.9917627677098,
    -632.6194398682044,
]
b_values_CO2 = [
    -7350.247116968703,
    5586.820428336077,
    3611.861614497529,
    -14198.352553542021,
    9714.662273476117,
    3475.453047775947,
    -21497.199341021413,
    15202.635914332786,
]

m_values_mix = [
    13.662803729938126,
    -7.006578947368428,
    -2.0925928155246316,
    -0.7601818475740172,
    -7.30263157894737,
    -2.328947368421054,
    16.085526315789494,
    -8.804917959293448,
]
b_values_mix = [
    -72.09848247108395,
    93.25657894736848,
    49.030703760774315,
    49.030703760774315,
    140.62500000000003,
    66.01973684210529,
    -302.26973684210566,
    220.42959293463605,
]
