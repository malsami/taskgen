import random

def Value(offset):
    return {
        "offset" : offset
    }

def Variants():
    return Value(range(1000,20000,1000))

def Random():
    return Value(random.randint(1000, 20000))

def HighRandom():
    return Value(random.randint(10000, 20000))

def MediumRandom():
    return Value(random.randint(5000, 10000))

def LowRandom():
    return Value(random.randint(1000, 5000))
