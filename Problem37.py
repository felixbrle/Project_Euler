#Problem 37: Truncatable primes

#Start with upper bound of 1000000

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
    if n == 1 or n == 0:                #one or zero are ot prime
        return False
    for i in range(2,k_teWurzel_n(n,2)+1):
        if n % i == 0:
            return False
    return True

candidates = eratosthenes(1000000)


def trunc_check(number):                        #condition checker
    for i in range(0, len(str(number))):
        if not is_prime(int(str(number)[i:])) or not is_prime(int(str(number)[:i+1])):
            return False
    return True

#test
print(trunc_check(3797))
print(trunc_check(8930212))

trunc_numbs = []

for c in candidates:
    if is_prime(c) and trunc_check(c) and c > 8:
        trunc_numbs.append(c)

print(trunc_numbs)
print(sum(trunc_numbs))

