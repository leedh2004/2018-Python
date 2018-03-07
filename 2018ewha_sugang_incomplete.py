from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome('C:\\Users\\LDH\\Desktop\\chromedriver_win32\\chromedriver.exe')

html = driver.get("http://sugang.ewha.ac.kr")

driver.find_element_by_name("id").send_keys("1635020")
driver.find_element_by_name("passwd").send_keys("akswlwlak1")
driver.find_element_by_xpath('/html/body/center[1]/form/table/tbody/tr[3]/td/input[1]').click()  # 클릭

time.sleep(1)
cnt = 1
course_num = input('Your course number: ')
class_num = input('Your class number: ')

while True:
    try:
        driver.get("http://sugang.ewha.ac.kr/esug/servlet/sugb_slog2")
        iframe = driver.find_element_by_name("user")
        driver.switch_to_frame(iframe)
        html = driver.page_source
        driver.find_element_by_xpath("/html/body/form[3]/fieldset/table/tbody/tr/td/input[1]").send_keys(course_num)
        driver.find_element_by_xpath("/html/body/form[3]/fieldset/table/tbody/tr/td/input[2]").send_keys(class_num)
        driver.find_element_by_xpath("/html/body/form[3]/fieldset/table/tbody/tr/td/input[7]").click()
        time.sleep(0.5)
        alert = driver.switch_to_alert()
        time.sleep(1)
        alert.accept()
        print("TRY")
    except:
        time.sleep(2)
        alert = driver.switch_to_alert()
        alert.accept()
        print("EXCEPT")
        
    
#driver.quit() # 브라우저 종료
