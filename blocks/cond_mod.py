import random

"""
Fulfills the condition, which terminates the program without counting.
`cond_mod` immediately, if `args1` is multiple of 2.
"""
def Value(arg1):
    return {
        "pkg" : "cond_mod",
        "config" : {
            "arg1" : arg1
        }
    }


"""
Random argument `arg1`, `n` is the maximum value for `arg1`.
"""
def Random(n):
    return Value(random.randint(1, n))

"""
The break condition is 2.
"""
def Break():
    return Value(2)

"""
The break condition is chosen randomly.
"""
def RandomBreak():
    return Value(random.randint(0, 1000000)*2)

"""
Creates variants of looping.
"""
def Variants(variants):
    return Value(range(1,variants))
