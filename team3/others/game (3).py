#此程式是猜數字遊戲透過猜拳來決定玩家猜的先後順序。
import random
import os

def GameCheck(player): #猜拳防呆
    haven = False #true表示輸入了"剪刀""石頭""布"以外的字串
    if player!="剪刀":
        if player!="石頭":
            if player!="布": #輸入"剪刀""石頭""布"以外的字串
                haven = True #表示輸入了"剪刀""石頭""布"以外的字串
            else:
                haven = False
        else:
            haven = False
    else:
        haven = False 

    while haven: #表示輸入了"剪刀""石頭""布"以外的字串
        print("沒有此招(@A@)請再輸入一次\n") 
        player = input("請輸入你想出的招(剪刀、石頭、布): ")
        if player!="剪刀":
            if player!="石頭":
                if player!="布": #輸入"剪刀""石頭""布"以外的字串
                    haven = True #表示輸入了"剪刀""石頭""布"以外的字串
                else:
                    haven = False
            else:
                haven = False
        else:
            haven = False
    
    return player

def GameCompare(player, computer, playpoint, compoint): #比賽猜拳
    if player==computer: #兩個人出的一樣
        print("平手_(:3 」∠ )_") 
    elif player=="剪刀": #玩家出剪刀
        if computer=="石頭": #電腦出石頭
            print("玩家二號贏了(´ﾟдﾟ`)") 
            compoint+=1 #對手(電腦)的分數加1
        else: #電腦出布
            print("玩家一號贏了(ﾉ>ω<)ﾉ")
            playpoint+=1 #玩家的分數加1
    elif player=="石頭": #玩家出石頭
        if computer=="布": #電腦出布
            print("玩家二號贏了(´ﾟдﾟ`)")
            compoint+=1 #對手(電腦)的分數加1
        else: #電腦出剪刀
            print("玩家一號贏了(ﾉ>ω<)ﾉ")
            playpoint+=1 #玩家的分數加1
    else: #玩家出布
        if computer=="剪刀": #電腦出剪刀
            print("玩家二號贏了(´ﾟдﾟ`)")
            compoint+=1 #對手(電腦)的分數加1
        else: #電腦出石頭
            print("玩家一號贏了(ﾉ>ω<)ﾉ")
            playpoint+=1 #玩家的分數加1 
    
    return playpoint, compoint

choices = ["剪刀","石頭","布"] #能出的招式
bigorsmall = ["大","小"] #能押的注
isnotover = True #true表示遊戲還沒有結束
isnotRight = True #true表示押注大小還沒有結束
compoint = 0 #對手(電腦)的分數
playpoint = 0 #玩家的分數
commoney = 0 #對手(電腦)的本金
playmoney = 0 #玩家的本金
comtrymoney = 0 #對手(電腦)的下注金額
playtrymoney = 0 #玩家的下注金額
round = 0 #進行幾輪 
num = 0 #隨機抽取一個數字
print("\n說明:這是一個簡易的猜數字遊戲，首先輸入總共有幾位(1-2位)玩家，不用擔心自己太邊緣，會由我們的電腦哥哥姊姊貼心成為您的第一位朋友喔 (੭ु´ ᐜ `)੭ु⁾⁾")
print("再來請各位玩家進行猜拳，贏的人有1500的本金，並且先選擇押大、小，輸的人有1250的本金，並選擇剩下的，數字隨機從1~1000出，1<=數字<=500為小，501<=數字<=1000為大")
print("接著輸入下注金額，預設賠率為2倍，贏的人獲得2倍的金額，輸的人扣除2倍的金額，直到有人先達標2000元，或是本金花光光，遊戲就結束囉(=´ω`=)")
print("貼心小提醒: 如果對手為電腦，下注金額與您的下注金額相同喔，顆顆:3\n")
print("--------現在遊戲開始--------\n")
gameplayer = input("請輸入1-2位玩家: ") #玩家數

while isnotover: #來判斷遊戲有沒有結束
    player = input("請輸入玩家一號想出的招(剪刀、石頭、布): ")
    player = GameCheck(player) #猜拳防呆

    if gameplayer == "1": #一位玩家
         computer=random.choice(choices) #隨機選擇剪刀、石頭、布
    elif gameplayer == "2":#兩位玩家
        computer = input("請輸入玩家二號想出的招(剪刀、石頭、布): ")
        computer = GameCheck(computer) #猜拳防呆
    else:#輸入了"1""2"以外的字串
        print("妹子阿不提供此人數喔(@A@)請再輸入一次\n")   
        while gameplayer != "1" and gameplayer != "2":
            gameplayer = input("請輸入1-2位玩家: ") 

    print("\n"+"玩家一號出的是: "+player)
    print("\n"+"玩家二號/電腦哥哥出的是: "+computer+"\n")
    
    (playpoint, compoint) = GameCompare(player, computer, playpoint, compoint) #比賽猜拳

    num = int(random.randrange(1,1001)) #隨機選擇數字1-1000

    while playpoint == compoint: #雙方平手
        player = input("請輸入玩家一號想出的招(剪刀、石頭、布): ")
        player = GameCheck(player) #猜拳防呆
        
        if gameplayer == "1": #一位玩家
            computer=random.choice(choices) #隨機選擇剪刀、石頭、布
        else:#兩位玩家
            computer = input("請輸入玩家二號想出的招(剪刀、石頭、布): ")
            computer = GameCheck(computer) #猜拳防呆

        print("\n"+"玩家一號出的是: "+player)
        print("\n"+"玩家二號/電腦哥哥出的是: "+computer+"\n")
        (playpoint, compoint) = GameCompare(player, computer, playpoint, compoint) #比賽猜拳

    if playpoint > compoint: #玩家猜拳贏
        if round == 0: #第一輪
            commoney = 1250 #對手(電腦)的本金
            playmoney = 1500 #玩家的本金
        playchoice = input("\n請玩家一號選擇押注(大、小): ") #玩家押注
        if playchoice == "大": #玩家押大
            comchoice = "小"
        elif playchoice == "小": #玩家押小
            comchoice = "大"
        else: #輸入了"大""小"以外的字串
            while isnotRight: #表示輸入了"大""小"以外的字串
                print("寶貝你輸錯了喔＼(●´ϖ`●)／請再輸入一次\n") 
                playchoice = input("請玩家一號選擇押注(大、小): ")
                if playchoice == "大": #玩家押大
                    comchoice = "小"
                    isnotRight = False
                elif playchoice == "小": #玩家押小
                    comchoice = "大"  
                    isnotRight = False            
                else:
                    isnotRight = True #表示輸入了"大""小"以外的字串

    else: #電腦猜拳贏
        if round == 0: #第一輪
            commoney = 1500 #對手(電腦)的本金
            playmoney = 1250 #玩家的本金

        if gameplayer == "1": #一位玩家
            comchoice = random.choice(bigorsmall) #隨機選擇大、小
        else: #兩位玩家
            comchoice = input("請玩家二號選擇押注(大、小): ")

        if comchoice == "大": #電腦押大
            playchoice = "小"
        elif comchoice == "小": #電腦押小
            playchoice = "大"
        else: #輸入了"大""小"以外的字串
            while isnotRight:
                print("寶貝你輸錯了喔＼(●´ϖ`●)／請再輸入一次\n") 
                comchoice = input("請玩家二號選擇押注(大、小): ")
                if comchoice == "大": #玩家押大
                    playchoice = "小"
                    isnotRight = False
                elif comchoice == "小": #玩家押小
                    playchoice = "大"  
                    isnotRight = False            
                else:
                    isnotRight = True #表示輸入了"大""小"以外的字串

    isnotRight = True #true表示押注大小還沒有結束
    playpoint = 0 
    compoint = 0 
    playtrymoney = int(input("請玩家一號選擇下注金額: ")) #玩家的下注金額
    if gameplayer == "1":
        comtrymoney = playtrymoney #對手(電腦)的下注金額
    else:
        comtrymoney = int(input("請玩家二號選擇下注金額: ")) #對手(電腦)的下注金額

    if num >= 501 and num <= 1000: #下注大為贏
        if playchoice == "大":
            playmoney = playmoney + playtrymoney*2
            commoney = commoney - comtrymoney*2
        else:
            playmoney = playmoney - playtrymoney*2
            commoney = commoney + comtrymoney*2
    else: #下注小為贏
        if playchoice == "小":
            playmoney = playmoney + playtrymoney*2
            commoney = commoney - comtrymoney*2
        else:
            playmoney = playmoney - playtrymoney*2
            commoney = commoney + comtrymoney*2

    round+=1
    print("\n" + "********隨機數字為: ", num, "********\n")  
    print("\n" + "********玩家一號注",playchoice,", 玩家二號注",comchoice,"********\n")  
    print("\n" + "********玩家一號的下注金額為:",playtrymoney,", 玩家二號的下注金額為 :",comtrymoney,"********\n")
    print("\n" + "********目前比分為:",playmoney,"(玩家一號的本金), ",commoney,"(玩家二號的本金)********\n")

    if playmoney <= 0:
        if commoney <= 0:
            if playmoney > commoney:
                print("========遊戲結束========\n玩家一號贏了這場遊戲ヽ(✿ ﾟ▽ﾟ)ノ")
            else:
                print("========遊戲結束========\n玩家一號輸給了玩家二號 (☍﹏⁰) (╥﹏╥)")  
        else:
            print("========遊戲結束========\n玩家一號輸給了玩家二號 (☍﹏⁰) (╥﹏╥)")  
        isnotover = False #迴圈結束=遊戲結束
    elif playmoney >= 2000:
        if commoney >= 2000:
            if playmoney > commoney:
                print("========遊戲結束========\n玩家一號贏了這場遊戲ヽ(✿ ﾟ▽ﾟ)ノ")
            else:
                print("========遊戲結束========\n玩家一號輸給了玩家二號 (☍﹏⁰) (╥﹏╥)")  
        else:
            print("========遊戲結束========\n玩家一號贏了這場遊戲ヽ(✿ ﾟ▽ﾟ)ノ")
        isnotover = False #迴圈結束=遊戲結束
    elif commoney <= 0:
        print("========遊戲結束========\n玩家一號贏了這場遊戲ヽ(✿ ﾟ▽ﾟ)ノ")  
        isnotover = False #迴圈結束=遊戲結束
    elif commoney >= 2000:
        print("========遊戲結束========\n玩家一號輸給了玩家二號 (☍﹏⁰) (╥﹏╥)")
        isnotover = False #迴圈結束=遊戲結束
    else: #還沒有人獲勝
        isnotover = True  #迴圈繼續   
    
os.system("pause")
