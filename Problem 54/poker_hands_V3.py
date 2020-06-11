from functools import reduce
import operator
from time import time

start = time()

order = '23456789TJQKA'

def sort(cards):
    if type(cards) == str:
        cards = cards.strip()
    return sorted(cards,key = lambda x: order.index(x),reverse = True)
    
def Max(arg_1,arg_2):
    return sort(reduce(operator.add,[arg_1,arg_2]))[0]

def Min(arg_1,arg_2):
    return sort(reduce(operator.add,[arg_1,arg_2]))[1]

def is_Flush(cards):
    cards = cards.strip()
    Cards_values = cards[0:len(cards):2]
    Cards_suits = cards[1:len(cards):2]
    if len(set(Cards_suits)) == 1:
        return (True,sort(Cards_values))
    return (False,0)

def is_Straight(cards):
    cards = cards.strip()
    Order = order*2
    Cards = ''
    for c in range(0,len(cards),2):
        Cards += cards[c]
    Cards = sort(Cards)[::-1]
    if reduce(operator.add,Cards) in Order:
        return (True,Cards)
    return (False,0)

def is_Royal_Flush(cards):
    cards = cards.strip()
    if is_Flush(cards)[0]:
        if ('T' in cards) & ('J' in cards) & ('Q' in cards) & ('K' in cards) & ('A' in cards):
            return (True,'A')
    return (False,0)

def is_Straight_Flush(cards):
    cards = cards.strip()
    if is_Flush(cards)[0] & is_Straight(cards)[0]:
        return (True,sort(cards[0:len(cards):2]))
    return (False,0)

def is_Four_of_a_Kind(cards):
    cards = cards.strip()
    Cards = ''
    for card in range(0,len(cards),2):
        Cards += cards[card]

    if len(set(Cards)) == 2:
        for i in set(Cards):
            if Cards.count(i) == 4:
                temp = list(set(Cards))
                temp.remove(i)
                return (True,[i,temp[0]])
    return (False,0)

def is_Three_of_a_Kind(cards):
    cards = cards.strip()
    Cards = ''
    for c in range(0,len(cards),2):
        Cards += cards[c]

    for c in set(Cards):
        if Cards.count(c) == 3:
            temp = list(set(Cards))
            temp.remove(c)
            return (True,[c]+sort(temp))
    return (False,0)

def is_Two_Pairs(cards):
    cards = cards.strip()
    Cards = ''
    for card in range(0,len(cards),2):
        Cards += cards[card]
    
    pair = []
    for c in set(Cards):
        if Cards.count(c) == 2:
            pair.append(c)
            if len(pair) == 2:
                temp = list(set(Cards))
                for p in pair:
                    temp.remove(p)
                
                return (True,[Max(pair[0],pair[1]),Min(pair[0],pair[1]),temp[0]])
    return (False,0)

def is_One_Pair(cards):
    cards = cards.strip()
    Cards = ''
    for card in range(0,len(cards),2):
        Cards += cards[card]

    for c in set(Cards):
        if Cards.count(c) == 2:
            temp = list(set(Cards))
            temp.remove(c)
            return (True,[c]+sort(temp))
    return (False,0)

def is_Full_House(cards):
    cards = cards.strip()
    if is_Three_of_a_Kind(cards)[0] and is_One_Pair(cards)[0]:
        return (True,[is_Three_of_a_Kind(cards)[1][0],is_One_Pair(cards)[1][0]])
    return (False,0)

def compare(list_1,list_2):
    for p_1,p_2 in zip(list_1,list_2):
        if p_1 != p_2:
            if Max(p_1,p_2) == p_1:
                return True
            else:
                return False

def p1_win(game):
    rank = ['is_One_Pair','is_Two_Pairs','is_Three_of_a_Kind','is_Straight','is_Flush','is_Full_House','is_Four_of_a_Kind','is_Straight_Flush','is_Royal_Flush']
    game = game.split(' ')
    Cards_p1 = reduce(operator.add,game[:5])
    Cards_p2 = reduce(operator.add,game[5:])
    #print(Cards_p1,Cards_p2)
    if is_Royal_Flush(Cards_p1)[0] and not is_Royal_Flush(Cards_p2)[0]:
        return (True,"Royal Flush")
    elif not is_Royal_Flush(Cards_p2)[0]:
        for r in range(len(rank)-1):
            if not eval(rank[::-1][r])(Cards_p2)[0]:
                if eval(rank[::-1][r+1])(Cards_p1)[0] and not eval(rank[::-1][r+1])(Cards_p2)[0]:
                    return (True,rank[::-1][r+1])
                elif eval(rank[::-1][r+1])(Cards_p1)[0] and eval(rank[::-1][r+1])(Cards_p2)[0]:
                    if compare(eval(rank[::-1][r+1])(Cards_p1)[1],eval(rank[::-1][r+1])(Cards_p2)[1]):
                        return (True,rank[::-1][r+1])
                    else:
                        return (False,rank[::-1][r+1])
            else:
                return (False,rank[::-1][r])
        if not is_One_Pair(Cards_p2)[0]:
            if compare(sort(Cards_p1[0:len(Cards_p1):2]),sort(Cards_p2[0:len(Cards_p2):2])):
                return (True,"High Card")
            else:
                return (False,"High Card")
        else:
            return (False,"One_pair")
    return (False,"Royal Flush",Cards_p1,Cards_p2)
count = 0
with open("p054_poker.txt",'r') as Games:
    for game in Games:
     #   print(' '.join(game.split(' ')[:5]) + ' // ' + ' '.join(game.split(' ')[5:]))
        if p1_win(game)[0]:
           count += 1
    #    print(' '.join(game.split(' ')[:5]) + ' // ' + ' '.join(game.split(' ')[5:]))
    #    input()
     #   print(p1_win(game))
      #  In = input()
       # if In == '1':
        #    count += 1
        
print(count)
#print(p1_win('6H 5H 4C 3H 2H 3S QH 5S 6S AS'))
#print(is_One_Pair("6S3C3HAS7S"))
#cards = '6C4S5H5S6D'
#print(cards[1:len(cards):2])
#print(sort('7253A'))
#print(is_Straight("7D2S5D3SAC"))
#print(is_Straight_Flush("6S3C3HAS7S"))

end = time()
print("=====================================")
print("time taken : " + str(end-start) + " s")
print("=====================================")
      
