"""
Prints out `hey: Hello!`
"""

def Value(arg1):
	return {
    	"pkg" : "namaste",
    	"quota" : "10M",
    	"config" : {
            "arg1" : arg1
        }
	}

def Variants(variants):
    return Value(range(1,variants))
