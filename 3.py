
from math import floor, sqrt

def factor(num):
    result = []

    if num == 2:
        result.append(2)
        return result

    for i in range(3, floor(sqrt(num)) ):
        if num % i == 0:
            if len(factor(i)) == 0:
                result.append(i)
    return result
    




#print(factor(10))
print(factor(600851475143))
print(factor(600851475143)[-1])