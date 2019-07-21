# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 22:46:31 2019

@author: Administrator
"""

from random  import randint
total = 0
times = 0
while True:
    choice = input('1.开始游戏；2.退出\n')
    if str(choice) == '1':
        total += 1
        num = randint(1,20)
        while True:
            times += 1
            guess = int(input("请输入你要猜的数："))
            if guess > num:
                print("太大了")
            elif guess < num:
                print("太小了")
            else:
                print("你猜对了！")
                break
    if str(choice) == '2':
        break
    if total > 0:
        print('共猜了%d次，平均%.1f猜中\n'%(total,float(times)/total))
print('游戏结束')