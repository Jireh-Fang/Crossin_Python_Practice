# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 22:46:31 2019

@author: Administrator
"""

'''
猜字游戏：程序随机一个结果，用户通过命令行输入去猜。程序会告诉你猜大了还是小了，知道猜中为止。
附加功能：1.游戏可以反复进行，猜中了之后可以重新开始；2.统计用户猜了几轮，平均几次猜中；
3.限制每轮猜的次数，判定输赢。
'''
from random  import randint
total = 0
times = 0
while True:
    choice = input('1.开始游戏；2.退出\n')
    if str(choice) == '1':
        total += 1
        num = randint(1,20)
        this_time = 0
        while True:
            times += 1
            this_time += 1
            if this_time >= 6:
                print('本轮你已猜5次，失败！')
                break
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
