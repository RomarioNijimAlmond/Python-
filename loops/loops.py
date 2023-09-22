list_item = [1, 2, 3, 4, 5, 6, 7]
for i in range(len(list_item)):
    print(f"{i} => {list_item[i]}")
    # -------------------------------

for num in list_item:
    print(num)
    # -------------------------------

value = 1
while value <= 10:
    print(value)
    value += 1

    # -------------------------------

value = 1
while value <= 10:
    value += 1
    if value == 5:
        continue
    print(value)
    # -------------------------------

word = "mississippi"

for char in "mississippi":
    print(char)
    # -------------------------------

names = ["Dave", "John", "Sara"]

for name in names:
    if name == "John":
        continue
    print(name)
    # -------------------------------

for x in range(1, 11):
    print(x)

print("")

for x in range(4):
    print(x)

    print("")

# incrementation

# increment by 2 (increment by one is the default)
for x in range(0, 12, 2):
    print(x)
else:
    print("that\'s over")

    print("")
# -------------------------------

# nested loops
names = ["Dave", "Sara", "John"]
actions = ["codes", "eats", "sleeps"]

for name in names:
    for action in actions:
        print(f"{name}: {action}")


# Dave: codes
# Dave: eats
# Dave: sleeps
# Sara: codes
# Sara: eats
# Sara: sleeps
# John: codes
# John: eats
# John: sleeps
