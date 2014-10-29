from number import n
from functions import *
from random import randint
from sys import argv

def print_usage(programname):
    print """
USAGE:
{programname} -1     - Get t and y = (t*t) mod n
{programname} -2 t z - Try to crack
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
    else:
        print_usage(argv[0])
        exit(1)

