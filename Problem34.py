#Problem 34: Digit factorials

def factorialIterative(n):          #factorial, not recursiv (numerical problems)
    result = 1
    if n == 0:
        return 1
    else:
        for i in range(n):
            result = result*(i+1)
        return result

#Test first upper bound as 1,000,000: Result: Not callable, but candidate set is solution [145,40585], speed is okay, 3 seconds
#==> 100,000 as upper bound works

candidates = []

for i in range(3,100000):              #find candidates
    sum = 0
    for z in str(i):
        sum += factorialIterative(int(z))
        if sum == i:
            candidates.append(i)

print(candidates)

sum = 0
for c in candidates:
    sum += c

print(sum)

