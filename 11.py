from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import urllib.request

import os
import time


driver = webdriver.Chrome()
url = 'http://www.ivsky.com/tupian/chengshilvyou/'
driver.get(url)
for i in range(5):
    i =float(i)/5
    print(i)
    pageud='document.documentElement.scrollTop =document.documentElement.scrollHeight*{}'.format(i)
    driver.execute_script(pageud)
    time.sleep(3)
    a_list=driver.find_elements_by_css_selector('.il_img a img')
    for img in a_list:
        print(img)
        exit()
        src=img.get_attribute('src')
        img_name=img.src.split('/')[-1]
        path='/Users/hogen/Pictures/bbb/'+str(img_name)+'.jpg'
        urllib.request.urlretrieve(src,path)


