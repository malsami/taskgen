"""
Prints out `hey: Hello!`
"""

def Value(arg1):
	return {
    	"pkg" : "hey",
    	"config" : {
            "arg1" : arg1
        }
	}

def Variants(variants):
    return Value(range(1,variants))
