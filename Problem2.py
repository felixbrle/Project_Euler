#Problem2: Sum of even fibonacci numbers less 4 MIO
import numpy as np


def fibonacci(n):       #Fibonacci based on matrix multiplication for speed
    if n == 0:
        return np.matrix('1; 0')
    else:
        vector = fibonacci(n-1)
        return np.matrix('1 1; 1 0')*vector

counter = 0
sum = 0
while fibonacci(counter)[0] < 4000000:
    s = fibonacci(counter)[0]
    if s % 2 == 0:
        sum += s
    counter += 1

print(sum)
