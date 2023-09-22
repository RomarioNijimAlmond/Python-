def hello_function():
    print("this is a function")


hello_function()

# -----------------------


def sum(num1=0, num2=0):
    if (type(num1) is not int and type(num2) is not int):
        raise ValueError("the argument that was typed is not of type int")
    if num1 == num2:
        return 2 * (num1 + num2)
    else:
        return num1 + num2


total = sum(2, 2)
total2 = sum(1, 2)
print(total)
print(total2)
# print(sum("a", "f"))


def greet(name=None):
    if name is None:
        print("default")
    else:
        print(f"Hello, {name}!")


greet()
greet("Alice")

print(sum())

# --------------------

# multiple args


def multi_args(*args):
    print(args)
    print(type(args))


multi_args()

multi_args("Dave", "John", "Sara")


def multi_named(**kwargs):
    print(kwargs)
    print(type(kwargs))


multi_named()

multi_named(first="Dave", second="John", third="Sara")
