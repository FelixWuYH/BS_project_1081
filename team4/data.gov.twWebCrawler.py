# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 02:06:16 2019
WebCrawler抓老師指定網站 政府開放資料平台
@author: LINYUJEN
"""

import urllib.request as req #載入模組並設定別名
from urllib.request import urlopen
import urllib
import bs4 # 爬蟲分析
import re # #字串.數字的操控

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@連線到第一層網頁"https://data.gov.tw/"
url="https://data.gov.tw/" #政府公開資料平台網址

#!!!必須建立一個Request的物件,附加Request Headers的資訊,讓Pprogram看起來像正常的使用者
request0=req.Request(url,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36"
})

# urlopen不要給網址 , 給request ,利用request去嘗試打開網站 否則會網頁被拒絕
with req.urlopen(request0) as response: #網路連線(打開一個網址)並回傳response物件
    data=response.read().decode("utf-8") #讀取此網頁的資料(原始碼 HTML CSS) 再 使用utrf-8解碼
    
#使用第三方套建BeautifulSoup 來分析網頁原始碼
root=bs4.BeautifulSoup(data , "html.parser")#將網頁原始碼data丟給beautifulSoup 使用html做解析
print(root.title.string) #印出整個網頁的大標題 (政府資料開放平臺 | 政府資料開放平臺)

#解析原始碼,取得每個正方形框框的標題及網址
Squares=root.find_all("div", class_="inner-wrapper") #使用find_all()找尋所有class="inner_wrapper"的div 所有標籤和內容 ,此會回傳一個list!!!
#Squares是網頁上那些所有小方塊的"原始碼"的一個list 

SquaresTitalList =[] ## 空lsit 用來存放每個框框的內容 (好像沒啥用)
hrefList=[] ## 空lsit  用來存放每個框框的連結
for Square in Squares : # 抓出每個小方塊原始碼中的的 "標題文字" 與 "短網址" 先存起來
    print(Square.a.string , end = '' ) #取"標題文字"
    #SquaresTitalList.append(Square.a.string) # 放入list存起來
    print(",網址為:", end = '')
    print("https://data.gov.tw/" + Square.a.get('href') )
    hrefList.append(Square.a.get('href')) # 放入list存起來
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@連線到第一層網頁結束

#**********************************************************連線到第二層網頁,點入正方形框框


for href in hrefList : # 跑完所有的方塊
    href = url + href # 自動產生新的每個方塊的各自連結(https://data.gov.tw/ + 剛剛存起來的短網址 )

    #----------------再次開始連線到各個框框(方式同上)
    request1 = req.Request(href,headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36"
    })
    with req.urlopen(request1) as response: #網路連線(打開一個網址)並回傳response物件
        data=response.read().decode("utf-8")

    root=bs4.BeautifulSoup(data , "html.parser")#將網頁原始碼data丟給beautifulSoup 使用html做解析
    print("-------------------------------------------------------------------")
    print("目前" , end='')
    print(root.title.string) #印出整個網頁的大標題 (點正方形後的標題)
    print("                                                                 ")
    print("                                                                 ")
    print("                                                                 ")
    
    #----------------以下能得知 一個正方形中共有多少資料 每頁15筆 故也能算出頁數
    data=root.find("span",class_="zone-facet current") #找到含有資料筆數的那一串字
    s = re.sub("\D","",data.string) #將字串中留下數字
    MAXnum=int(s) # 字串轉數字
    print("此資料集共有:", end= '' )
    print( MAXnum , end= '')
    print("筆資料")
    print("因此共有:", end= '' )
    print( MAXnum // 15, end= '' )
    print("頁,每頁最多15筆資料" )
    MAXpage = MAXnum // 15 # 總頁數
    #----------------以上能得知 一個方塊中共有多少資料 每頁15筆
   
    count = 0
    k=0
    while k <= MAXpage : #將此方塊的第一頁到最後一頁都跑過  if maxpage = 33 那網頁連結為 0到 33 1~34頁
        
        OldUrl = "https://data.gov.tw/datasets/search?qs=dtid%3A291&order=downloadcount&type=dataset&page="  #分頁的固定網址 只有後面的page會改變
        a = str(k); #數字轉字串
        NewUrl = "https://data.gov.tw/datasets/search?qs=dtid%3A291&order=downloadcount&type=dataset&page=" + a  #page0.1.2.3.4.5.......
        
        request2 = req.Request(NewUrl,headers={  # 連線到每個小分頁
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36"
        })
        with req.urlopen(request2) as response: #網路連線(打開一個網址)並回傳response物件
            data=response.read().decode("utf-8")
        
        root=bs4.BeautifulSoup(data , "html.parser")#將網頁原始碼data丟給beautifulSoup 使用html做解析

        datas=root.find_all("header", class_="node-header") #使用find_all()找尋所有class="node-header"的header 所有標籤和內容 ,會回傳一個列表list!!!
        #datas是網頁上那些每頁裡面的每個小標題的"原始碼"的一個list
        
        dataList =[] ## 空lsit
        datahrefList=[] ## 空lsit
        
        print("目前此頁page為:", end= '' )
        print( k+1 )
        for data in datas : # 抓出每個小標題的文字與連結 先存起來 (跑完此一頁的每一個標題)
            dataList.append(data.h2.a.string) #放入list
            #可在此直接連線直接取出所有的檔案!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            
            datahrefList.append(data.h2.a.get('href'))#放入list
            finalhref = url + data.h2.a.get('href') #將每個短網址與前面的網址組成最終的網址
            
            #--------------------------------------------連線到最後一個頁面!!!!!
            request3 = req.Request(finalhref,headers={  # 連線到每個小分頁
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36"
            })
    
            with req.urlopen(request3) as response: #網路連線(打開一個網址)並回傳response物件
                data=response.read().decode("utf-8")
                
            root=bs4.BeautifulSoup(data , "html.parser")#將網頁原始碼data丟給beautifulSoup 使用html做解析
            print("***********最終資料下載頁面*********")
            print(root.title.string) #印出整個網頁的大標題
            
            finalUrl = root.find("a", class_= "dgresource ff-icon ff-icon-csv") #使用find找尋csv檔
            fileName = str(count) + ".csv"
            if (finalUrl == None ):
                finalUrl = root.find("a", class_="dgresource ff-icon ff-icon-壓縮檔") #使用find找尋壓縮檔
            if (finalUrl == None) :
                finalUrl = root.find("a",class_="dgresource ff-icon ff-icon-ods") #使用find找尋ods檔
                fileName = root.title.string + ".ods"    
            if (finalUrl == None) :
                finalUrl = root.find("a",class_="dgresource ff-icon ff-icon-json") #使用find找尋json檔               
                fileName = root.title.string + ".json"
            if (finalUrl == None) :
                finalUrl = root.find("a",class_="dgresource ff-icon ff-icon-xls") #使用find找尋xls檔    
                fileName = root.title.string + ".xls"
            if (finalUrl == None) :
                finalUrl = root.find("a", class_="dgresource ff-icon ff-icon-txt" ) #使用find找尋TXT檔  
                fileName = root.title.string + ".txt"
            if (finalUrl == None) :
                finalUrl = root.find("a", class_="dgresource ff-icon ff-icon-zip" ) #使用find找尋zip檔   
                fileName = root.title.string + ".zip"
            if (finalUrl == None) :
                finalUrl = root.find("a", class_="dgresource ff-icon ff-icon-xml" ) #使用find找尋xml檔   
                fileName = root.title.string + ".xml"
            if (finalUrl == None) :
                finalUrl = root.find("a", class_="dgresource ff-icon ff-icon-pdf" ) #使用find找尋pdf檔    
                fileName = root.title.string + ".pdf"
            if (finalUrl == None) :
                finalUrl = root.find("a", class_="dgresource ff-icon ff-icon-xlsx" ) #使用find找尋xlsx檔                 
                fileName = root.title.string + ".xlsx"
            if (finalUrl == None) :
                finalUrl = root.find("a", class_="dgresource ff-icon ff-icon-doc" ) #使用find找尋doc檔                  
                fileName = root.title.string + ".doc"    
                
                
                
                
              
                
            finall = finalUrl.get('href')
            print("進入此連結可下載資料" , end='')
            print(finall)
        
            for ch in finall:
                if u'\u4e00' <= ch <= u'\u9fff': 
                    finall = urllib.parse.quote(finall, safe='/:?=')
                    print(finall)
                    break
                
            '''       
            headers = {"User-Agent":" Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"}
            req = urllib.request.Request(finall,headers=headers)
            data = urllib.request.urlopen(req).read().decode("utf-8")
            '''

            urllib.request.urlretrieve(finall, fileName)
                    
            count+=1
            
        #for迴圈結束
        
        k+=1 #下一頁
    #while迴圈結束
# for迴圈結束
        
