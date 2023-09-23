# function calls itself - recursive call 

def add_one(num):
    if num >= 9:
        return num + 1
    total = num + 1
    print(total)
    return add_one(total)


new_total = add_one(0)
print(new_total)

#-------------------------------------------------------------------

def prevent_same_consicutive_chars(char:str): #a a b b a => aba 
    if len(char) <=1:
        return char
    charac = char[0]
    if charac == char[1]:
        return prevent_same_consicutive_chars(str(char[1:]))
    else:
        return charac[0] + prevent_same_consicutive_chars(str(char[1:]))
    
    

print(prevent_same_consicutive_chars("Hello Bookkeeper"))

    