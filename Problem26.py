#Problem 26: Reciprocal cyles

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

def sam_3(a,d,n):           #SQUARE AND MULTIPLY algo / Algebra
  b, c = 1, a % n
  while d > 0:
    while d % 2 == 0:
      c , d = c**2 % n, d//2
    b ,d = (b*c) % n, d - 1
  return b

def naive_ord(a,n):             #calculate ord von a modulo n
    for k in range(1,n+1):
        if sam_3(a, k, n) == 1:
            return k

divisors = eratosthenes(1000)           #candidates
del divisors[0]
del divisors[1]             #delete 2 and 5 out of list , due to 10 = 2*5

print(divisors)

#Cycle length is multiplicative order of 10 in d corp, for gcd(d, 10) = 1, use primes, so fcd condition
#is always working


max = 0
for d in divisors:              #get the max
    candidate = naive_ord(10,d)
    if candidate > max:
        max = d

sol = max
print(sol)