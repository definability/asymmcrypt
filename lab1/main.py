from generators import *
import time

if __name__ == '__main__':
    #seed = dict()
    #SEEDS
    # Default and LFSRs
    #seed = 1
    # Lemer
    #seed = {'x':0, 'm':LEMER_M, 'c':LEMER_C, 'a':LEMER_A} # Lemer
    # Geffe
    #seed = {'LFSRs': [GeneratorL89(1), GeneratorL89(2**18), GeneratorL20(1)]}
    # BBS
    seed = {'r': 2, 'p': BBS_P, 'q': BBS_Q}
    #g = GeneratorDefault(seed)
    #g = GeneratorLemer(seed)
    #g = GeneratorL20(seed)
    #g = GeneratorL89(seed)
    #g = GeneratorGeffe(seed)
    g = GeneratorBBS(seed)
    current_value = 0
    frequencies = [0] * 256
    i = 0
    while i < 2**20 - 1:
        #print "Generator %s says 0x%X!"%(g.get_name(), g.get_byte())
        current_value = g.get_byte()
        frequencies[current_value] += 1
        #print current_value,
        i += 1

    for f in frequencies:
        print int((2**20-1.0)/256 - f),
