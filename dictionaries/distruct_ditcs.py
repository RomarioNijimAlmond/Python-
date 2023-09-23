obj = {
    "bread": 1,
    "protein": 2,
    "eggs": 3,
}

one, two, three = obj
print(one)
print(two)
print(three)

for key, value in obj.items():
    print(f"the key={key} and quantity => {value}")
