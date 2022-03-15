#Problem31: Coin sums

counter = 0
#get all solutions of the euqtion: a + 2b + 5c + 10d + 20e + 50f + 100g = 200
#where (a,b,c,d,e,f,g) integers^7, a sum of 1 pence in equation

for a in range(3):          #a here is number of 100pence / 1 pund coins
	for b in range(1+(200-100*a)//50):
				for c in range(1+(200-100*a-50*b)//20):
						for d in range(1+(200-100*a-50*b-20*c)//10):
								for e in range(1+(200-100*a-50*b-20*c-10*d)//5):
										for f in range(1+(200-100*a-50*b-20*c-10*d-5*e)//2):
											counter += 1

print(counter+1)        #add 1 for 2 pounds coin