## Завдання 1
from math import log, sin, cos, log10, factorial, prod
a = 6
b = 9
h = 0.2
x = a
while x <= b:
    if x<7:
        print(log10(x*log(x)+sin(x)))
    elif x>=7 and x<8:
        print(log((sin(x)+4),3))
    else:
        print(1/(16+1/cos(x)))
    x += h


## Завдання 2
a = 0
b = 0.5
h = 0.05
d = 0.001
m = 9
x = a 
while x<=b:
    n = 1
    sum_value = 1
    term = (-1)**n*prod([m+i for i in range(n)]) * (x**n)/factorial(n)
    while abs(term) > d:
        sum_value += term
        n += 1
        term = ((-1)**n*prod([m+i for i in range(n)]) * (x**n)/factorial(n))
    print("x = ", round(x,4), "f(x) =", sum_value)
    x+=h
    x = round(x,2)
    print(x)
    