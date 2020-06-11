Fact = 1
Number = int(input("Enter the Number : "))

for i in range(2,Number+1):
    Fact *= i

Sum = 0

for i in range(len(str(Fact))):
    Sum += int(str(Fact)[i])

print(Sum)
    
