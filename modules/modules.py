import math
import sys
import random as rdm # alias
from enum import Enum # specific module from a module
import my_module
from rps7 import rock_paper_scissors

class My_enum(Enum):
    YES = 1
    NO = 0

print(math.pi)

rdm.choice("123")

for item in dir(rdm):
    print(item)

# print(dir(rdm))

my_module.func()


print(my_module.bird)
print(my_module.capital)
print(my_module.__name__)


rock_paper_scissors()

# sys.exit()

