# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
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
