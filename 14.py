#collatz problem
#it takes 36.81712460517883s to produce the results
import sys, time

def collatz(number):

    if number%2 == 0:
        number = number/2
       
        #print(" ->", number)

    elif number%2!= 0:
        number = (3*number) + 1
        #collatz(number)
     
        #print(" ->", number)
    number = int(number)
    return(number)
    

    

def main():
    start_time = time.time()
    current_longest_chain = 0
    number_that_produced_chain = 0
    x =  1
    collatz_up_to = 1000000

    while( x < collatz_up_to):
        current_number = x
        current_chain = 1

        while (current_number != 1):
            current_number = collatz(current_number)
            current_chain += 1
        if current_chain > current_longest_chain:
            current_longest_chain = current_chain
            number_that_produced_chain = x
        #print(x, current_chain)
        current_chain = 1
        x += 1
    print(number_that_produced_chain, current_longest_chain)
    print(time.time() - start_time)


main()






