def main():
    number_of_prime_to_find = 10001
    x = 2

    listOfprime = []

    while(len(listOfprime) < number_of_prime_to_find):
        if all(x % prime for prime in listOfprime):
            listOfprime.append(x)
        x += 1

    print(listOfprime[-1])

main()