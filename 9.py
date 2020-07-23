#find all the numbers

def main():
    
    totalSum = 1000

    for c in range(totalSum):
        for b in range(c):
            for a in range(b):
                if a+b+c == totalSum:
                    if pythagorean(a,b,c):
                        print(a*b*c)

    


def pythagorean(a, b, c):
    if a**2 + b**2 == c**2:
        return True        
    else:
        return False


main()