#Problem 53: Combinatoric selections

def fac_it(n):
    prod = 1
    for i in range(2,n+1):
        prod *= i
    return prod

def binomial_coefficient(n,k):
    return fac_it(n)/(fac_it(k)*(fac_it(n-k)))

counter = 0
for i in range(23,101):         #n
    for j in range(3,100):          #r
        if binomial_coefficient(i,j) > 1000000:
            counter += 1

print(counter)