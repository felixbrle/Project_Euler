#Problem45: Triangular, pentagonal and hexagonal

#Check function Functions for all those numbers
#==> just have to calculate one number ==> faster

#Look wikipedia for conditions
def pentagonal_number_check(n):         #condition check
    if ((24*n+1)**0.5 + 1) % 6 == 0:
        return True
    else:
        return False

def hexagonal_number_check(n):        #wikipedia
    if ((8*n + 1)**0.5 + 1) % 4 == 0:
        return True
    else:
        return False

#test
print(pentagonal_number_check(22), hexagonal_number_check(28))

count = 286         #we look for the next number

while True:
    n = count*(count + 1)/2
    if pentagonal_number_check(n) and hexagonal_number_check(n):        #check condition
        print(int(n))
        break
    count += 1
