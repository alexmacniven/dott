from .runner import DayRunner, HourRunner


def dott(func, rule, timer):
    if rule == "hour":
        HourRunner(func, timer)
    elif rule == "day":
        DayRunner(func, timer)
    else:
        raise RuntimeError("{0} is an invalid rule".format(rule))