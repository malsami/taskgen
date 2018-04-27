import random

def Value(criticaltime):
    return {
        "criticaltime" : criticaltime
    }

def Variants():
    return Value([x*1000 for x in range(20)])

def Random():
    return Value(1000*random.randint(20))

def HighRandom():
    return Value(1000*random.randint(14, 20))

def MediumRandom():
    return Value(1000*random.randint(7, 14))

def LowRandom():
    return Value(1000*random.randint(1, 7))

