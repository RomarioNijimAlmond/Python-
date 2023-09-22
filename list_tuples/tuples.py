mytuple = tuple(('Dave', 42, True))
my_type = (1, 2, 4, 2, 5)

print(mytuple)
print(my_type)

print(type(mytuple))
print(type(my_type))


new_list = list(mytuple)
new_list.append("neil")
print(new_list)

new_tuple = tuple(new_list)
print(new_tuple)

print(my_type.count(2))
