from generators import *
from primitive_testing import primitive_test_wrapper
from probability_testing import probability_test_wrapper
from independence_testing import independence_test_wrapper
from intervals_testing import intervals_test_wrapper
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
            #'LFSRs': [GeneratorL20(1), GeneratorL20(2**10), GeneratorL20(2**17)]
            'LFSRs': [GeneratorLFSR('L1',
                {'x':1<<10, 'register_size': 11, 'mask': (1<<8) | (1<<10)}),
                GeneratorLFSR('L2',
                {'x':1<<8, 'register_size': 9, 'mask':
                    (1<<4) | (1<<5) | (1<<7) | (1<<8)}),
                GeneratorLFSR('L3',
                {'x':1<<7, 'register_size': 10, 'mask': (1<<6) | (1<<9)})
                ]

            }
    seed_BBS = {'r': 2, 'p': BBS_P, 'q': BBS_Q}
    seed_Librarian = None
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
            'file.txt'), 'r') as f:
        seed_Librarian = {'text': f.read()}
    """
    Generators initialization
    """
    generators = [
            GeneratorDefault(seed),
            GeneratorLemer(seed_Lemer),
            GeneratorLemerLast(seed_Lemer),
            GeneratorL20(seed),
            GeneratorL89(seed),
            GeneratorGeffe(seed_Geffe),
            GeneratorBBS(seed_BBS),
            GeneratorBBSBits(seed_BBS),
            GeneratorLibrarian(seed_Librarian)
            ]
    """
    Generators testing
    """
    m = 2**20

    print 'PRIMITIVE TESTING'
    primitive_test_wrapper(generators, m)
    print 'PROBABILITY TESTING'
    probability_test_wrapper(generators, m)
    print 'INDEPENDENCE TESTING'
    independence_test_wrapper(generators, m)
    print 'INTERVALS TESTING'
    intervals_test_wrapper(generators, m)
    print 'END OF TESTS'
