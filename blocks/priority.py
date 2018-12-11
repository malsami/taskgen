import random

# kernel: 256 priorties
    # genode: 128 priorities
def Value(priority):
    return {            
        "priority" : priority
    }

def Variants():
    return Value(range(0, 127))

def Random():
    return Value(random.randint(1, 127))

def HighRandom():
    return Value(random.randint(0, 42))

def MediumRandom():
    return Value(random.randint(42, 84))

def LowRandom():
    return Value(random.randint(84, 127))



        
