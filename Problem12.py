#Problem12: Highly divisible triangular number (500 divisors)

def k_teWurzel_n(n,k):          #faster than math sqrt and rounding / numerical stable
    L, R = 1, n
    while R - L >= 2:
        M = (L+R)//2
        if M**k <= n:
            L = M
        else:
            R = M
    return L

def number_of_divisors(num):                #count divisors
    count, n = 1, 1
    stop = k_teWurzel_n(num,2) + 1          #faster
    while n < stop:
        if num % n == 0:
            count += 2              #28 mod 2 = 0 ==> 2 AND 14 are divisors
        n += 1
    return count


def get_triangle_number(upperbound):        #condition testing
    n = triangle_number = 0
    while number_of_divisors(triangle_number) < upperbound:
        n += 1
        triangle_number += n
    return triangle_number


print(get_triangle_number(500))

#need some time approx 5-40 seconds, depending on hardware
