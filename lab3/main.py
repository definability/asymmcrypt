from number import n
from functions import *
from random import randint
from sys import argv

def print_usage(programname):
    print """
USAGE:
{programname} --sqr t         - Get y = (t*t) mod n
{programname} --gcd-crack t z - Get p = gcd(t+z, n)
""".format(programname = programname)

if __name__ == '__main__':
    if len(argv) < 2 or argv[1] == '--h':
        print_usage(argv[0])
        if len(argv) < 2:
            exit(1)
        else:
            exit(0)
    elif argv[1] == '-1':
        t = randint(2,n)
        print "t = %d"%t
        print "t*t = %d"%get_t2(t)
    elif argv[1] == '-2':
        t, z = int(argv[2]), int(argv[3])
        print "z = %d"%z
        if t == z:
            print "t is equal to z"
            exit(1)
        print "pq = %d"%get_pq(t, z)
        p = get_pq(t, z)
        if p < 2 or n%p != 0 or n == p:
            print 0
            exit(1)
        else:
            print "CRACKED SUCCESSFULLY!"
            q = n/p
            print "p = %d"%p
            print "q = %d"%q
            exit(0)
    elif argv[1] == '--generate':
        print randint(2,n)
    elif argv[1] == '--sqr':
        t = int(argv[2])
        print get_t2(t)
        exit(0)
    elif argv[1] == '--gcd-crack':
        t, z = int(argv[2]), int(argv[3])
        if t == z:
            print 0
            exit(1)
        else:
            print get_pq(t, z)
            exit(0)
    elif argv[1] == '--check-p-q':
        p = int(argv[2])
        if p < 2 or n%p != 0 or n == p:
            print 0
            exit(1)
        else:
            print "CRACKED SUCCESSFULLY!"
            q = n/p
            print "p = %d"%p
            print "q = %d"%q
            exit(0)
