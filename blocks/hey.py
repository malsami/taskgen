"""
Prints out `hey: Hello!`
"""

def Value(arg1):
	return {
    	"pkg" : "hey",
    	"quota" : "10M",
    	"config" : {
            "arg1" : arg1
        }
	}

def Variants(variants):
    return Value(range(1,variants))
