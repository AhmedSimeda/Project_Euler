from math import sqrt

def is_prime(Num):
    if Num <= 1:
        return False
    for i in range(2,int(sqrt(Num))+1):
        if Num % i == 0 :
            return False

    return True

count = 0
Num   = 1
while count != 10001:
    Num += 1
    if is_prime(Num):
        count +=1

print(Num)
            
