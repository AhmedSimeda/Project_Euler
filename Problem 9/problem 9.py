import math
def func(c):
    T1 = 2000-2*c
    T2 = T1**2 - 8*(1000**2 - 2000*c)

    try:
        A = (T1 - math.sqrt(T2)) / 4
        B = (T1 + math.sqrt(T2)) / 4
    except:
        return 0

    if A != int(A):
        A = 0

    if B != int(B):
        B = 0

    return (A,B,c)

R = []
for i in range(400,500):
    R.append(func(i))

print(R)


        
