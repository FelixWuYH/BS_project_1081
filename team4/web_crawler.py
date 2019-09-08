# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
copyright by Team4
"""
from bs4 import BeautifulSoup 
from urllib import request 
import chardet 

url = "https://udn.com/news/breaknews/" 
response = request.urlopen(url) 
html = response.read() 
charset = chardet.detect(html) 
html = html.decode(str(charset["encoding"])) 

soup = BeautifulSoup(html, 'html.parser') 
#設置html的編碼方式 
#使用剖析器為html.parser 

allList = soup.select("div.ms-info h1") 
#取HTML中的 <div class="ms-info"></div> 中的<h1>標籤存入allList
allLink = soup.select('.ms-slide')  

for title, news in zip(allList, allLink):
    print(title.text) #print title in <h1></h1>
    temp = news.select('a') #select the url in <a href=""></a> 
    href = 'https://udn.com' + temp[0]['href'] #makes the url available
    print(href)
    print("\n")


    


            
        

