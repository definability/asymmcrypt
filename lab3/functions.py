from number import n
from fractions import gcd
from sys import argv

def get_pq(t, z):
    return gcd(t+z, n)

def get_t2(t):
    return (t*t) % n
