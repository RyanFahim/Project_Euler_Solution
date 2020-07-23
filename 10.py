def main():
    number_of_prime_to_find_upto = 20
    x = 2

    listOfprime = [2]

    while(listOfprime[0] <= number_of_prime_to_find_upto):
        if all(x % prime for prime in listOfprime):
            listOfprime.append(x)
        x += 1

    print(listOfprime)

main()