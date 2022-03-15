#Problem50: Consecutive prime sum

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

candidates = eratosthenes(1000000)

s = 0
max = 0

#brute force

for i in range(len(candidates)):
    if candidates[i] > 500000:      #dont know if its true, but programm runs still correct
        break
    for j in range(0,i):
        liste = candidates[j:i + 1]         #start with longest list of consecutive number
        length = len(liste)
        prime = sum(liste)
        if prime in candidates and length > max and prime < 1000000:    #check conditions
            max = length
            s = prime
        break       #list just gets shorter
    print(candidates[i])

print(max)       #just for interest
print(s)


#takes long time