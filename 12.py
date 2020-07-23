    
import sys

def isTriangle(limit):
    '''
    first we need to generate the triangle number
    1
    1+2=3
    3+3=6
    6+4=10
    10+5=15  
    '''
    number = 0
    for i in range(1,limit):
        number += i
        #print("The triangle numbers", number)
        isDivisor(number)

def isDivisor(number):
    list=[]
    div=[]
    for i in range (1,number+1):
        if number%i == 0:
            #print(i)
            list.append(i)
            if len(list) == 500:
                div.append(number)
                if len(div) == 1:
                    print("The first number: ",number)
                    #print(div)
                    sys.exit()

           
    
                
                
          #      SystemExit 
          #      print(number,": " ,list)
          #  elif len(list) > 5:
          #      pass
          #  elif len(list) < 5:
          #      SystemExit

        




def generateNumbers():
    number = 1
    while True:
        isTriangle(number)
        number+=1


generateNumbers()