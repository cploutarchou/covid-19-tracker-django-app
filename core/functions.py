import datetime


def percentage_difference_calculator(old_value, new_value):
    val1 = float(old_value)
    val2 = float(new_value)
    rate = (((val1 - val2) / ((val1 + val2) / 2)) * 100)
    if rate is not None:
        return format(--rate, ".2f")
    else:
        return False


def get_yesterday_date():
    yesterday = datetime.date.today() - datetime.timedelta(days=2)
    yesterday = yesterday.strftime('%Y-%m-%d')
    return yesterday


def get_two_dates_before():
    res = datetime.date.today() - datetime.timedelta(days=3)
    res = res.strftime('%Y-%m-%d')
    return res
