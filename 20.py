import math

def main(number):
    fact = math.factorial(number)
    #print(fact)

    making_fact_str = str(fact)
    #print(making_fact_str)

    list_of_fact=[]

    for i in making_fact_str:
        list_of_fact.append(int(i))
    print(sum(list_of_fact))



main(100) 