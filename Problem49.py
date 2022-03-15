#Proble49: Prime permutations
from itertools import combinations, permutations

#Prime stuff
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

#candidates for the 4 digit number:

candidates = eratosthenes(10000)

#existence is safe ==>

for c in candidates:
    if c > 3340:        #upperbound for 4 digit
        break
    n = c + 3330
    s = c + 6660
    if c != 1487:
        if (sorted(str(c)) == sorted(str(n)) and  # condition for permutation
            sorted(str(c)) == sorted(str(s))):
            if n in candidates and s in candidates:     #test prime condition
                print(str(c) + str(n) + str(s))
                break
