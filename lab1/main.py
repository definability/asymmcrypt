from generators import *
from primitive_testing import primitive_test_wrapper
from probability_testing import probability_test_wrapper
from independence_testing import independence_test_wrapper
import os
import time

if __name__ == '__main__':
    '''
    Asymmetric Cryptography: Lab 1
    '''

    """
    Seeds initialization
    """
    seed = 1
    seed_Lemer = {'x': 0, 'm': LEMER_M, 'c': LEMER_C, 'a': LEMER_A}
    seed_Geffe = {
            'LFSRs': [GeneratorL89(1), GeneratorL89(2**18), GeneratorL20(1)]
            }
    seed_BBS = {'r': 2, 'p': BBS_P, 'q': BBS_Q}
    seed_Librarian = None
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
            'kant.txt'), 'r') as f:
        seed_Librarian = {'text': f.read()}
    """
    Generators initialization
    """
    generators = [
            GeneratorDefault(seed),
            GeneratorLemer(seed_Lemer),
            GeneratorL20(seed),
            GeneratorL89(seed),
            GeneratorGeffe(seed_Geffe),
            GeneratorBBS(seed_BBS),
            GeneratorLibrarian(seed_Librarian)
            ]
    """
    Generators testing
    """
    m = 2**20

    #print 'PRIMITIVE TESTING'
    #primitive_test_wrapper(generators, m)
    #print 'PROBABILITY TESTING'
    #probability_test_wrapper(generators, m)
    #print 'INDEPENDENCE TESTING'
    #independence_test_wrapper(generators, m)
