#CRUD files
import os

# r = Read
# a = Append
# w = Write
# x = Create

f = open("names.txt")
print(f.read())
f.close()


f = open("names.txt", "a")
f.write("Json")
f.close()


f = open("names.txt", "r")
print(f.read())
f.close()

#wite (overwite)
f = open("context.txt", "w")
f.write("helooo")
f.close()


f = open("context.txt", "r")
print(f.read())
f.close()

#delete file

#avoid an error if it dosen't exist

if os.path.exists("names.txt"):
    os.remove("names.txt")
else:
    print("the file you wish to delete does not exist!")