#Problem 22: Names scores

ABC1 = {  " ":"00", "A":"01" , "B":"02" , "C":"03" , "D":"04" , "E":"05" ,
        "F":"06" , "G":"07" , "H":"08" , "I":"09" , "J":"10" ,
        "K":"11", "L":"12", "M":"13", "N":"14", "O":"15",
        "P":"16", "Q":"17", "R":"18", "S":"19", "T":"20",
        "U":"21", "V":"22", "W":"23", "X":"24", "Y":"25", "Z":"26"   }          #Dictionary for letter -> number

data = open("p022_names.txt", 'r')          #read file

names = data.read()
names = names.split(',')
names = [n.strip('"') for n in names]
names.sort()        #ALphabetical order

data.close()        #Python is happy

L = []
for i in range(len(names)):         #Convert letter of names to numbers in list, so easy summation
    L.append([])
    for letter in names[i]:
        L[i].append(ABC1[letter])
    L[i] = list(map(int, L[i]))         #Convert string integers to real integers

print(L)        #test of L

total = 0
i = 1
for name in L:
    sum = 0
    for c in name:
        sum += c
    total += (sum*i)
    i += 1
print(total)