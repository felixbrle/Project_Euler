#Problem 36: Double-base palindromes

def check_palindrome(n):        #Palindrome checker
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False


sum = 0
for c in range(1,1000000):              #brute force it
    if check_palindrome(c) == True and check_palindrome(format(c, "b")) == True:        #format is a nice function
        sum += c

print(sum)