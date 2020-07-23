from math import ceil,floor


#is palindrome
def isPalindrome(num):
    s = str(num)

    s1 = s[0: int(len(s)/2)]
   
    s2 = s[int(ceil(len(s)/2.0) ):]
   
   
    return s1 == s2[::-1]
    return s1, s2

#print(isPalindrome(90109))
#lagrgest palindrome
laggest = 0
for x in range(100, 1000):
    for y in range(100,1000):
        z = x*y
       if isPalindrome(z) and z > laggest:
             laggest= z
print(laggest)


            