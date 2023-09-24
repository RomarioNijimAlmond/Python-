# try:
#     print(x)
# except:
#     raise Exception("x is not defined - it is used before initialized")
# else:
#     print("no errors")

# try:
#     print(y)
# except:
#     print("y is not defined")


# try:
#     print(x)
# except Exception as error:
#     print(f"{error}: x is used before initialized")
# else:
#     print("no errors")
# finally:
#     print("im going to print with or without an error")


num = 11
try:
    if not type(num) is str:
        raise TypeError("num is not a string")
except Exception as error:
    print(f"{error}")


# custom expetions - class that inherits from the Exception class

class JustNotError(Exception):
    pass


num = 11
try:
    if not type(num) is str:
        raise JustNotError("not error")
except Exception as error:
    print(f"{error}")
