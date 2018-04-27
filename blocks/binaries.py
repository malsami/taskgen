import random
from taskgen.blocks import *

"""
Returns a list of all binary and randomized values.
"""
def Random(par1_max):
    return [
        hey.Value(parl_max),
        cond_mod.Random(par1_max),
        cond_42.Random(par1_max),
        namaste.Value(parl_max),
        pi.Random(par1_max),
        linpack.Random(par1_max),
        tumatmul.Random(par1_max),
    ]

"""
Returns a list of size `size` with random tasks.
"""
def RandomList(size, par1_max):
    return [random.choice(Random(par1_max)) for x in range(size)]
