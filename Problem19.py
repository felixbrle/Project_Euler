#Problem19: Counting Sundays:
import calendar

calendar.setfirstweekday(6)

#print(calendar.firstweekday())
#print(calendar.monthcalendar(2022,2))

def number_of_sundays(year):
    count = 0
    for i in range(1,13):      #go through all months
        dates = calendar.monthcalendar(year, i)     #generate a "matrix"
        if dates[0][0] == 1:
            count += 1
    return count

sum_of_sundays = 0

for i in range(1901,2001):      #go though all years
    sum_of_sundays += number_of_sundays(i)

print(sum_of_sundays)

