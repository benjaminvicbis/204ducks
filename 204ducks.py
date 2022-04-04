#!/usr/bin/env python3

from math import *
from sys import *

def get_help():
    print("USAGE")
    print("\t./204ducks a")
    print("")
    print("DESCRIPTION")
    print("\ta\tconstant")
    exit(0)

def calc_prob(a, t, version = 0):
    if (version == 0):
        return -a * exp(-t) - (4 - 3 * a) / 2 * exp(-2 * t) - (2 * a - 4) / 4 * exp(-4 * t)
    else:
        return a * exp(-t) + (4 - 3 * a) * exp(-2 * t) + (2 * a - 4) * exp(-4 * t)

def get_ART(a):
    r = 0.0 ; t = 0.0
    while t < 10:
        r += calc_prob(a, t, 1) * t / 1000
        t += 0.001
    return r

def get_SD(a, art):
    r = 0.0 ; t = 0.0
    while t < 100:
        r += pow(t - art, 2) * calc_prob(a, t, 1) / 1000
        t += 0.001
    return sqrt(r)

def get_TD(a, x):
    t = 0.0
    while t < 1000:
        if calc_prob(a, t / 60) - calc_prob(a, 0) >= x:
            return t
        t += 0.002
    raise

argv.pop(0)

try:
    if (len(argv) != 1):
        raise

    if (argv[0] == '-h'):
        get_help()

    a = float(argv[0])

    if (a < 0 or a > 2.5):
        raise

    art = get_ART(a)
    sd = get_SD(a, art)
    td1 = get_TD(a, 0.5)
    td2 = get_TD(a, 0.99)
    dp1 = (calc_prob(a, 1) - calc_prob(a, 0)) * 100
    dp2 = (calc_prob(a, 2) - calc_prob(a, 0)) * 100

    print("Average return time: %dm " % int(art) + "%ds" % ceil((art - int(art)) * 60))
    print("Standard deviation: %.3f" % sd)
    print("Time after which 50%% of the ducks are back: %dm %d%ds" % (td1 / 60, td1 % 60 / 10, td1 % 10))
    print("Time after which 99%% of the ducks are back: %dm %d%ds" % (td2 / 60, td2 % 60 / 10, td2 % 10))
    print("Percentage of ducks back after 1 minute: %.1f%%" % dp1)
    print("Percentage of ducks back after 2 minutes: %.1f%%" % dp2)

except:
    exit(84)
