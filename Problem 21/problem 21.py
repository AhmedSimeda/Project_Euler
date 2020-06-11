import math

def Factorize(Num):
    factors = [1]
    for i in range(2,int(math.sqrt(Num))+1):
        if Num % i == 0:
            factors += [i,Num//i]
    return list(sorted(factors))

taken = []            
for i in range(1,10000):
    F = sum(Factorize(sum(Factorize(i))))
    if i == F :
        if sum(Factorize(i)) != i:
            taken.append(i)

    
print(sum(taken))




