#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import math

#for i in range(1,11):
    #   print(i ,": ",2520/i)

#first find that is the number divisable from 1 to 20
def isDivisableFrom1to20(number):
    for tryNumber in range(1,21):
        if number % tryNumber != 0:
            return False
    return True

number = 1
while True: # an infinite loop
    if isDivisableFrom1to20(number):
        break                         #if one is found,break
    number += 1 #increment the number

print(number)

