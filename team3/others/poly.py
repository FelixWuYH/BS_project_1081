import array as ar

def Arrange(num, index): # 整理多項式
    i = 0
    length = len(index)
    while i < length:
        j = i + 1 
        while j < length:

            if index[i] == index[j]:   # 若是指數相同，則係數相加
                num[i] = num[i] + num[j]
                del num[j]
                del index[j]
                j -= 1
                length = len(index)
            
            j += 1
        
        i += 1

    i = 0 
    length = len(num)  
    while i < length:  # 排除係數為零的多項式
        if num[i] == 0:
          del num[i]
          del index[i]
          i -= 1
          length = len(num)
        
        i += 1

    return num, index 

def Sort(num, index): # 由大到小排 序
    i = 0
    length = len(index)
    while i < length:
        j = i + 1 
        while j < length:

            if index[i] < index[j]: # 若後面的比前面小，則交換
                temp1 = num[i]
                temp2 = index[i]
                num[i] = num[j]
                index[i] = index[j]
                num[j] = temp1
                index[j] = temp2 
            
            j += 1
        
        i += 1
   
    return num, index

def Plus(num1, index1, num2, index2): # 多項式相加、相減
    i = 0
    length1 = len(index1) # 第一個多項式長度
    length2 = len(index2)
    exist = False
    while i < length2:
        j = 0 
        while j < length1:

            if index2[i] == index1[j]: # 若找到指數相同，則係數相加
                num1[j] = num1[j] + num2[i]
                exist = True
                break
            
            j += 1

        if j == length1 and exist == False: # 若沒有相同指數，則存進列表
            num1.append(num2[i])
            index1.append(index2[i])

        exist = False
        i += 1   
    
    (num1, index1) = Arrange(num1, index1) # 整理
    (num1, index1) = Sort(num1, index1) # 排列
    return num1, index1
    
def Mul(num1, index1, num2, index2): # 相乘
    i = 0
    ansn = []
    ansi = []
    length1 = len(index1) # 第一個多項式長度
    length2 = len(index2)
    exist = False

    while i < length2:
        j = 0 
        while j < length1:
            ansn.append(num1[j]*num2[i])  # 係數相乘
            ansi.append(index1[j]+index2[i])  # 指數相加
            
            j += 1

        i += 1 
    
    (ansn, ansi) = Arrange(ansn, ansi) # 整理
    (ansn, ansi) = Sort(ansn, ansi) # 排列
    return ansn, ansi

def Print(num, index): # 輸出多項式
    exist = False
    k = 0
    while k < len(num):
        if k != 0:  # 若不為第一個
            if num[k] >= 0: # 若係數為正
                if index[k] == 0:
                    print(" +", num[k], end='')
                elif index[k] == 1:
                    print(" +", num[k], "x", end='')
                else:
                    print(" +", num[k], "x^", index[k], end='')
                
                exist = True
            else:   # 若係數為負
                if index[k] == 0:
                    print(num[k], end='')
                elif index[k] == 1:
                    print(num[k], "x", end='')
                else:
                    print(num[k], "x^", index[k], end='')
                
                exist = True
        else:  # 若為第一個
            if index[0] == 0:
                print(num[k], end='')
            elif index[0] == 1:
                print(num[k], "x", end='')
            else:
                print(num[k], "x^", index[k], end='')

            exist = True
        
        if exist == False:
            print("0", end='')
        
        exist = False
        k += 1
    
    print('\n')



def Create(): # 建立多項式

    a = []
    b = []
    while True:
        c = int(input("係數: "))
        d = int(input("指數: "))
        e = d
        if c != 0 and d >= 0 :  # 若係數不等於零
            a.append(c)
            b.append(d)
        else:
            print("Error!")

        quit = int(input("是否繼續增加係數與指數? Yes:1 / No:0 : "))
        if quit != 1:  
          (a, b) = Arrange(a, b) # 整理
          (a, b) = Sort(a, b) # 排序
          return a, b  




stop = 1 # 判斷是否停止
while stop == 1:
    ansnum = [] # 答案
    ansindex = []

    print("第一個多項式: ")
    (poly1_num, poly1_index) = Create()  # 建立第一個多項式
    Print(poly1_num, poly1_index)

    print("第二個多項式: ") 
    (poly2_num, poly2_index) = Create()  # 建立第二個多項式
    Print(poly2_num, poly2_index)

    op = input("請輸入運算: +,-,* : ")
    while op!="+" and op!="-" and op!="*" : # 若不符合支援的運算，則重新輸入
        print("不支持此運算")  
        op = input("請輸入運算: +,-,* : ")  

    if op == "+": # 加法
        (ansnum, ansindex) = Plus(poly1_num, poly1_index, poly2_num, poly2_index)
    elif op == "-": # 減法
        k = 0
        while k < len(poly2_num): # 將第二個多項式的係數皆呈以(-1)
           poly2_num[k] = poly2_num[k]*(-1) 
           k += 1
        
        (ansnum, ansindex) = Plus(poly1_num, poly1_index, poly2_num, poly2_index)
    else: # 乘法
        (ansnum, ansindex) = Mul(poly1_num, poly1_index, poly2_num, poly2_index)

    print("答案: ")
    Print(ansnum, ansindex)

    del poly1_num[:]
    del poly1_index[:]
    del poly2_num[:]
    del poly2_index[:]
    del ansnum[:]
    del ansindex[:]
    stop = int(input("是否繼續多項式運算? Yes:1 / No:0 : "))


        
  
