#Problem7: Find 10001st prime
import scipy.integrate as integrate
from math import log

result = integrate.quad(lambda x: 1/log(x), 2, 150000)
print(result)           #for approximation ==> 10000 prime number is less than 150000

def eratosthenes(n):
    if n < 2:
        return []
    A = [0,0] + (n-1)*[1]
    i = 2
    while i*i <= n:
        if A[i] == 1:
            for j in range(i*i, n+1,i):
                A[j] = 0
        i = i + 1
    return [p for p in range(n+1) if A[p] == 1]

print(eratosthenes(150000)[10000])
