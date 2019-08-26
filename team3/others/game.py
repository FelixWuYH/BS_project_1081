#此程式是個猜拳遊戲
import random
import os
choices = ["剪刀","石頭","布"] #能出的招式
card = "0"##用來查看玩家是否使用功能卡
isnotover = True #true表示遊戲還沒有結束
compuHP = 100 ##對手(電腦)的血量
playHP = 100 ##玩家的血量
subtract = 0 ##扣去多少血量
shield = False ##用來判別功能5的盾牌是否使用
iscard = False##用來判斷是否使用功能卡的輸入是否正確
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

os.system("pause")
  
  
