#Problem 15: Routes in 20x20 grid

#Can be solved with bonomial coefficient, some theory look Wikipedia / Lattice paths
def fak(n):         #calc n! recursive: n! = n * (n-1)!
    if n < 1:
        return 1
    else:
        return n * fak(n-1)

print(fak(6))

print(fak(40)/fak(20)/fak(20))         #Calculate binomial coefiicent