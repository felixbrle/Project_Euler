#Problem3: Largest prime factor 600851475143

def k_teWurzel_n(n,k):          #Algorithm for k-th root of n in natural numbers
    L, R = 1, n
    while R - L >= 2:
        M = (L+R)//2
        if M**k <= n:
            L = M
        else:
            R = M
    return L

n = 600851475143
lpf = 0
for i in range(3,k_teWurzel_n(n,2),2):          #step of 2 due to prime searching
    if n % i == 0:
        while n % i == 0:
            n = n/i
        lpf = i

print(lpf)
