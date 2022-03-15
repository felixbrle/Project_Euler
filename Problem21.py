#Problem 21: Amicable numbers

def k_teWurzel_n(n,k):          #Algorithm for k-th root of n in natural numbers for upperbound
    L, R = 1, n
    while R - L >= 2:
        M = (L+R)//2
        if M**k <= n:
            L = M
        else:
            R = M
    return L

def find_divisors_sum(n):       #find divisors
    A = [1]
    for i in range(2, k_teWurzel_n(n,2) +1):
        if n % i == 0:                      #28 % 2 = 0 ==> divisors, but also 28 /2 = 14 is divisor
            A.append(i)
            A.append(n//i)
    return sum(A)

def test_amicable(a,b):
    if a != b and find_divisors_sum(a) == b and find_divisors_sum(b) == a:          #test condition
        return True
    return False

#Test functions
#print(find_divisors_sum(220))
#print(find_divisors_sum(284))
#print(test_amicable(220,284))

count = 0
for i in range(1,10000):
    j = find_divisors_sum(i)
    if test_amicable(i,j) == True:
        count += i                  #double counting problem, we also get j


print(count)


