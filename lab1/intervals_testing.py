from chi2 import calculate_chi2_advanced, calculate_chi2_critical
from chi2_testing import chi2_test_wrapper
from math import log

MAX_VALUE = 255

def intervals_test(generator, count, r=0):
    if r is 0:
        r = 1 + int(log(count)/log(2))

    frequencies = list()
    frequencies_1 = [0] * (2**8)
    intervals = [count/r] * r
    for i in range(2**8):
        frequencies.append([0] * r)

    for i in range(r):
        for j in range(intervals[i]):
            value = generator.get_byte()
            frequencies[value][i] += 1
            frequencies_1[value] += 1
    chi2 = calculate_chi2_advanced(frequencies, frequencies_1, intervals)
    return chi2

def intervals_test_wrapper(generators, count):
    r = 1 + int(log(count)/log(2))
    chi2_test_wrapper(generators, count, 255*(r-1), lambda generators, count:
            intervals_test(generators, count, r))
