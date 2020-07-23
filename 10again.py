import sympy

a=1
b=2000000
print(list(sympy.primerange(a,b)))


c=sum(list(sympy.primerange(a,b)))
print(c)