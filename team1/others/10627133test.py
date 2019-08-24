import sys
import os
if __name__ == "__main__":
    while 1 :
        print('0結束 1轉大寫 2轉小寫 3數數字 4讀文字檔 5複製檔案 6從文件找char出現數\n7建立k個n方數的list 8建立n個k方數並除j餘h的list')
        command = input('請輸入一個數字:')
        if command == '0' :
            break
        elif command == '1' :
            sentence = input('請輸入含有小寫英文之句子:')
            print(sentence.upper())
        elif command == '2' :
            sentence = input('請輸入含有大寫英文之句子:')
            print(sentence.lower())
        elif command == '3' :
            start = int(input('請輸入起始數字:'))
            end = int(input('請輸入結束數字:'))
            need = input('如需間隔請按/:')
            if need == '/':
                jump = int(input('請輸入間隔:'))
            for i in range(start,end+1,jump) :
                print(i)
        elif command == '4' :
            data = input('請輸入檔名:')
            with open(data)as f :
                 words = f.read()  #直接讀
            print(words)
        elif command == '5' :
            data = input('請輸入檔名:')
            with open(data)as f :
                words = f.readlines()     #分行讀 儲存在陣列中
            outdata = 'copy' + data
            fp = open(outdata,"w")
            for i in range(len(words)):
                print(words[i],end='',file=fp)
            fp.close()
        elif command == '6' :
            data = input('請輸入檔名:')
            target = input('請輸入要計算之char:')
            with open(data)as f :
                words = f.read()
            count = 0
            for c in words:
                if c==target:
                    count+=1
            print (count)
        elif command == '7' :
            howmany = input('請輸入要多少數字(從0開始):')
            square = input('請輸入要的次方數:')
            nums = [i**int(square) for i in range(int(howmany))]
            print (nums)
        elif command == '8' :
            howmany = input('請輸入要多少數字(從0開始):')
            square = input('請輸入要的次方數:')
            div = input('請輸入除數:')
            remainder = input('請輸入餘數:')
            nums = [i**int(square) for i in range(int(howmany)) if i**int(square) % int(div) == int(remainder)]
            print (nums)
        sys.exit()
