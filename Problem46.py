#Problem46: Gladbach's other conjuecture
#Prime Stuff
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


#brute force: condition for break: (n-oddint)/2 == i**2
#when now sqrt(n-oddint)/2) is integer, we know, that such combination exist

candidates = []

n = 3
#brute force it
while True:
    if is_prime(n) == True:
        candidates.append(n)
        n += 2      #prime works always, just choos 0**2
        continue
    elif n % 2 != 0:        #odd number
        for i in candidates:
            if (((n-i)/2))**0.5 == int((((n-i)/2))**0.5):       #test condition
                break
        else:
            print(n)
            break
    n += 2

