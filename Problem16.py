#Proble 16: Digit sum of 2^1000


n = str(2**1000)            #string gives nice use in for loop
count = 0
for z in n:
    count += int(z)                 #sum

print(count)
