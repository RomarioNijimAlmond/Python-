
multiple = lambda num : num * num
print(multiple(2))

add = lambda num : num + num

def addTwo(num): 
    return num + 2

print(addTwo(5))

print(add(2))

# similar to js arrow function = 
# const addTwoNums = (a,b) => a + b

add_two_nums = lambda a,b : a + b
print(add_two_nums(5,6))

def func_builder(param):
    return lambda num : num + param

add_ten = func_builder(10)
add_twenty = func_builder(20)

print(add_ten(10))
print(add_twenty(30))

print(add_ten(1))
print(add_twenty(7))