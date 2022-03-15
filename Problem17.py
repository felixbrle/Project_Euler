#Project 17: Number letter counts:

A = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
     'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen',
     'seventeen', 'eighteen', 'nineteen']

B = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty',
     'ninety']

for i in B:             #Add B to A
  A.append(i)           #==> [1-19,20,30,40,50,...,90]
  for d in range(0,9):
    A.append(str(i + A[d]))   #Add to A:i = 0: string i ('twenty') + 'twenty' + ('one', 'two',...,'nine')

for a in range(0,9):        #numbers >= 100
  A.append(str(A[a] + 'hundred')) #create hundreds
  for b in range(0,99):             #fill up hundred
    A.append(str(A[a] + 'hundredand'+ A[b]))

A.append('onethousand')     #1000 is missing
print(A)

count = 0
for a in A:
  count += len(a)     #length of the strings

print(count)