#Num_W  = ["one" , "two" , "three" , "four" , "five" , "six" , "seven" , "eight" , "nine", "ten" , "eleven" , "twelve" , "thirteen" , "fourteen" , "fifteen" , "sixteen" , "seventeen" , "eighteen" , "nineteen"]

Cloud_0  = ["one" , "two" , "three" , "four" , "five" , "six" , "seven" , "eight" , "nine", "ten" , "eleven" , "twelve" , "thirteen" , "fourteen" , "fifteen" , "sixteen" , "seventeen" , "eighteen" , "nineteen"]
Cloud_1  = ["twenty" , "thirty" , "forty" , "fifty" , "sixty" , "seventy" ,"eighty" , "ninety"]
Cloud_2  = ["one" , "two" , "three" , "four" , "five" , "six" , "seven" , "eight" , "nine" ]


Sum = sum([len(i) for i in Cloud_0])

for i in Cloud_1:
    #Num_W += [i]
    Sum += len(i)
    for j in Cloud_2:
        #Num_W += [i+j]
        Sum += len(i+j)

for i in Cloud_2:
    #Num_W += [i + "hundred"]
    Sum += len(i + "hundred")
    for j in Cloud_0:
        #Num_W += [i+ "hundredand" + j]
        Sum += len(i+ "hundredand" + j)
    for l in Cloud_1:
        #Num_W += [i + "hundredand" + l]
        Sum += len(i + "hundredand" + l)
        for k in Cloud_2:
            #Num_W += [i + "hundredand" + l + k]
            Sum += len(i + "hundredand" + l + k)


#print(Num_W)
print( Sum + len("onethousand") )
