# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 09:34:49 2019

@author: Administrator
"""

#组成牌组
import random
card = []
suit = ['C','D','E','F']        #代表花色
number = ['A','2','3','4','5','6','7','8','9','10','j','Q','K']  #牌号
for i in range(len(suit)):
    for j in range(len(number)):
        card.append(suit[i]+number[j])
card.append('rad_Joker')
card.append('Black_Joker')
random.shuffle(card)
leave_card = card[-3:]
card = card[:-3]           #拿出三张牌后的牌组
#开始发牌
#第一种发牌方式
#p1 = card[::3]
#p2 = card[1::3]
#p3 = card[2::3]
#print(leave_card)
#print(p1)
#print(p2)
#print(p3)

#第二种发牌方式
p1 = []
p2 = []
p3 = []
while len(card) > 0:
    p1.append(card.pop())
    p2.append(card.pop())
    p3.append(card.pop())
print(leave_card)
print(p1)
print(p2)
print(p3)