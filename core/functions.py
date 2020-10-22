def percentage_difference_calculator(old_value, new_value):
    val1 = float(old_value)
    val2 = float(new_value)
    rate = (((val1 - val2) / ((val1 + val2) / 2)) * 100)
    rate = -rate
    return format(rate, ".2f")
