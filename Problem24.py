#Problem 24: Lexicographic permutations
import itertools

A = list(range(10))

def permutations(string):
    p = list(itertools.permutations(string))            #itertools can do it
    return p[1000000-1]

s = permutations("0123456789")
print(s)

print("".join([str(i) for i in s]))         #get number out of tuple