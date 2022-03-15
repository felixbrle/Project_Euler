#Problem1: Multiples of 3 or 5 for numbers between 0 and 1000
import numpy as np

print(sum(np.array(list(p for p in range(1,1000) if p % 3 == 0 or p % 5 == 0))))    #use modulo operator, numpy for speed
