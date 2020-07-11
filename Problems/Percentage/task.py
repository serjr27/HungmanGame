def get_percentage(number: float, round_digits=None):
    return '{}%'.format(round((number * 100), round_digits))
