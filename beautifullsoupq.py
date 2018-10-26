import requests
from bs4 import BeautifulSoup
#
# root_url='http://www.nowscore.com/'
# r=requests.get(root_url)
# soup = BeautifulSoup(r.text,"lxml")
# print('asdfasdf')
# for i in soup.select('a'):
#     temp=i.attrs['href']
#     r = requests.get(temp)
#     print(r.text)

# root_url='http://sc.news.163.com/meishi/'
# r=requests.get(root_url)
# soup = BeautifulSoup(r.text,"lxml")
#
# for i in soup.select('a'):
#     temp=i.attrs['href']
#     r = requests.get(temp)
#     print(r.text)

#
# root_url = 'http://www.4399.com/'
# r=requests.get(root_url)
# soup=BeautifulSoup(r.text,features="lxml")
# for i in soup.select('a'):
#     temp=i.attrs['href']
#     a=requests.get(temp)
#     print(a.text)
#



# import requests
# from bs4 import BeautifulSoup
# root_url = "http://blog.jobbole.com/all-posts/"
#
# r = requests.get(root_url)
# soup = BeautifulSoup(r.text)
#
# for i in soup.select('a.archive-title'):
#     tmp_href = i.attrs['href']
#     r = requests.get(tmp_href)
#     print(r.text)
#
#
#


import requests
from bs4 import BeautifulSoup
root_url = "http://blog.jobbole.com/all-posts/"

r = requests.get(root_url)
soup = BeautifulSoup(r.text,"lxml")
tag_head = soup.head
print(tag_head.contents[0])
# for i in soup.head:
#     temp=i.attrs['href']
#     a = requests.get(temp)
#     print(a.text)















