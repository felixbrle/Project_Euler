#Problem29: Distinct powers

A = []
for a in range(2,101):          #Brute force it
    for b in range(2,101):
        A.append(a**b)

result = []
for a in A:
    if a not in result:             #generate distinct list
        result.append(a)
print(result)
print(len(result))