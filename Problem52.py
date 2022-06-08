#52: Permuted multiples

stop = False
number = 1

def sorted_string(s):
    return "".join(sorted(str(s)))                                              #sorted string of number alphabetical

while stop is False:
    if (sorted_string(number) == sorted_string(2*number) and                    #Check conditions
        sorted_string(number) == sorted_string(3*number) and
        sorted_string(number) == sorted_string(4*number) and
        sorted_string(number) == sorted_string(5*number) and
        sorted_string(number) == sorted_string(6*number)):
        stop = True
    else:
        number += 1

print(number)