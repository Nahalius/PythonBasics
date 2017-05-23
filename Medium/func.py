x = "Texto za printirane"
def func(y):
    print(y)
func(x)



def func2(*args): #unpack list
    print(args)
values = (1,3,5,8)
func2(values)
func2(*values)

def func3(**args2): #upack dictionary
    print(args2)
func3(a =1, b = 5)
