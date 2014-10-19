import random
from fractions import gcd


BIT_MASK = 1
BYTE_MASK = 0xFF

BBS_P = 0x5ABA02CC8F5C8E71DD2FE0F870C2CDDB77B4EC7
BBS_Q = 0x5ABA02CC8F5C8E71DD2FE0F870C2CDDB77B4EC7

LEMER_M = 2**32
LEMER_A = 2**16 + 1
LEMER_C = 119

L20_MASK = (1 << 19) | (1 << 8) | (1 << 4) | (1 << 2)
L89_MASK = (1 << 37) | (1 << 88)


def calculate_bits(number):
    '''
    Got from https://wiki.python.org/moin/BitManipulation
    '''
    counter = 0
    while number:
        number &= number - 1
        counter += 1
    return counter


class Generator(object):
    #seed = None
    def __init__(self, name, seed):
        self.name = name
        self.seed = seed
        self.plant_a_seed(self.seed)
    def get_name(self):
        return self.name

    def plant_a_seed(self, seed):
        self.seed = seed

    def get_byte(self):
        return 0


class GeneratorDefault(Generator):
    def __init__(self, seed):
        super(GeneratorDefault, self).__init__('Default', seed)

    def plant_a_seed(self, seed):
        super(GeneratorDefault, self).plant_a_seed(seed)
        random.seed(self.seed)

    def get_byte(self):
        return random.getrandbits(8)


class GeneratorLemer(Generator):
    FIRST_BLOCK = 0
    LAST_BLOCK = 3
    BITS_IN_BLOCK = 8
    BLOCK_MASK = BYTE_MASK
    current_block = FIRST_BLOCK
    current_x = 1
    a = 0
    m = 0
    c = 0

    def __init__(self,seed):
        super(GeneratorLemer, self).__init__('Lemer', seed)

    def plant_a_seed(self, seed):
        super(GeneratorLemer, self).plant_a_seed(seed)

        self.x_n = self.seed['x']
        self.a = self.seed['a']
        self.m = self.seed['m']
        self.c = self.seed['c']
        '''
        self.current_block = self.FIRST_BLOCK
        for i in range(self.FIRST_BLOCK, self.LAST_BLOCK):
            self.get_byte()
        '''

    def get_byte(self):
        '''
        # This stuff returned every byte of 32-bit register
        if self.current_block <= self.LAST_BLOCK:
            current_offset = self.BITS_IN_BLOCK*self.current_block
            current_mask = self.BLOCK_MASK << current_offset
            current_value = (self.x_n & current_mask) >> current_offset
            self.current_block += 1
            return current_value
        else:
            self.x_n = self.seed['a'] * self.x_n + self.seed['c']
            self.x_n %= self.seed['m']
            self.current_block = self.FIRST_BLOCK
            return self.get_byte()
        '''
        # And this is not
        self.x_n = (self.a * self.x_n + self.c) % self.m 
        return self.x_n & self.BLOCK_MASK


class GeneratorLFSR(Generator):
    BITS_IN_BLOCK = 8
    BLOCK_MASK = BYTE_MASK
    mask = 0
    current_x = 1
    register_size = 1
    register_mask = 0

    def __init__(self,name,seed):
        super(GeneratorLFSR, self).__init__('LFSR', seed)

    def plant_a_seed(self, seed):
        super(GeneratorLFSR, self).plant_a_seed(seed)
        self.current_x = seed['x']
        self.mask = seed['mask']
        self.register_size = seed['register_size']
        for i in range(self.register_size+1):
            self.register_mask <<= 1
            self.register_mask |= 1
        for i in range(self.register_size):
            self.get_byte()

    def get_bit(self):

            current_bit = calculate_bits(self.current_x & self.mask) & BIT_MASK

            self.current_x <<= 1
            self.current_x |= current_bit
            self.current_x &= self.register_mask

            return current_bit & BIT_MASK

    def get_byte(self):
        result = 0
        for i in range(self.BITS_IN_BLOCK):
            current_bit = self.get_bit()
            result <<= 1
            result |= current_bit

        return result & BYTE_MASK


class GeneratorL20(GeneratorLFSR):
    def __init__(self,seed):
        current_seed = {'x': seed, 'mask': L20_MASK, 'register_size': 20}
        super(GeneratorL20, self).__init__('L20', current_seed)


class GeneratorL89(GeneratorLFSR):
    def __init__(self,seed):
        current_seed = {'x': seed, 'mask': L89_MASK, 'register_size': 89}
        super(GeneratorL89, self).__init__('L89', current_seed)


class GeneratorGeffe(Generator):
    LFSRs = list()

    def __init__(self,seed):
        super(GeneratorGeffe, self).__init__('Geffee', seed)

    def plant_a_seed(self, seed):
        super(GeneratorGeffe, self).plant_a_seed(seed)
        self.LFSRs = seed['LFSRs']

    def get_bit(self):
        return (lambda x1,x2,x3: (x1 & x2) ^ (~x1 & x3))(
                self.LFSRs[0].get_bit(), self.LFSRs[1].get_bit(),
                self.LFSRs[2].get_bit()) & BIT_MASK

    def get_byte(self):
        result = 0
        for i in range(8):
            result <<= 1
            result |= self.get_bit()
        return result & BYTE_MASK

class GeneratorBBS(Generator):
    BYTE_MASK = 0xFF
    n = 1
    current_r = 2
    def __init__(self,seed):
        super(GeneratorBBS, self).__init__('BBS', seed)

    def plant_a_seed(self,seed):
        super(GeneratorBBS, self).plant_a_seed(seed)
        self.n = self.seed['p'] * self.seed['q']
        self.current_r = self.seed['r']

    def get_block(self, block_mask=BIT_MASK):
        result = self.current_r
        self.current_r = (self.current_r ** 2) % self.n
        return result & block_mask

    def get_bit(self):
        return self.get_block(BIT_MASK)

    def get_byte(self):
        return self.get_block(BYTE_MASK)
