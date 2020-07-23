#The sum of the squares of the first ten natural numbers is,

#12+22+...+102=385
#The square of the sum of the first ten natural numbers is,

#(1+2+...+10)2=552=3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640.

#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum


#sum for both
#difference

def sumSqure():
    sumOfsquares = 0
    for i in range( 1, 101 ):
        sumOfsquares += i*i  
    print(sumOfsquares)
    return sumOfsquares
    

def squreOfsum():
    total = 0
    for i in range(1, 101):
        total += i

    totalSqure = total*total
    print(totalSqure)
    return totalSqure
   


def substraction():
    result = squreOfsum() - sumSqure()
    print(result)





#sumSqure()
#squreOfsum()

substraction()