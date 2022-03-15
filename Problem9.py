#Problem 9: Special pythagorean triplet, 1000:

triplet = []
for a in range(1,1000):
    for b in range(1,1000):
        c = 1000 - b - a            # first condition for solution
        if a**2 + b**2 == c**2:
            triplet = [a,b,c]
            break

#show tirplet and calc product
print(triplet)

produkt = 1
for i in triplet:
    produkt = produkt * i

print(produkt)