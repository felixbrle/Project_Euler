#Problem 33: Digit cancelling fractions
from fractions import Fraction
#less than one in value: denominator > numerator

def check(n, d):                        #checker function
    num = [int(i) for i in str(n)]
    den = [int(i) for i in str(d)]
    for i in num:
        for j in den:
            if i == j and i * j != 0:           #i * j == 0 is bad
                num.remove(i)
                den.remove(j)
                if num[0] != 0 and den[0] != 0:         #explicit testing for dividing though zero
                    if Fraction(num[0], den[0]) == Fraction(n,d):
                        return True
                    else:
                        return False
    return False

candidates = []

#go though all numbers 10-100:

for a in range(11,100):
    for b in range(a+1,100):            #a+1 due to value has to be less than one
        if b <= a:
            continue
        else:
            if check(a, b) == True:             #check condition
                candidates.append(Fraction(a, b))

print(candidates)

prod = 1
for i in candidates:
    prod = prod * i

print(prod)