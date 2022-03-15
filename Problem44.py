#Problem44: Pentagon numbers

#pentagon function
#Wikipedia: if n = (sqrt(24*x + 1)+1)/6 is an integer ==> n in pentagonal number
def pentagonal_number_check(n):         #condition check
    if ((24*n+1)**0.5 + 1) % 6 == 0:
        return True
    else:
        return False

def pentagonal_number(n):           #calc pentagonal number
    return int(n*(3*n-1)/2)

#test
print(pentagonal_number_check(35))

#start with an upper bound of 10000, approximated, worked:
#second upperbound 5000 also works
#printed a and b ==> 2200 as upper bound is sufficient
candidates = []
result = []
#Calculate all differnces
for a in range(1,2200):
    candidates.append(pentagonal_number(a))
    for b in range(0, len(candidates) - 1):     #upperbound, due to difference
        if (pentagonal_number_check(candidates[a-1] + candidates[b-1]) == True and          #check difference and sum
            pentagonal_number_check(candidates[a - 1] - candidates[b - 1]) == True):
            result.append(abs(candidates[a-1] - candidates[b-1]))
            print(a,b)

print(result)
print(min(result))

