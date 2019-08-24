#此程式是個三戰兩勝的猜拳遊戲
import random
import os
choices = ["剪刀","石頭","布"] #能出的招式
isnotover = True #true表示遊戲還沒有結束
compoint = 0 #對手(電腦)的分數
playpoint = 0 #玩家的分數
print("說明:這是一個簡易的猜拳遊戲，採三戰兩勝制~~\n")
print("--------現在遊戲開始--------\n")
while isnotover: #來判斷遊戲有沒有結束
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
         print("對手贏了(´ﾟдﾟ`)") 
         compoint+=1 #對手(電腦)的分數加1
     else: #電腦出布
         print("你贏了(ﾉ>ω<)ﾉ")
         playpoint+=1 #玩家的分數加1
  elif player=="石頭": #玩家出石頭
     if computer=="布": #電腦出布
         print("對手贏了(´ﾟдﾟ`)")
         compoint+=1 #對手(電腦)的分數加1
     else: #電腦出剪刀
         print("你贏了(ﾉ>ω<)ﾉ")
         playpoint+=1 #玩家的分數加1
  else: #玩家出布
     if computer=="剪刀": #電腦出剪刀
         print("對手贏了(´ﾟдﾟ`)")
         compoint+=1 #對手(電腦)的分數加1
     else: #電腦出石頭
         print("你贏了(ﾉ>ω<)ﾉ")
         playpoint+=1 #玩家的分數加1
  print("\n" + "********目前比分為:",playpoint,"(你的分數) :",compoint,"(對手的分數)********\n")
  if playpoint==2: #玩家獲得兩分
     isnotover = False #迴圈結束=遊戲結束
     print("========遊戲結束========\n你贏了這場遊戲ヽ(✿ ﾟ▽ﾟ)ノ") 
  elif compoint==2: #對手(電腦)獲得兩分
     isnotover = False #迴圈結束=遊戲結束
     print("========遊戲結束========\n你輸給了對手 (☍﹏⁰) (╥﹏╥)")  
  else: #還沒有人獲勝
     isnotover = True  #迴圈繼續   

os.system("pause")
  
