import math
def is_prime (Num):
    if   Num == 1      :
        return False
    elif Num <  4      :
        return True
    elif Num %  2 == 0 :
        return False
    elif Num <  9      :
        return True
    elif Num %  3 == 0 :
        return False
    else:
        x = int(math.sqrt(Num))
        n = 5
        while n <= x:
            if Num % n == 0     : return False
            if Num % (n+2) == 0 : return False
            n += 6
        return True

Sum = 2
for i in range(3,2000000,2):
    if is_prime(i):
        Sum += i
        
print(Sum)
