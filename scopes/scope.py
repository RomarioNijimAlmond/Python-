#global scope

name = "Dave"
count = 1

def greeting(firstname):
    color = "blue" #local scope
    global count # refers to the global avriable with the global keyword since and it was not created in the local scope
    count += 1
    print(count)
    print(color)
    print(name)
    print(firstname)

greeting("John")
print("")


def another_func(name):
    greeting(name)

another_func("Sara")

# another_one() it is in the func inside func scope

def func_inside_func():
    color = "sky blue!" # lexical scope of the another one function
    def another_one():
        print(" define function inside another function")
        print(color)
    another_one()

func_inside_func()
