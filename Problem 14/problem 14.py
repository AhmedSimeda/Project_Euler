def iterator(Num):
    if Num % 2 == 0:
        return  Num // 2
    else:
        return 3*Num + 1

Max = 10
S_N = 13
for i in range(13,1000000):
    count = 1
    END   = i
    while END != 1:
        END = iterator(END)
        count += 1
        
    if count > Max:
        Max = count
        S_N = i
    
        print(S_N,Max)




                 
