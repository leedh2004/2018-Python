from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
from multiprocessing import Pool 

def crawling(x):
    driver = webdriver.Chrome('C:\\Users\\LDH\\Desktop\\chromedriver_win32\\chromedriver.exe')
    driver.get("http://www.weehan.com/index.php?mid=main2015_2&act=dispMemberLoginForm")
    driver.find_element_by_name("user_id").send_keys("YourID")
    driver.find_element_by_name("password").send_keys("YourPW")
    driver.find_element_by_xpath('//*[@id="fo_member_login"]/fieldset/div[2]/input').click()  # 클릭
    page_num = x

    while True:
        url = "http://www.weehan.com/index.php?mid=board_all&page="+str(page_num)
        driver.get(url)
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        lis = soup.findAll('a', class_='hx')
        for i in lis:
            driver.get(url+(i["href"][i["href"].find('&best_document_srl='):]))
        page_num +=1


if __name__ =='__main__':
    num_list = list()
    page = 1200
    for i in range(0,5):
        num_list.append(page)
        page+=100
        
    pool = Pool(processes=5)
    pool.map(crawling, num_list)
    
