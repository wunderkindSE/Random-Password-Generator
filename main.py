import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbol = "[]\;/!@#$%^&*()-"

all = lower + upper + number + symbol
length = 8
password = "".join(random.sample(all,length))
print("The password you generated is :",password)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
