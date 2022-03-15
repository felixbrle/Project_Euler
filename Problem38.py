#Problem 38: Pandigital multiples

def check(n):       #condition tester
    if sorted(n) == ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        return True
    else:
        return False

candidates = []         #go through all numbers with some approximated upper bounds, 10000, 100
for i in range(10000):
    t = ""
    for j in range(1,100):
        if len(t) < 9:
            t = t + str(i * j)
    if check(t):
        candidates.append(t)

print(candidates)
A = list(map(int, candidates))
#Get maximum
print(max(A))
