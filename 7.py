import math


def primeNumber(number):
    result =[]
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                #print("Not a prime number")
                #print(i,"times",number//i,"is",number)
                break

        else:
            print(number, " is a prime number")
            result.append(number)
            
            
            while 1:
                if int(len(result)) == 6:
                    print(result)
                break
        

    else:
        pass
        #print("not a prime number")



primeNumber(10)
