#higher order functions
# a function that takes one or more functions as arguments 
#or a function that returns a function as its result

def func_builder(x):
    return lambda num : num + x


numbers = [3,7,12,18,20,21]

# map is a functio that takes a function as its first param and the second param is its data
sqaured_nums = map(lambda num : num * num, numbers)
print(list(sqaured_nums))

#another built it python function - filter

def find_odd_nums(num):
    return num % 2 != 0

nums = [1,2,3,4,5,6,7]

odd = filter(find_odd_nums, nums)

print(list(odd))

###################################
# another higher order function

from functools import reduce

lam = lambda acc, curr : acc + curr

numbers = [1,2,3,4,5,12]

total = reduce(lam, numbers)

print(total)
