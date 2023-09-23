#closure is a function having access to the scope of it's parent function or parent scope when the parent funciton has already closed/returned

# another_one() it is in the func inside func scope

# def parent_func():
#     color = "sky blue!" # lexical scope of the another one function
#     def nested_func():
#         print(" define function inside another function")
#         print(color)
#     return nested_func()

# parent_func()


def parent_function(person:str, coins:int):
    # coins = 3 avoid global variables when possible 
    def play_game():
        nonlocal coins
        coins -= 1
        if coins > 1:
            print(f"\n {person} has {str(coins)} coins left")
        elif coins == 1:
            print(f"\n {person} has {str(coins)} coin left")
        else:
            print(f"\n {person} is out of coins")
    return play_game



tommy = parent_function("Tommy", 3)
jenny = parent_function("Jenny", 5)

tommy()
tommy()
tommy()
jenny()
jenny()