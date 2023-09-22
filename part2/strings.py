# string data type

# literal assignment

first_name = "Dave"
last_name = "Wilson"

print(type(first_name))
print(type(first_name) == str)
print(isinstance(first_name, str))

# constructor function
pizza = str("pepperoni")

print(type(pizza))
print(type(pizza) == str)
print(isinstance(pizza, str))

# concatenation
fullname = f"{first_name} {last_name}"
print(fullname)

# casting number to a string

num = str(1980)
print(type(num))

# cast string to number
st = int("42")
print(type(st))

# multi line

multiline = '''

hello  
            how 
                        are

                                you?
'''

print(multiline)


# single quotes for escaping special characters

sn = 'I\'m back at work'
print(sn)


# string methods - functions that are called on the string class

print(first_name)
print(first_name.lower())
print(first_name.upper())


# center

center = "MENU"
print(center.center(20, "="))


# string index values

print(first_name[0])
print(first_name[1])
print(first_name[2])
print(first_name[3])

print("-----------")

char = "Dave"
for i in char:
    print(i)

print(char.startswith("D"))
print(char.endswith("e"))
