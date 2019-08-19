#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

##poker是牌, card是對應的值, again用來判斷是否繼續玩
poker=["A","2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
card={"A":1 or 11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}
again = "y"

##用來加牌
def add(man, times):
    i=0
    while i<times:
        newc=random.choice(poker)
        man.append(newc)
        i=i+1

##用來判斷error massage
def error(cmd, msg):
    while(cmd!="y" and cmd!="n"):
        print("wrong commend")
        input(msg)

    return cmd

##計算總和
def cal(man):
    sum=0
    for i in man:
        if (i!="A"):
            sum = sum+card[i]
    if "A" in man: ###決定A的值
        if(sum<=10):
            sum = sum+11
        else:
            sum = sum+1
    return sum

while(again=="y"):
    player=[]
    robot=[]
    
    ##先各發兩張牌
    add(player, 2)
    add(robot, 2)
    
    ##show 牌
    print(player)
    tmp = error(input("add one card ?(y/n) "), "add one card ?(y/n) ")
    
    ##判斷是否加牌
    while(tmp=="y"):
        add(player, 1)
        print(player)
        
        if(cal(robot)<17):
            print("robot add one card")
            add(robot, 1)
        
        ##檢查是否超過21點, 超過停止遊戲    
        if(cal(player)>21):
            print("boom")
            tmp="n"
        else:
            tmp = error(input("add one card ?(y/n) "), "add one card ?(y/n) ")
        
    while(cal(robot)<17):
        print("robot add one card")
        add(robot, 1)
    
    ##show robot牌
    print("robot cards: ")
    print(robot)
    
    ##判斷輸贏
    if(cal(robot)<22 and cal(player)<22):
        if(cal(robot)<cal(player)):
            print("you win!")
        elif(cal(robot)==cal(player)):
            print("peace~")
        else:
            print("you lose!")
    elif(cal(robot)>=22 and cal(player)<22):
        print("you win!")
    elif(cal(robot)<22 and cal(player)>=22):
        print("you lose!")
    else:
        print("peace~")
        
    again=error(input("play again ?(y/n) "), "play again ?(y/n) ")
    


# In[ ]:




