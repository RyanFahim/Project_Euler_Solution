
import math

def main():
    a= 2**1000

    arr = []
    nstr = str(a)
    print(nstr)

    for i in nstr:
        arr.append(int(i))
    print(sum(arr))

main()
    
