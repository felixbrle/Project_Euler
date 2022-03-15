#Problem 35: Circular primes

from itertools import permutations

#All what you need for prime tasks:

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

def k_teWurzel_n(n,k):          #Algorithm for k-th root of n in natural numbers
    L, R = 1, n
    while R - L >= 2:
        M = (L+R)//2
        if M**k <= n:
            L = M
        else:
            R = M
    return L

def is_prime(n):            #Prime tester
    for i in range(2,k_teWurzel_n(n,2)+1):
        if n % i == 0:
            return False
    return True

candidates = eratosthenes(1000000)

def _digits_rotations(digits):          #digit rotation, NOT asked after permutations
    return [int(digits[i:] + digits[:i]) for i in range(len(digits))]

result = []
for c in candidates:                        #Brute force it, result contains circular primes
    test = _digits_rotations(str(c))
    i = 0
    for t in test:
        if is_prime(t) == True:
            i += 1
    if i == len(str(c)):
        result.append(c)

print(result)
print(len(result))





