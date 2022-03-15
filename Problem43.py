#Problem43: Sub-string divisibility

from itertools import permutations

candidates = permutations("0123456789")         #all pan digital 0-9 numbers

#Now just check the candidates on the condition:

count = 0
#Modulo Operator equals 0 ==> divisible
#Tuple ==> join
for c in candidates:
    if (int("".join(c[1:4])) % 2 == 0 and
        int("".join(c[2:5])) % 3 == 0 and
        int("".join(c[3:6])) % 5 == 0 and
        int("".join(c[4:7])) % 7 == 0 and
        int("".join(c[5:8])) % 11 == 0 and
        int("".join(c[6:9])) % 13 == 0 and
        int("".join(c[7:10])) % 17 == 0):
        count += int("".join(c))

print(count)