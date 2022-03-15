#Problem40: Champernowne's constant

#we approximate an uperbound at:
#9 *  1 + 90*2 + 900 * 3 + ....
#upperbound at

print(9 + 90*2 + 900* 3 + 9000 * 4 + 90000* 5)
print(9 + 90*2 + 900* 3 + 9000 * 4 + 90000* 5 + 900000*6)
#==> 488889 <= 1000000 <= 5888889 ==> choose 1000000 as upper bound

number = ""

for i in range(1,1000100):      #create number
    number += str(i)

d2 , d3, d4, d5, d6, d7 = int(number[9]), int(number[99]), int(number[999]), int(number[9999]), int(number[99999]), int(number[999999])

print(d2 * d3 * d4 * d5 * d6 * d7)