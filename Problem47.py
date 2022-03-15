#Problem47: Distinct prime factors

#Primfaktorzerlegung

def prim_fac(n):
    p = []
    e = []
    if n % 2 == 0:
        ee = 1
        n = n / 2
        while n % 2 == 0:
            ee += 1
            n = n / 2
        p.append(2**ee)
    pp = 3
    while pp ** 2 <= n:
        if n % pp == 0:
            ee = 1
            n = n/pp
            while n % pp == 0:
                ee += 1
                n = n / pp
            p.append(pp**ee)
        pp += 2
    if n > 1:
        p.append(n)
    return p

#Just choose greates prime divisor, if ee > 1, for condition
print(prim_fac(62))

count = 50

#brute force, test condition: minimum 4 prime factors  for 4 numbers
while True:
    if len(prim_fac(count)) == 4:       #just interested in numbers with four different prime factors
        count += 1
        if len(prim_fac(count)) == 4:
            count += 1
            if len(prim_fac(count)) == 4:
                count += 1
                if len(prim_fac(count)) == 4:
                    print(count -3)
                    break
    count += 1