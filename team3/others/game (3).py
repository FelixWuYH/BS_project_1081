#此程式是個猜拳遊戲
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
bigorsmall = ["大","小"] ###能押的注
game = 0 #選擇哪一個遊戲
card = "0"##用來查看玩家是否使用功能卡
isnotover = True #true表示遊戲還沒有結束
isnotRight = True ###true表示押注大小還沒有結束
compuHP = 100 ##對手(電腦)的血量
playHP = 100 ##玩家的血量
subtract = 0 ##扣去多少血量
shield = False ##用來判別功能5的盾牌是否使用
iscard = False##用來判斷是否使用功能卡的輸入是否正確
compoint = 0 ###對手(電腦)的分數
playpoint = 0 ###玩家的分數
commoney = 0 ###對手(電腦)的本金
playmoney = 0 ###玩家的本金
comtrymoney = 0 ###對手(電腦)的下注金額
playtrymoney = 0 ###玩家的下注金額
round = 0 ###進行幾輪 
num = 0 ###隨機抽取一個數字

game = int(input("親~這款遊戲有兩種模式可以選，請輸入 1 or 2 ~\n"))
while game != 1 and game != 2: ###遊戲模式防呆
    game = int(input("大大~沒有這模式阿!!!請重新輸入!!!\n"))

if game == 1: #第一款模式

    print("說明:這是一個靠運氣的猜拳遊戲~~\n")
    print("有功能卡可以進行使用，可能可以會有奇妙的功能唷~~~嘿嘿\n")
    print("--------現在遊戲開始--------\n")
    while isnotover: #來判斷遊戲有沒有結束
        card = input("是否使用功能卡: ")
        if card != "是":
            if card != "否":
                while iscard != True:##判斷功能卡輸入是否正確
                    print("輸入錯誤囉!請輸入 是 or 否")
                    card = input("是否使用功能卡: ")
                    if card == "是":
                        iscard = True
                    elif card == "否":
                        iscard = False
                    break             
            else:
                iscard = False
        else:
            iscard = True

        if iscard == True:##功能卡輸入"是"
            carduse = random.randint(1,5)##從功能1-5中隨機選擇
            if carduse == 1:##功能1，玩家HP直接歸0
                playHP = 0 
                print( "賜你自盡!!!!!!!!!")
                print("\n" + "********目前血量為:",playHP,"(你的分數) :",compuHP,"(對手的分數)********\n")
                print("========遊戲結束========\n你輸給了對手 (☍﹏⁰) (╥﹏╥)")
                break
            if carduse == 2:##功能2，玩家與電腦血量交換
                temp = playHP
                playHP = compuHP
                compuHP = temp
                print( "玩家與對手的血量進行交換 ~ ~ ~")
                print("\n" + "********目前血量為:",playHP,"(你的分數) :",compuHP,"(對手的分數)********\n")
            if carduse == 3:##功能3，玩家補血30
                playHP = playHP + 30
                print( "恭喜玩家進行補血30!!") 
                print("\n" + "********目前血量為:",playHP,"(你的分數) :",compuHP,"(對手的分數)********\n")
            if carduse == 4:##功能4，玩家補血40
                playHP = playHP - 30
                print( "歐歐~玩家扣除血量30!!")
                print("\n" + "********目前血量為:",playHP,"(你的分數) :",compuHP,"(對手的分數)********\n")      
                if playHP <= 0:##如果玩家血量小於等於0，則宣告遊戲結束
                    print("========遊戲結束========\n你輸給了對手 (☍﹏⁰) (╥﹏╥)") 
                    print("\n" + "********目前血量為:",playHP,"(你的分數) :",compuHP,"(對手的分數)********\n")
                    break
            if carduse == 5:##功能5，玩家獲得在下輪一次不扣血機會
                print( "恭喜玩家在下個回合獲得盾牌!!")
                shield = True
        else:
            shield = False
  
        computer=random.choice(choices) #隨機選擇剪刀、石頭、布
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

        print("\n"+"你出的是: "+player)
        print("\n"+"對手出的是: "+computer+"\n")
        if player==computer: #兩個人出的一樣
            print("平手_(:3 」∠ )_") 
        elif player=="剪刀": #玩家出剪刀
            if computer=="石頭": #電腦出石頭         
                if shield == True:
                    print("盾牌守護")
                else:
                    subtract = random.randint(40,100)##隨機扣除血量
                    playHP = playHP - subtract ##玩家目前HP減去扣去的血量
                    print( "玩家扣除", subtract, "HP")
                    print("玩家剩餘 ",playHP," HP") 
            else: #電腦出布
                subtract = random.randint(40,100)##隨機扣除血量
                compuHP = compuHP - subtract ##電腦目前HP減去扣去的血量
                print( "對手扣除", subtract, "HP")
                print("對手剩餘 ",compuHP," HP") 
        elif player=="石頭": #玩家出石頭
            if computer=="布": #電腦出布
                if shield == True:
                    print("盾牌守護")
                else:
                    subtract = random.randint(40,100)##隨機扣除血量
                    playHP = playHP - subtract ##玩家目前HP減去扣去的血量
                    print( "玩家扣除", subtract, "HP")
                    print("玩家剩餘 ", playHP ," HP") 
            else: #電腦出剪刀
                subtract = random.randint(40,100)##隨機扣除血量
                compuHP = compuHP - subtract ##電腦目前HP減去扣去的血量
                print( "對手扣除", subtract, "HP")
                print("對手剩餘 ",compuHP, " HP") 
        else: #玩家出布
            if computer=="剪刀": #電腦出剪刀
                if shield == True:
                    print("盾牌守護")
                else:
                    subtract = random.randint(40,100)##隨機扣除血量
                    playHP = playHP - subtract ##玩家目前HP減去扣去的血量
                    print( "玩家扣除", subtract, "HP")
                    print("玩家剩餘 ", playHP, " HP") 
            else: #電腦出石頭
                subtract = random.randint(40,100)##隨機扣除血量
                compuHP = compuHP - subtract ##電腦目前HP減去扣去的血量
                print( "對手扣除", subtract, "HP")
                print("對手剩餘 ",compuHP," HP")
        if playHP <= 0: ##玩家血量小於等於0 
            print("\n" + "********目前血量為:",playHP,"(你的分數) :",compuHP,"(對手的分數)********\n")
            isnotover = False #迴圈結束=遊戲結束
            print("========遊戲結束========\n你輸給了對手 (☍﹏⁰) (╥﹏╥)") 
        elif compuHP <= 0: ##電腦血量小於等於0
            print("\n" + "********目前血量為:",playHP,"(你的分數) :",compuHP,"(對手的分數)********\n")
            isnotover = False #迴圈結束=遊戲結束
            print("========遊戲結束========\n你贏了這場遊戲ヽ(✿ ﾟ▽ﾟ)ノ")  
        else: #還沒有人獲勝
            print("\n" + "********目前血量為:",playHP,"(你的分數) :",compuHP,"(對手的分數)********\n")
            isnotover = True  #迴圈繼續
        shield =False
else:  #第二款模式
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
