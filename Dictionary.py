# coding: utf8

import requests
from bs4 import BeautifulSoup
import win32com

f = open("C:/Users/LDH/Desktop/englishDB.txt", 'w')

url = "http://endic.naver.com/rank.nhn?sLn=kr&pubLev=2&firstWord=all&posp=all&pageNo="
resp = requests.get(url)

excel = win32com.client.Dispatch("Excel.Application")
excel.Visible = True

exit(0)
for i in range(1,196) :
    resp = requests.get(url+str(i))
    
    html = resp.text
    soup = BeautifulSoup(html, "html.parser")
    english_list = soup.findAll('span', class_='e_19_a')
    korean_list = soup.findAll('td', class_='f_con')
    for j in range(0,20):
        print (english_list[j].find(text=True),end=' '),
        print (korean_list[j].find(text=True).strip())
    
f.close()

