#Problem41: Pandigital Prime

#Prime Stuff:
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

#tried some upperbounds, 100000, 1000000, 10000000, ...
candidates = eratosthenes(10000000)    #huge, there is potential

def check_pandigital(n):        #pandigital checker
    s = ""
    for i in range(1, len(str(n)) + 1):
        s += str(i)
    if sorted(str(n)) == sorted(s):
        return True
    else:
        return False

max = 0
for c in candidates:            #brute force it
    if max < c and check_pandigital(c):
        max = c

print(max)