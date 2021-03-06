"""
Using sieve of Erathosthenes for calculating primes.
"""
import random

def Value(arg1):
    return {
        "pkg" : "tumatmul",
        "config" : {
            "arg1" : arg1
        }
    }

"""
Random argument `arg1`, `n` is the maximum value for `arg1`.
"""
def Random(n):
    return Value(random.randint(1, n))




def Variants(variants):
    return Value(range(1,variants))
