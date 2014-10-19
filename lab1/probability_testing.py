from primitive_testing import calculate_frequencies
from chi2 import calculate_chi2, calculate_chi2_critical, alphas
from chi2_testing import chi2_test_wrapper

def probability_test(generator, count):
    frequencies = calculate_frequencies(generator, count)
    chi2 = calculate_chi2(frequencies, count)
    return chi2

def probability_test_wrapper(generators, count):
    chi2_test_wrapper(generators, count, 255, probability_test)
