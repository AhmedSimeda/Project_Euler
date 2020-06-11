# -*- coding: utf-8 -*-
"""Prime permutations.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OwXoatHPq03UYbda4lKclX5VTWKNct2u
"""

from itertools import permutations
import numpy as np

def do_List(Num,Reference):
  return Num > Reference

def has_prop(Number):
  Num = ""
  for N in str(Number):
    Num += N
  
  if len(Num) < 4:
    "0" + Num

  #if len(set(str(Number))) != 4:
    #return [False,0]

  List = list(map(lambda x:int(''.join(x)),list(filter(lambda x:do_List(int(''.join(x)),int(Num)),list(permutations(Num))))))

  for i in range(len(List)):
    List[i] = List[i] - int(Num)


  List_2 = np.array([List])//2

  for num in List:
    if num in List_2:
      return [True,num]
  return [False,0]

from math import sqrt 

def is_prime(Num):
  if Num <= 1 :
    return False
  else:
    for i in range(2,int(sqrt(Num))+1):
      if Num % i == 0 :
        return False
    return True

PP = []
for i in range(100,9999):
  H = has_prop(i)
  if H[0]:
    PP.append((i,H[1]))

Result = []
for I in PP:
  Nums = [I[0]]
  for j in range(1,3):
    Nums.append(I[0]+j*I[1])
  
  Nums = list(filter(is_prime,Nums))

  if len(Nums) == 3:
    Result.append(Nums)

Result