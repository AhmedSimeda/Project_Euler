from functools import reduce
import operator

number = open(r'1000-digit number.txt','r')
Num    = ''
for line in number:
    Num += line[:-1]

print(len(Num))

Max = 0
for i in range(len(Num)-13):
    Nums = [int(i) for i in Num[i:i+13]]
    prod = reduce(operator.mul,Nums)
    if prod > Max:
        Max = prod

print(Max)
    
