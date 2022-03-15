#Problem 42:

ABC1 = {  " ":"00", "A":"01" , "B":"02" , "C":"03" , "D":"04" , "E":"05" ,
        "F":"06" , "G":"07" , "H":"08" , "I":"09" , "J":"10" ,
        "K":"11", "L":"12", "M":"13", "N":"14", "O":"15",
        "P":"16", "Q":"17", "R":"18", "S":"19", "T":"20",
        "U":"21", "V":"22", "W":"23", "X":"24", "Y":"25", "Z":"26"   }          #Dictionary for letter -> number

data = open("p042_words.txt", 'r')          #read file

names = data.read()
names = names.split(',')
names = [n.strip('"') for n in names]
names.sort()        #ALphabetical order

data.close()        #Python is happy

def triangle_number(n):     #short function
    return 0.5 * n * (n + 1)

triangle_numbers = []
count = 1
t = 1
while t < 1000:          #get triangle numbers based on upperbound below
    t = int(triangle_number(count))
    triangle_numbers.append(t)
    count += 1

#print(triangle_numbers)

words1 = []
for n in names:             #turn words in numbers
    w = 0
    for z in n:
        w = w + int(ABC1[z])
    words1.append(w)

words = list(map(int, words1))
#print(words)

print(max(words))  #200 ==> upper bound for triangle numbers

triangle_words = []
for w in words:
    if w in triangle_numbers:
        triangle_words.append(w)

#print(triangle_words)
print(len(triangle_words))


