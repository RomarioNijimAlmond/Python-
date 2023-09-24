hello_world = "hello world"
print(hello_world)

# comments hash tag


def countNumber(num1: int, num2: int):
    if num1 == num2:
        return 2 * (num1 + num2)
    else:
        return num1 + num2


print(countNumber(2, 2))
print(countNumber(1, 2))

name = "john"

print(name.capitalize())
print(name.upper())


from faker import Faker 

fake = Faker()

fake_name = fake.name()
print(fake_name)