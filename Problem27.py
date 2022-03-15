#Problem 27: Quadratic Primes

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

prime_th = eratosthenes(1000)

def condition(a,b):
    test = eratosthenes(1000)
    n = 0
    while n*n + a*n + b in test:
        n += 1
    return [n, a, b]

#abs(a) and abs(b) has to be prime AND a and b can not b negative at the same time
max = 0

prime = prime_th        #double the list, we work with her
prime_2th = eratosthenes(2000)          # n = 1== > p = 1 + a + b ==> a = x - b - 1

candidates = []         #set of pairs, where the first two numbers are prime

for b in prime_th:
    for x in prime_2th:
        a = x - b - 1
        if a >= 1000:
            break
        candidates.append([a,b])

print(candidates)

max = 0
ls = []
pair = []
for c in candidates:
    i = 0
    while is_prime(i**2 + c[0]*i + c[1]) == True and i**2 + c[0]*i + c[1] > 0:      #test all pairs
        i = i+1
    if i > max:
        max = i
        ls.append(i)
        candidate = [c[0], c[1]]

print(ls)
print(max)
print(candidate)
print(candidate[0]*candidate[1])




