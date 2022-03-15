#Problem 10: Summation of primes

def eratosthenes(n):
    if n <2:
        return []
    a = [0,0] + (n-1)*[1]
    i = 2
    while i*i <= n:
        if a[i] == 1:
            for j in range(i*i, n+1, i):
                a[j] = 0
        i += 1
    return [p for p in range(n+1) if a[p] == 1]

print(sum(eratosthenes(2000000)))