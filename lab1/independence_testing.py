from chi2 import calculate_chi2_advanced, calculate_chi2_critical
from chi2_testing import chi2_test_wrapper

BYTE_SIZE = 8

def independence_test(generator, count):
    n = count/2
    frequencies = list()
    frequencies_1 = [0] * (2**8)
    frequencies_2 = [0] * (2**8)
    for i in range(2**8):
        frequencies.append([0] * (2**8))
    for i in range(n):
        numbers = (generator.get_byte(), generator.get_byte())
        frequencies[numbers[0]][numbers[1]] += 1
        frequencies_1[numbers[0]] += 1
        frequencies_2[numbers[1]] += 1
    chi2 = calculate_chi2_advanced(frequencies, frequencies_1, frequencies_2)
    return chi2

def independence_test_wrapper(generators, count):
    chi2_test_wrapper(generators, count, 255**2, independence_test)
    '''
    for generator in generators:
        print independence_test(generator, count)
        print 'Quantile:', calculate_chi2_critical(0.99, 255**2)
    '''
