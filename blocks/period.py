import random

def Value(period):
    return {
        "period" : period
    }

def Variants():
    return Value(range(20))

def Random():
    return Value(random.randint(1000, 20000))

def HighRandom():
    return Value(random.randint(1000, 3000))

def MediumRandom():
    return Value(random.randint(4000, 10000))

def LowRandom():
    return Value(random.randint(10000, 20000))

