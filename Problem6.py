#Problem 6: Sum square difference
import numpy as np

def difference(n):
    a = np.arange(101)
    return sum(a)**2 - sum(a ** 2)          #Use numpy, faster array calculation function

print(difference(100))
