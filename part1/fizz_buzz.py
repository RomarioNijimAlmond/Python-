def fizz_buzz(num):
    if num % 5 == 0 and num % 3 == 0:
        print("fizzbuzz")
    elif num % 5 == 0:
        print("buzz")
    elif num % 3 == 0:
        print("fizz")


print(fizz_buzz(15))
print(fizz_buzz(25))
print(fizz_buzz(3)) 
