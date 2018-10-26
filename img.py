# import requests
# from bs4 import BeautifulSoup
#
# url='http://desk.zol.com.cn/pc/'
# html= requests.get(url)
# html.encoding='utf8'
#
# soup = BeautifulSoup(html.content,'html.parser')
#
#
# count=1
# for i in soup.select('a.pic'):
#     temp = i.findAll('img')[0].attrs['src']
#     print(temp)
#     img = requests.get(temp)
#     with open('/Users/hogen/Pictures/sb_pic/' + str(count) + '.jpg', 'wb') as f:
#         f.write(img.content)
#         f.close()
#     count+=1
#     if count==20:
#         break


#
# import requests
# from bs4 import BeautifulSoup
#
# url='https://tieba.baidu.com/f?ie=utf-8&kw=%E5%A6%B9%E5%AD%90%E5%9B%BE%E7%89%87&fr=search'
# html= requests.get(url)
# html.encoding='utf8'
#
# soup = BeautifulSoup(html.content,'html.parser')
#
#
# count=1
# for i in soup.select('a.thumbnail vpic_wrap'):
#     temp = i.findAll('img')[0].attrs['src']
#     img = requests.get(temp)
#     with open('/Users/hogen/Pictures/porn/' + str(count) + '.jpg', 'wb') as f:
#         f.write(img.content)
#         f.close()
#     count+=1
#     if count==20:
#         break
#




#
#
# import requests
# from bs4 import BeautifulSoup
#
# url='http://www.mmjpg.com/mm/1'
# html= requests.get(url)
# # html.encoding='utf8'
#
# soup = BeautifulSoup(html.content,'html.parser')
#
#
# count=1
# for i in soup.select('img'):
#     # print(i)
#     tem = i.attrs['src']
#     print(tem)
#
#     # for j in i:
#     #     t = j.get['src']
#     #     print(t)
#     img = requests.get(tem)
#     with open('/Users/hogen/Pictures/porn/' + str(count) + '.jpg', 'wb') as f:
#         f.write(img.content)
#         f.close()
#     count+=1
#     if count==20:
#         break








import lxml
import requests
from bs4 import BeautifulSoup
#
# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
#
# url='https://www.qiushibaike.com/pic/'
# r= requests.get(url,headers=headers)
# content=r.text
# # html.encoding='utf8'
#
# soup = BeautifulSoup(content,'lxml')
#
#
# count=1
# d = soup.find_all(class_='thumb')
# for i in d:
#     img= i.a.img.attrs['src']
#     src = 'http:'+ img
#     print(src)
#     temp = requests.get(src)
#
#
#
#     with open('/Users/hogen/Pictures/porn/' + str(count) + '.jpg', 'wb') as f:
#         f.write(temp.content)
#         f.close()
#     count+=1
#     if count==20:
#         break




headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
url = 'http://www.meizitu.com/a/more_1.html'
r = requests.get(url,headers=headers)
content=r.text
soup = BeautifulSoup(content,'lxml')
div = soup.find_all(class_='pic')
count=20
for a in div:
    src = a.img.attrs['src']
    print(src)

    temp = requests.get(src)

    with open('/Users/hogen/Picture/porn/' + str(count) + '.jpg', 'wb') as f:
        f.write(temp.content)
        f.close()
    count+=1
    if count==25:
        break



