def calculate_frequencies(generator, count):
    frequencies = [0] * 256
    for i in range(count):
        frequencies[generator.get_byte()] += 1
    return frequencies

def yield_frequencies(generator, count):
    frequencies = calculate_frequencies(generator, count)
    for f in frequencies:
        yield f

def primitive_test_wrapper(generators, count):
    g = generators[1]
    for generator in generators:
        print "Testing generator %s..." % generator.get_name()
        for f in yield_frequencies(generator, count):
            #print int(count/256.0 - f),
            print f,
        print ''
        print ''
