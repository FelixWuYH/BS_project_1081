#資訊二乙 10627214 黃欣誼 簡易撲克


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

def straight(card):#順子的判別
    look = card[0]#設一個look來判斷是否連續
    count = 1 #用來跑回圈
    while count < 5:#當查看完5張牌的時候離開
        look = look + 1
        if look != card[count]:#判別是否有連號
            return False,0#只要有一個沒有連號就回傳false，此函式結束
        count += 1
    return True,card[4]#沒有回傳false，表示card是一個順子

def fourkind(card):#四條的判別(由於我的card是經過排序的，所以只有兩種情況)
    
    count = 0 #用來計數
    look = card[0]
    if look == card[1]:#第一種情況，我的第一張牌跟第二張一樣
        count = 2#從第三張牌開始比較
        while count < 4:#比到第四張牌停止
            if look != card[count]:#只要有一張牌跟我的第一張不一樣
                return False,0#回傳false，跳出函式
          
            count += 1
        
        return True,card[0]#是第一種情況，但是還沒跳出函式
    else: #不是第一種情況   
        look = card[1]
        if look == card[2]:#第二種情況，第二張牌跟第三張一樣
            count = 3#從第四張開始比較
            while count < 5:#比到第五張停止
                if look != card[count]:#只要有一張牌跟我的第一張不一樣
                    return False,0#回傳false，跳出函式
                count += 1
            return True,card[1]#是第二種情況，但是還沒跳出函式

    return False,0#不是以上兩種情況

            
def threekind(card):#三條的判別，因為有經過排序，所以是三條的有三種情況
    look = card[0]
    if look == card[1]:#我的第一張牌跟第二張牌一樣
        if look == card[2]:#且跟我的第三張牌一樣
            return True,card[0]#就直接回傳，並跳出函式
    look = card[1]
    if look == card[2]:#我的第二張牌跟第三張牌一樣
        if look == card[3]:#且跟第四張牌一樣
            return True,card[1]#就直接回傳，並跳出函式
    look = card[2]
    if look == card[3]:#我的第三張牌跟第四張牌一樣
        if look == card[4]:#且跟第五張牌一樣
            return True,card[2]#就直接回傳，並跳出函式
    return False,0#此時還沒有回傳，表示card中沒有三條

def onepair(card):#一對的判別
    look = 0#用來計數
    count = 0#用來計數
    while count < 5:  #五張牌都比較到  
        look = count + 1#為了不重複比較
        while look < 5:#五張牌都比較到
            if card[count] == card[look]:#找到一樣數字的牌
                return True,card[count]#回傳並跳出迴圈
            look += 1
        count += 1
    return False,0#此時還沒有回傳，表示card中沒有一對

def fullhouse(card):#葫蘆的判別
    look = card[0]
    if look == card[1]:#我的第一張牌跟第二張牌一樣
        if look == card[2]:#且跟我的第三張牌一樣
            if card[3] == card[4]:#且我的第四張牌跟第五張一樣
                return True,card[0]#就直接回傳，並跳出函式
    
    look = card[2]
    if look == card[3]:#我的第三張牌跟第四張牌一樣
        if look == card[4]:#且跟第五張牌一樣
            if card[0] == card[1]:#且弟一張牌跟第二張一樣
                return True,card[2]#就直接回傳，並跳出函式
    return False,0#此時還沒有回傳，表示card中沒有葫蘆

def twopair(card):#一對的判別
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
                           return True,card[count]#回傳並跳出迴圈
                    num += 1

            look += 1
        count += 1
    return False,0#此時還沒有回傳，表示card中沒有一對

def flush(flower): #同花的判別
    look = flower[0]  
    count = 1 
    while count < 5:
        if look != flower[count]:#有任何一張跟第一張牌的花色一樣
            return False,0#回傳並跳出函式
        count = count + 1
    return True,flower[4]#五張牌花色都一樣

def straightflush(card,flower):#同花順的判別
    if flush(flower) == True:#判斷是否是同花
        if straight(card) == True:#判斷是否是順子
            return True,card[4]#回傳並跳出函式
    return False,0#不是同花順，回傳並跳出


def sort(card1,flower1):
    copy = 0 #用來跑迴圈
    count = 1 #用來跑迴圈
    while copy < 5: #排序由小排到大
        count = copy + 1
        while count < 5:
            if card1[copy] > card1[count]:
                temp1 = flower1[copy]
                temp = card1[copy]
                flower1[copy] = flower1[count]
                card1[copy] = card1[count]
                flower1[count] = temp1
                card1[count] = temp   
    
               
            count += 1 
    
        copy += 1 
    return card1,flower1

def typecard(card,flower):#幫牌型大小制定階級
    look, temp = straightflush(card,flower)
    if  look == True :#是否是同花順
        print ("同花順")
        return  8

    look,temp = fourkind(card)
    if look == True :#是否是四條
        
        print("四條")
        return  7

    look,temp = fullhouse(card)#是否是葫蘆
    if look == True :
        print("葫蘆")
        return  6
    
    look,temp = flush(flower)#是否是同花
    if look == True :
        print("同花")
        return  5

    look,temp = straight(card)#是否是順子
    if look == True :
        print("順子")
        return  4
    
    look,temp = threekind(card)#是否是三條
    if look == True :
        print( "三條")
        return  3

    look,temp = twopair(card)#是否是兩對
    if look == True :
        print("兩對")
        return  2 
    
    look,temp =  onepair(card)#是否是一對
    if look == True :
        print("一對")
        return  1
    
    print("散牌")
    return 0

def findbig(level,big,card):#找出最大的排
    if level == 8:#同花順，最大的牌是第五張
        big = card[4]
        return big
    elif level == 7:#四條
        temp = fourkind(card)
        big = temp[1]
        return big
    elif level == 6:#葫蘆
        temp = fullhouse(card)
        big = temp[1]
        return big
    elif level == 5:#同花
        big = card[4]
        return big
    elif level == 4:#順子
        big = card[4]
        return big
    elif level == 3:#三條
        temp = threekind(card)
        big = temp[1]
        return big
    elif level == 2:#兩對
        temp = fullhouse(card)
        big = temp[1]
        return big
    elif level == 1:#一對
        temp = fullhouse(card)
        big = temp[1]
        return big
    else:#散牌
        big = card[4]
        return big

print("簡易撲克要開始囉(=> _ <=)")
print("花色有S,H,D,C，數字是A,2-10,J,Q,K,請用ex.SA這種格式進行輸入呦~")
onecard = input("請輸入第一個玩家的第1張牌(ex.H5): ")#輸入第一個玩家的第1張牌
twocard = input("請輸入第一個玩家的第2張牌(ex.H5): ")#輸入第一個玩家的第2張牌
threecard = input("請輸入第一個玩家的第3張牌(ex.H5): ")#輸入第一個玩家的第3張牌
fourcard = input("請輸入第一個玩家的第4張牌(ex.H5): ")#輸入第一個玩家的第4張牌
fivecard = input("請輸入第一個玩家的第五張牌(ex.H5): ")#輸入第一個玩家的第5張牌
if "0" in onecard:
    one = onecard[1]+onecard[2]#第1張牌的數字
else:
    one = onecard[1]#第1張牌的數字
if "0" in twocard:
    two = twocard[1]+twocard[2]#第2張牌的數字
else:
    two = twocard[1]#第2張牌的數字
if "0" in threecard:
    three = threecard[1]+threecard[2]#第3張牌的數字
else:
    three = threecard[1]#第3張牌的數字
if "0" in fourcard:
    four = fourcard[1]+fourcard[2]#第4張牌的數字
else:
    four  = fourcard[1]#第4張牌的數字

if "0" in fivecard:
    five = fivecard[1]+fivecard[2]#第5張牌的數字
else:
    five  = fivecard[1]#第5張牌的數字

playercard1 = transint(one)#將字串轉為數字
playercard2 = transint(two)#將字串轉為數字   
playercard3 = transint(three)#將字串轉為數字 
playercard4 = transint(four)#將字串轉為數字  
playercard5 = transint(five)#將字串轉為數字
flower1 = [onecard[0],twocard[0],threecard[0],fourcard[0],fivecard[0]]#第一個玩家五張牌的花色
card1 = [playercard1,playercard2,playercard3,playercard4,playercard5]#第一個玩家我的五張牌的數字
card1, flower1 = sort(card1,flower1)#第一個玩家牌的排序

onecard = input("請輸入第二個玩家的第1張牌(ex.H5): ")#輸入第二個玩家的第1張牌
twocard = input("請輸入第二個玩家的第2張牌(ex.H5): ")#輸入第二個玩家的第2張牌
threecard = input("請輸入第二個玩家的第3張牌(ex.H5): ")#輸入第二個玩家的第3張牌
fourcard = input("請輸入第二個玩家的第4張牌(ex.H5):")#輸入第二個玩家的第4張牌
fivecard = input("請輸入第二個玩家的第五張牌(ex.H5):")#輸入第二個玩家的第5張牌

if "0" in onecard:
    one = onecard[1]+onecard[2]#第1張牌的數字
else:
    one = onecard[1]#第1張牌的數字
if "0" in twocard:
    two = twocard[1]+twocard[2]#第2張牌的數字
else:
    two = twocard[1]#第2張牌的數字
if "0" in threecard:
    three = threecard[1]+threecard[2]#第4張牌的數字
else:
    three = threecard[1]#第3張牌的數字
if "0" in fourcard:
    four = fourcard[1]+fourcard[2]#第4張牌的數字
else:
    four = fourcard[1]#第4牌的數字

if "0" in fivecard:
    five = fivecard[1]+fivecard[2]#第5張牌的數字
else:
    five  = fivecard[1]#第5張牌的數字

playercard1 = transint(one)#將字串轉為數字
playercard2 = transint(two)#將字串轉為數字   
playercard3 = transint(three)#將字串轉為數字 
playercard4 = transint(four)#將字串轉為數字  
playercard5 = transint(five)#將字串轉為數字
flower2 = [onecard[0],twocard[0],threecard[0],fourcard[0],fivecard[0]]#第一個玩家五張牌的花色
card2 = [playercard1,playercard2,playercard3,playercard4,playercard5]#第一個玩家我的五張牌的數字
card2,flower2 = sort(card2,flower2)#第二個玩家牌的排序

level1 = typecard(card1,flower1)#第一個玩家牌的大小
print(" vs ")
level2 = typecard(card2,flower2)#第二個玩家牌的大小

if level1 > level2 :#當第一個玩家的牌比第二個大
    print("恭喜第一個玩家贏得牌局(>_<)")
elif level1 < level2 :#當第二個玩家的牌比第一個大
    print( "恭喜第二個玩家贏得牌局(>_<)")
else:
    big1 = card1[4]
    big2 = card2[4]
    big1 = findbig(level1,big1,card1)
    big2 = findbig(level2,big2,card2)
    if big1 > big2:#數字部分的比較
        print("恭喜第一個玩家贏得牌局(>_<)")
    elif big1 < big2:
        print( "恭喜第二個玩家贏得牌局(>_<)")
    else:
        print( "恭喜平手(>_<)")
print("簡易撲克結束囉~~謝謝你的使用OuO")



