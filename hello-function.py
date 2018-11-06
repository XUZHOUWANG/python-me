#help()
def hello():
    print("hello wolrd")

def useHello() :
    return hello

#print(useHello())
#return tuple

def make_function(parity) :
    if (parity == 'even'):
        print('even')
        matches_parity = lambda x: x%2 == 2
    elif parity == 'odd':
        print('odd')
        matches_parity = lambda x: x%2 !=2
    else:
        raise AttributeError("Unknown Parity: " + parity)

make_function("even")
