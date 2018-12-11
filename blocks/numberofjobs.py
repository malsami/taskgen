import random

def Value(numberofjobs=1):
    return {
        "numberofjobs" : numberofjobs
    }

def Variants():
    return Value(range(1,20))

def Random():
    return Value(random.randint(1, 20))

def HighRandom():
    return Value(random.randint(1, 5))

def MediumRandom():
    return Value(random.randint(5, 10))

def LowRandom():
    return Value(random.randint(10, 20))

