import logging
logging.basicConfig(level=logging.DEBUG)

#naking fibonacci series
fiboNumber = [1,2]

while fiboNumber[-1] < 4000000:
    fiboNumber.append(fiboNumber[-1] + fiboNumber[-2])

del fiboNumber[-1]
logging.debug(fiboNumber)

#getting the even numbers
evenFibNumber = []
for i in fiboNumber:
    if i%2 == 0:
        evenFibNumber.append(i)

logging.debug(evenFibNumber)

#sum of those even number
print(sum(evenFibNumber))

total = 0
for numbers in evenFibNumber:
    total += numbers

print(total)