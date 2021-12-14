# Author JRI 12/14/21

import random

number = random.randint(1, 9999)
if number < 10:
    number = "0" + "0" + "0" + number
elif number < 100:
    number = "0" + "0" + number
elif number < 1000:
    number = "0" + number


x = input("Name a clone? ")
while x == "y":
    print("New clone trooper name: CT-{0}".format(number))
    if x == "n":
        break
    