import math
def Factorize(Num):
    Factors = [1,Num]
    for i in range(2,int(math.sqrt(Num))+1):
        if Num % i == 0:
            Factors.append(i)
            Factors.append(Num//i)

    return len(Factors)

S = 1
F = Factorize(S)
while F <= 500:
    Sum = sum([i for i in range(S)])
    F = Factorize(Sum)
    S += 1

print(Sum)
