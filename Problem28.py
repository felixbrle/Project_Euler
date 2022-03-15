#Problem 28: Number spiral diagonals

N = 1001
n = N*N                             #right upper corner
summe = n
for i in range(N-1, 0, -2):         #if we have one round done: two columns less
    for j in range(4):              #go to the corners
        n += -i                     #calculate corner value
        summe += n                  #add corner value

print(summe)