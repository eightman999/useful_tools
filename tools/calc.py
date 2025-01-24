from scipy.special import math


def significant_figures(number, n):
    n = 10^n
    result = math.floor(number * n) / n
    return result

