#Problem48: Self powers

s = 0
#Caution: 0**0 = 1
#calc number
for i in range(1,1001):
    s += i**i

string = str(s)

#last ten digits of number
print(string[-10:])

