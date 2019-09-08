# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
copyright by Team4
"""
from bs4 import BeautifulSoup 
from urllib import request  #用來建立請求
import chardet  # 使用 chardet 偵測字串的編碼
url = "https://udn.com/news/breaknews/"  #新聞網址
response = request.urlopen(url)  #存取網頁
html = response.read()  #讀取網頁原始碼

charset = chardet.detect(html) #執行detect函式
html = html.decode(str(charset["encoding"])) ##使用 str(charset["encoding"]) 解碼

soup = BeautifulSoup(html, 'html.parser') 
#設置html的編碼方式 
#使用剖析器為html.parser 

allList = soup.select("div.ms-info h1") 
#取HTML中的 <div class="ms-info"></div> 中的<h1>標籤存入allList
allLink = soup.select('.ms-slide')  

for title, news in zip(allList, allLink): # 將標題與新聞 使用zip函數打包成一組一組
    print(title.text) #print title in <h1></h1>
    temp = news.select('a') #select the url in <a href=""></a> 
    href = 'https://udn.com' + temp[0]['href'] #makes the url available
    print(href)
    print("\n")


    


            
        

