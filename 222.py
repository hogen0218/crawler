import os
import time
import urllib.request
from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://www.ivsky.com/tupian/')



for i in range(1,5):
    i = float(i)/5

    js = "document.documentElement.scrollTop =document.documentElement.scrollHeight * %f"%i
    driver.execute_script(js)
    time.sleep(3)
img_list = driver.find_elements_by_css_selector('.il_img a img')
for img in img_list:
    img_scr = img.get('scr')
    img_name = img.scr.split('/')[-1]
    path = '/Users/hogen/Pictures/bbb/' + str(img_name) + '.jpg'
    urllib.request.urlretrieve(img_scr,path)
    driver.find_element_by_link_text('下一页').click()
os.chdir(os.path.pardir)
driver.quit()

