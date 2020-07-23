
def find_divisor(number):

    potential_divisor = 1
    list_of_divisor = []

    while potential_divisor < number:
        if number % potential_divisor == 0:
            list_of_divisor.append(potential_divisor)
        potential_divisor += 1
    return(list_of_divisor)


#print(find_divisor(10))
def find_amicable():

    numbers_up_to = 10000
    list_of_amicable_number = []
    number = 1
    while number < numbers_up_to:
        #find the divisor of number
        divisor_of_number = find_divisor(number)
        #sum the divisor number
        sum_of_number = sum(divisor_of_number)
        #find the divisor of new number
        divisor_of_new_number = find_divisor(sum_of_number)
        #find the sum of new number
        sum_of_new_number = sum(divisor_of_new_number)
        #check if the number is same as the sum of divisor of numbers and then append
        if number == sum_of_new_number and number < numbers_up_to and sum_of_number <numbers_up_to and number > sum_of_number: # 10[1,2,5] -> 10>8
            list_of_amicable_number.append(number)
            list_of_amicable_number.append(sum_of_number)
        number += 1

    print(sum(list_of_amicable_number))

find_amicable()