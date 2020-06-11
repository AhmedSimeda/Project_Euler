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
        for i in range(5,int(math.sqrt(Num)+1),2):
            if Num % i == 0:
                return False
        return True

Sum = 2
for i in range(3,2000000,2):
    if is_prime(i):
        Sum += i
        
print(Sum)

