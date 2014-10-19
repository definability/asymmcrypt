from chi2 import calculate_chi2, calculate_chi2_critical, alphas

def chi2_test_wrapper(generators, count, l, test):
    chi2_theoretical = [calculate_chi2_critical(1-alpha, l) for alpha in alphas]
    for generator in generators:
        print "Testing generator %s..." % generator.get_name()
        chi2 = test(generator, count)
        print "I've got Chi squared as %.2f" % chi2
        for i, alpha in enumerate(alphas):
            print "This value",
            if chi2 < chi2_theoretical[i]:
                print "fits",
            else:
                print "does not fit",
            print "the %.2f significance level (theoretical value is %.2f)" % (
                alpha, chi2_theoretical[i])
        print ''
