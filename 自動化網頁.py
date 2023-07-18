import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# 基本設置
options = Options()

# Chrome 位置
options.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe"

# webdriver 位置
webdriver_path = 'D:\gekodriver\chromedriver.exe'
driver = webdriver.Chrome(options=options)

# 前往 google
driver.get('https://www.youtube.com/')

time.sleep(3)

# 輸入搜尋文字
search_elem = driver.find_element(By.NAME, 'search_query')
search_elem.send_keys('衛達化學製藥')


time.sleep(2)

# 點擊搜尋按鈕
search_btn = driver.find_element(By.ID, 'search-icon-legacy')
search_btn.click()

# 延迟2秒
time.sleep(200)

# Name: selenium Version: 4.10.0  #版本 114.0.5735.199