#Problem 39: Integer right triangles

#Pretty straight forward, just test condition and use
#c^2 = a^2 + b^2

candidates = []

for a in range(1,500): #obvious upper bound
    for b in range(a, 500): #b >= a
        c = (a**2 + b ** 2) ** 0.5
        if int(c) == c and a + b + c <= 1000: #asked fpr integer solution
            candidates.append(a + b + c)


result = {c: candidates.count(c) for c in candidates}   #counter of list element in dictionary form

print(max(result.values()))
# == 8
m = max(result.values())
print([key for key in result if result[key] == m])
