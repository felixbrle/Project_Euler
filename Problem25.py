#Problem 25: 1000-digit Fibonacci number

f1, f2, i = 1, 1, 3
n = 1000
l = 1           #fib(3) = 1 + 1
while l < n:                #calculate fibonacci "with hand"
    fib = f1 + f2
    f2, f1, l = f1, fib, len(str(fib))
    if l >=n:           #if we fulfill condition, we dont go up
        break
    i += 1

print(i)