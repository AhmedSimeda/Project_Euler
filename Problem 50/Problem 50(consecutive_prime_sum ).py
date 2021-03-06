# -*- coding: utf-8 -*-
"""Consecutive prime sum.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OwXoatHPq03UYbda4lKclX5VTWKNct2u
"""

from math import sqrt

def is_prime(Num):
  if Num <= 1 :
    return False
  else:
    for i in range(2,int(sqrt(Num))+1):
      if Num % i == 0 :
        return False
    return True

def right_to_left(prime_array,limit):
  Sum = []
  for i in range(len(prime_array),0,-1):
    S = sum(prime_array[:i])
    if (not (S > limit)) & (is_prime(S)):
      Sum.append([S,len(prime_array[:i])])
  return Sum

from time import time
start = time()

limit = 1000000
P_Nums = [2] + [j for j in range(3,limit,2)if is_prime(j)]
P_Nums = P_Nums[:len(P_Nums)//4]
Sum = []
for i in range(len(P_Nums)):
    Sum += right_to_left(P_Nums[i:],limit)

end = time()
print("=====================================")
print("time taken : " + str(end-start) + " s")
print("=====================================")

P_Nums = [2] + [j for j in range(3,limit,2)if is_prime(j)]
len(P_Nums)//4

Max = 0
F_Sum = 0
for S in Sum:
  if S[1] > Max:
    Max = S[1]
    F_Sum = S[0]

F_Sum,Max