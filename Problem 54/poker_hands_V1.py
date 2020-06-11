from functools import reduce
import operator

def is_Flush(cards):
  Type = ''
  for t in range(1,len(cards),2):
    Type += cards[t]

  if len(set(Type)) == 1:
    return True
  return False

def is_Straight(cards):
  order = '23456789TJQKA'
  Card = ''
  for card in range(0,len(cards),2):
    Card += cards[card] 

  if Card in order:
    return True
  return False

def is_Royal_Flush(cards):
  if is_Flush(cards):
    if ('T' in cards) & ('J' in cards) & ('Q' in cards) & ('K' in cards) & ('A' in cards):
      return True
  return False

def is_Straight_Flush(cards):
  if is_Flush(cards) & is_Straight(cards):
    return True
  return False

def is_Four_of_a_Kind(cards):
  Card = ''
  for card in range(0,len(cards),2):
    Card += cards[card]

  if len(set(Type)) == 2:
    return True
  return False

def is_Three_of_a_Kind(cards):
  Card = ''
  for card in range(0,len(cards),2):
    Card += cards[card]

  if Cards.count(set(Cards)[0]) != 3:
      return False
  return True

def is_Two_Pairs(cards):
  Card = ''
  for card in range(0,len(cards),2):
    Card += cards[card]

  for c in set(Cards)[:-1]:
    if Cards.count(c) != 2:
      return False
  return True

def is_Three_of_a_Kind(cards):
  Card = ''
  for card in range(0,len(cards),2):
    Card += cards[card]

  if Cards.count(set(Cards)[0]) != 3:
      return False
  return True

def p1_win(game):
  rank = ['High Card','One Pair','Two Pairs','Three of a Kind','Straight','Flush','Full House','Four of a Kind','Straight Flush','Royal Flush']
  game = game.split(' ')
  Cards_p1 = reduce(operator.add,game[:5])
  Cards_p2 = reduce(operator.add,game[5:11])[:-1]

count = 0
with open(r"C:\Users\ALREHAB\Desktop\p054_poker.txt",'r') as Games:
  for game in Games:
    if p1_win(game):
      count += 1
