#Problem20: Factorial digit sum

def fak(n):             #n! not recursive for speed, n = 1 * 2 * ... * n
    result = 1
    for i in range(1,n):
        result = result * i
    return n*result

n = str(fak(100))
count = 0
for z in n:
    count += int(z)

print(count)