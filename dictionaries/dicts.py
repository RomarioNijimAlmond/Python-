bands = {
    "vocals": "Plant",
    "guitar": "Page",
}


print(bands)


# constructor dict

users = dict(name="John", lastname="Doe")
print(users)

print(type(bands))
print(type(users))

# access properties
print(bands["guitar"])
print(users["name"])

print("")

print(bands.get("guitar"))
print(users.get("lastname"))

# list all keys
print(bands.keys())
print(users.keys())
print("")

# list all values
print(bands.values())
print(users.values())
print("")

# list of key-value pairs as tuples
print(bands.items())
print(users.items())
print("")

print("name" in users)
print("Doe" in bands)
print("John" in users["name"])
print("s" in users["name"])

# change values in dict

users["name"] = "Johnny"
print(users)

users.update({"bass": "JPJ"})
print(users)

users["DJ"] = "K"
print(users)

# remove items

print(users.pop("bass"))
print(users)

print(users.popitem())
print(users)

# delete and clear

del bands["vocals"]
print(bands)

bands.clear()
print(bands)

# del bands
# print(bands)


# copy dictionaries

# bands = users  # creates a reference
# print(bands)

# bands["name"] = "newwww"
# print(users)
# print(bands)

user2 = users.copy()

user2["name"] = "yooo"

print(users)
print(user2)

# another way to copy via constructory dict

user3 = dict(users)

user3["name"] = "Mark"
user3["lastname"] = "json"

print(users)
print(user3)

# nested dictionaries

member1 = {
    "name": "Plant",
    "instrument": "vocals"
}

member2 = {
    "name": "Page",
    "instrument": "guitar"
}

di = {
    "member1": member1,
    "member2": member2,
}

print(di)

print(di["member1"]["name"])
print(di["member2"]["instrument"])
