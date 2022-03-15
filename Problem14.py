#Probelm 14: Longest Collatz sequence

def collatz_length(n):
    length = 1
    while n != 1:
        if n % 2 == 0:
            n = n //2
            length = length + 1
        else:
            n = 3*n + 1
            length = length + 1
        #print(n)
    return length

max_length = 0
for i in range(10,1000000):         #1000000 is upper bound
    s = collatz_length(i)
    if  s > max_length:
        max_length = s
        number = i

print(number)

#needs some time, approx 5-50 seconds, depending on hardware