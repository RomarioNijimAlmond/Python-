users = ["John", "Dave", "Sara"]
data = ["Dave", 42, True]
empty_list = []

print("Dave" in users)
print("noname" in users)

print(users[0])
print(users[-1])

print(users.index("John"))
print(users[0:2])
print(users[1:])
print(len(users))

for i in range(len(users)):
    print(f" at index {i}: {users[i]}")

users.append("James")
print(users)
users.pop()
print(users)

users.insert(0, "Jones")
print(users)
users.pop(0)
print(users)

users = users + ["json", "richard"]
print(users)
users.extend(["Robert", "Jimmy"])
print(users)

# users.extend(data)
# print(users)

users[1:3] = ["Johnny", "JPJ"]
print(users)

users.remove("Johnny")
print(users)

del users[1]
print(users)

# del data
data.clear()
print(data)

users.sort()
print(users)

users.append("dave")
users.sort(key=str.lower)
print(users)


num_list = [4, 42, 78, 1, 5]
num_list.reverse()
print(num_list)


# num_list.sort(reverse=True)
# print(num_list)

print(sorted(num_list, reverse=True))
print(num_list)
print("")

# copy a list

nums_copy = num_list.copy()
print(nums_copy)
my_nums = list(num_list)
print(my_nums)
my_copy = num_list[:]
print(my_copy)

my_copy.sort()
print(my_copy)
