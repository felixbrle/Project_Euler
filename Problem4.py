#Problem4: Find largest palindrome product made from the product of two 3 digest numbers.

def check_palindrome(n):        #Palindrome checker
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False

A = []
for i in range(101,1000):
    for j in range(101,1000):
        if check_palindrome(i*j) == True and i*j not in A:
            A.append(i*j)

def quicksort(a, l, r):     #just for fun, maybe faster than "max" function
    i = l
    j = r
    while i < j:
        while a[i] <= a[r] and i < j:
            i = i+1
        while a[j] >= a[r] and i < j:
            j = j-1
        tmp = a[i]
        a[i] = a[j]
        a[j] = tmp
    tmp = a[i]
    a[i] = a[r]
    a[r] = tmp

    if l < i-1:
        quicksort(a, l, i-1)
    if r > i+1:
        quicksort(a, i+1, r)
    return a

print(quicksort(A, 0, len(A)-1)[len(A)-1])
