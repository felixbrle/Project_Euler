#Problem 23: Non-abundant numbers

def k_teWurzel_n(n,k):          #Algorithm for k-th root of n in natural numbers
    L, R = 1, n
    while R - L >= 2:
        M = (L+R)//2
        if M**k <= n:
            L = M
        else:
            R = M
    return L

def sum_divisors(n):
    A = [1]
    for i in range(2,k_teWurzel_n(n,2)+1):
        if n % i == 0:
            A.extend([i,n/i])           #append i and n/i
    return sum(list(set(A)))

ab = []

for i in range(12,28123):
    if sum_divisors(i)>i:                  #abundant numbers
        ab.append(i)

non_ab_sum = [i for i in range(28123)]          #candidates

for i in range(len(ab)):
    for j in range(i,28123):
        if ab[i]+ab[j] < 28123:             #check condition
            non_ab_sum[ab[i]+ab[j]] = 0
        else:
            break

print(sum(non_ab_sum))




