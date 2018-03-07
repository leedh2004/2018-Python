from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time

driver = webdriver.Chrome('C:\\Users\\LDH\\Desktop\\chromedriver_win32\\chromedriver.exe')

html = driver.get("http://sugang.ewha.ac.kr")

driver.find_element_by_name("id").send_keys("#")
driver.find_element_by_name("passwd").send_keys("#")
driver.find_element_by_xpath('/html/body/center[1]/form/table/tbody/tr[3]/td/input[1]').click()  # 클릭
time.sleep(1)

count = 0
num = 1
select_list = list()

while True:
    
    driver.get("http://sugang.ewha.ac.kr/esug/servlet/sugb_slog2")
    nframe = driver.find_element_by_name("navi")
    
    driver.switch_to_frame(nframe)
    driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[2]/td/p[2]/span/a").click()
    driver.switch_to.default_content()
    
    dframe = driver.find_element_by_name("display")
    driver.switch_to_frame(dframe)
    time.sleep(0.2)
    
    li = driver.find_element_by_xpath("/html/body/left/center/table/tbody/tr/td[1]/form/select")
        
    if count == 0:
        for option in li.find_elements_by_tag_name("option"):
            print (str(count)+' '+(option.text))
            select_list.append(option.text)
            count+=1
        select = input()
    else:
        for option in li.find_elements_by_tag_name("option"):
            if select_list[int(select)] in option.text:
                option.click()
                driver.find_element_by_xpath("/html/body/left/center/table/tbody/tr/td[2]/input").click()
    print (num)
    num+=1
#driver.quit() # 브라우저 종료
