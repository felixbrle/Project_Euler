#Problem32: Pandigital products

digits = "123456789"

#product = 5 digits: ==> 100*100= 10000 doesnt work
#first approximation numbers has to be in 1-5000 and 1-5000 for having with product just 9 digits, product has to have 4 digits
#second approximation: numbers has to be in 1-1000 and 1-5000
#third approximation: numbers has to be in 1-500 and 1-2500: works
candidates = []
for a in range(1,500):              #Brute forceing and condition testing
    for b in range(1,2500):
        if "".join(sorted(str(a)+str(b)+str(a*b))) == "123456789":
            candidates.append(a*b)

result = []
for i in candidates:
    if i not in result:
        result.append(i)

print(sum(result))

