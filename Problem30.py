#Problem 30: Digit fifth powers

upper_bound = 5*9**5            #calculate upper bound
print(upper_bound)

A = []

for i in range(2,300000):               #Brute force it
    s = str(i)
    if i == sum([int(z)**5 for z in s]):            #condition testing
        A.append(i)

print(A)
print(sum(A))