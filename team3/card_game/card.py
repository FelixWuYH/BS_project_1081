#資訊二乙 10627214 黃欣誼 簡易撲克

import random
import os
def transint(one):#將牌轉換為int
    if one == "A":#將A轉換成數字1，方便之後判別牌型
        one = int(1)
    elif one == "J":#將J轉換成數字11，方便之後判別牌型
        one = int(11)
    elif one =="Q":#將K轉換成數字12，方便之後判別牌型
        one = int(12)
    elif one =="K":#將K轉換成數字13，方便之後判別牌型
        one = int(13)
    else:
        one = int(one)#將字串轉換成數字，方便之後判別牌型
    return one #回傳

def straight(card,flower):#順子的判別
    look = card[0]#設一個look來判斷是否連續
    count = 1 #用來跑回圈
    while count < 5:#當查看完5張牌的時候離開
        look = look + 1
        if look != card[count]:#判別是否有連號
            return False,0,0#只要有一個沒有連號就回傳false，此函式結束
        count += 1
    return True,card[4],flower[4]#沒有回傳false，表示card是一個順子

def fourkind(card,flower):#四條的判別(由於我的card是經過排序的，所以只有兩種情況)
    
    count = 0 #用來計數
    look = card[0]
    if look == card[1]:#第一種情況，我的第一張牌跟第二張一樣
        count = 2#從第三張牌開始比較
        while count < 4:#比到第四張牌停止
            if look != card[count]:#只要有一張牌跟我的第一張不一樣
                return False,0,0#回傳false，跳出函式
          
            count += 1
        
        return True,card[3],flower[3]#是第一種情況，但是還沒跳出函式
    else: #不是第一種情況   
        look = card[1]
        if look == card[2]:#第二種情況，第二張牌跟第三張一樣
            count = 3#從第四張開始比較
            while count < 5:#比到第五張停止
                if look != card[count]:#只要有一張牌跟我的第一張不一樣
                    return False,0,0#回傳false，跳出函式
                count += 1
            return True,card[4],flower[4]#是第二種情況，但是還沒跳出函式

    return False,0,0#不是以上兩種情況

            
def threekind(card,flower):#三條的判別，因為有經過排序，所以是三條的有三種情況
    look = card[0]
    if look == card[1]:#我的第一張牌跟第二張牌一樣
        if look == card[2]:#且跟我的第三張牌一樣
            return True,card[2],flower[2]#就直接回傳，並跳出函式
    look = card[1]
    if look == card[2]:#我的第二張牌跟第三張牌一樣
        if look == card[3]:#且跟第四張牌一樣
            return True,card[3],flower[3]#就直接回傳，並跳出函式
    look = card[2]
    if look == card[3]:#我的第三張牌跟第四張牌一樣
        if look == card[4]:#且跟第五張牌一樣
            return True,card[4],flower[4]#就直接回傳，並跳出函式
    return False,0,0#此時還沒有回傳，表示card中沒有三條

def onepair(card,flower):#一對的判別
    look = 0#用來計數
    count = 0#用來計數
    while count < 5:  #五張牌都比較到  
        look = count + 1#為了不重複比較
        while look < 5:#五張牌都比較到
            if card[count] == card[look]:#找到一樣數字的牌
                return True,card[look],flower[look]#回傳並跳出迴圈
            look += 1
        count += 1
    return False,0,0#此時還沒有回傳，表示card中沒有一對

def fullhouse(card,flower):#葫蘆的判別
    look = card[0]
    if look == card[1]:#我的第一張牌跟第二張牌一樣
        if look == card[2]:#且跟我的第三張牌一樣
            if card[3] == card[4]:#且我的第四張牌跟第五張一樣
                return True,card[2],flower[2]#就直接回傳，並跳出函式
    
    look = card[2]
    if look == card[3]:#我的第三張牌跟第四張牌一樣
        if look == card[4]:#且跟第五張牌一樣
            if card[0] == card[1]:#且弟一張牌跟第二張一樣
                return True,card[4],flower[4]#就直接回傳，並跳出函式
    return False,0,0#此時還沒有回傳，表示card中沒有葫蘆

def twopair(card,flower):#一對的判別
    look = 0#用來計數
    count = 0#用來計數
    num = 0 
    while count < 5:  #五張牌都比較到  
        look = count + 1#為了不重複比較
        while look < 5:#五張牌都比較到
            if card[count] == card[look]:#找到一樣數字的牌
                num = look + 1
                while num < 5:
                    if num+1 < 5:#防止num+1超出範圍
                        if card[num] == card[num+1]:#找到另外一對
                           return True,card[num+1],flower[num+1]#回傳並跳出迴圈
                    num += 1

            look += 1
        count += 1
    return False,0,0#此時還沒有回傳，表示card中沒有一對

def flush(flower,card): #同花的判別
    look = flower[0]  
    count = 1 
    while count < 5:
        if look != flower[count]:#有任何一張跟第一張牌的花色一樣
            return False,0,0#回傳並跳出函式
        count = count + 1
    return True,card[4],flower[4]#五張牌花色都一樣

def straightflush(card,flower):#同花順的判別
    if flush(flower,card) == True:#判斷是否是同花
        if straight(card,flower) == True:#判斷是否是順子
            return True,card[4],flower[4]#回傳並跳出函式
    return False,0,0#不是同花順，回傳並跳出



def typecard(card,flower):#幫牌型大小制定階級
    look, temp, fl = straightflush(card,flower)
    if  look == True :#是否是同花順
        print ("同花順")
        return  8,temp,fl

    look, temp, fl = fourkind(card,flower)
    if look == True :#是否是四條
        
        print("四條")
        return  7,temp,fl

    look, temp, fl = fullhouse(card,flower)#是否是葫蘆
    if look == True :
        print("葫蘆")
        return  6,temp,fl
    
    look,temp,fl = flush(flower,card)#是否是同花
    if look == True :
        print("同花")
        return  5,temp,fl

    look,temp,fl = straight(card,flower)#是否是順子
    if look == True :
        print("順子")
        return  4,temp,fl
    
    look,temp,fl = threekind(card,flower)#是否是三條
    if look == True :
        print( "三條")
        return  3,temp,fl

    look,temp,fl = twopair(card,flower)#是否是兩對
    if look == True :
        print("兩對")
        return  2,temp,fl 
    
    look,temp,fl =  onepair(card,flower)#是否是一對
    if look == True :
        print("一對")
        return  1,temp,fl
    
    print("散牌")
    return 0,0,0


pkcard = ["SA","SZ","S3","S4","S5","S6","S7","S8","S9","S10","S11","S12","S13","HA","HZ","H3","H4",
"H5","H6","H7","H8","H9","H10","H11","H12","H13","DA","DZ","D3","D4","D5","D6","D7","D8","D9","D10","D11","D12","D13",
"CA","CZ","C3","C4","C5","C6","C7","C8","C9","C10","C11","C12","C13"] #為了比較好排序把 2變成Z, J Q K變成11 12 13

print("簡易撲克要開始囉(=> _ <=) 系統將會隨機幫你生成牌組")
player1 = random.sample(pkcard,5)
delcard = 0 #用來記數
while delcard < 5: 
   pkcard.remove(player1[delcard]) #把用過的牌從牌疊中刪除
   delcard+=1

player2 = random.sample(pkcard,5)
delcard = 0 
while delcard < 5:
   pkcard.remove(player2[delcard]) #把用過的牌從牌疊中刪除
   delcard+=1

player1.sort() 
delcard = 0
while delcard < 5: #此迴圈用來把原本不對的牌型改回來
   if player1[delcard][1] == "Z":
       copy = player1[delcard][0]
       player1[delcard] = copy+"2"
   elif player1[delcard][1] == "1":
       if player1[delcard][2] == "1":
           copy = player1[delcard][0]
           player1[delcard] = copy+"J"
       elif player1[delcard][2] == "2":
           copy = player1[delcard][0]
           player1[delcard] = copy+"Q"
       elif player1[delcard][2] == "3":
           copy = player1[delcard][0]
           player1[delcard] = copy+"K"

   delcard+=1

print("這是你手中的牌呦~") 
print(player1)
player2.sort()
delcard = 0
while delcard < 5: #此迴圈用來把原本不對的牌型改回來
   if player2[delcard][1] == "Z":
       copy = player2[delcard][0]
       player2[delcard] = copy+"2"
   elif player2[delcard][1] == "1":
       if player2[delcard][2] == "1":
           copy = player2[delcard][0]
           player2[delcard] = copy+"J"
       elif player2[delcard][2] == "2":
           copy = player2[delcard][0]
           player2[delcard] = copy+"Q"
       elif player2[delcard][2] == "3":
           copy = player2[delcard][0]
           player2[delcard] = copy+"K"
           
   delcard+=1

print("這是對手出的牌~~") 
print(player2) 

if len(player1[0]) == 3:
    one = player1[0][1]+player1[0][2]#第1張牌的數字
else:
    one = player1[0][1]#第1張牌的數字
if len(player1[1]) == 3:
    two = player1[1][1]+player1[1][2]#第2張牌的數字
else:
    two = player1[1][1]#第2張牌的數字
if len(player1[2]) == 3:
    three = player1[2][1]+player1[2][2]#第3張牌的數字
else:
    three = player1[2][1]#第3張牌的數字
if len(player1[3]) == 3:
    four = player1[3][1]+player1[3][2]#第4張牌的數字
else:
    four  = player1[3][1]#第4張牌的數字

if len(player1[4]) == 3:
    five = player1[4][1]+player1[4][2]#第5張牌的數字
else:
    five  = player1[4][1]#第5張牌的數字

playercard1 = transint(one)#將字串轉為數字
playercard2 = transint(two)#將字串轉為數字   
playercard3 = transint(three)#將字串轉為數字 
playercard4 = transint(four)#將字串轉為數字  
playercard5 = transint(five)#將字串轉為數字
flower1 = [player1[0][0],player1[1][0],player1[2][0],player1[3][0],player1[4][0]]#第一個玩家五張牌的花色
card1 = [playercard1,playercard2,playercard3,playercard4,playercard5]#第一個玩家我的五張牌的數字


if len(player2[0]) == 3:
    one = player2[0][1]+player2[0][2]#第1張牌的數字
else:
    one = player2[0][1]#第1張牌的數字
if len(player2[1]) == 3:
    two = player2[1][1]+player2[1][2]#第2張牌的數字
else:
    two = player2[1][1]#第2張牌的數字
if len(player2[2]) == 3:
    three = player2[2][1]+player2[2][2]#第3張牌的數字
else:
    three = player2[2][1]#第3張牌的數字
if len(player2[3]) == 3:
    four = player2[3][1]+player2[3][2]#第4張牌的數字
else:
    four  = player2[3][1]#第4張牌的數字

if len(player2[4]) == 3:
    five = player2[4][1]+player2[4][2]#第5張牌的數字
else:
    five  = player2[4][1]#第5張牌的數字


playercard1 = transint(one)#將字串轉為數字
playercard2 = transint(two)#將字串轉為數字   
playercard3 = transint(three)#將字串轉為數字 
playercard4 = transint(four)#將字串轉為數字  
playercard5 = transint(five)#將字串轉為數字
flower2 = [player2[0][0],player2[1][0],player2[2][0],player2[3][0],player2[4][0]]#第一個玩家五張牌的花色
card2 = [playercard1,playercard2,playercard3,playercard4,playercard5]#第一個玩家我的五張牌的數字


level1,temp1,fl1 = typecard(card1,flower1)#第一個玩家牌的大小和最大的那張牌的數字與花色
print(" vs ")
level2,temp2,fl2 = typecard(card2,flower2)#第二個玩家牌的大小和最大的那張牌的數字與花色
print("\n")
if level1 > level2 :#當第一個玩家的牌比第二個大
    print("恭喜你贏得牌局(ﾉ>ω<)ﾉ")
elif level1 < level2 :#當第二個玩家的牌比第一個大
    print( "對手贏得牌局(☍﹏⁰)")
else:
    
    if temp1 > temp2:#數字部分的比較
        print("恭喜你贏得牌局(ﾉ>ω<)ﾉ")
    elif temp1 < temp2:
        print( "對手贏得牌局(☍﹏⁰)")
    else:
        if fl1>fl2:
            print("恭喜你贏得牌局(ﾉ>ω<)ﾉ")  
        else:
            print( "對手贏得牌局(☍﹏⁰)")

print("簡易撲克結束囉~~謝謝你的使用OuO")
os.system("pause")
