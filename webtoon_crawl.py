# coding: utf8

import requests
from bs4 import BeautifulSoup

f = open("C:/Users/LDH/Desktop/webtoon.txt", 'r')
webtoon_list = list()
while True:
	line = f.readline().replace("\n","")
	if not line: break
	webtoon_list.append(line)
f.close()

url = "http://comic.naver.com/webtoon/weekdayList.nhn?week="
resp = requests.get(url)

html = resp.text
soup = BeautifulSoup(html, "html.parser")
today_webtoon_list = soup.findAll("div", class_="thumb")

print ("오늘 볼 웹툰은 [", end=' ')

for j in webtoon_list:
    for i in today_webtoon_list:
        title = i.find('a')
        if str(title["title"]).find(j) != -1:
            print (j, end=' ')
print ("] 입니다")

