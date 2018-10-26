#
# import requests
# from bs4 import BeautifulSoup
#
# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
# root_url = 'http://www.meizitu.com/a/more_'
# for n in range(1,3):
#     url=root_url + str(n) +'.html'
#
#     r = requests.get(url,headers=headers)
#     content=r.text
#     soup = BeautifulSoup(content,'lxml')
#     div = soup.find_all(class_='pic')
#
#     count=1
#     for a in div:
#         src = a.img.attrs['src']
#
#
#
#         temp = requests.get(src)
#
#         with open('/Users/hogen/Pictures/aaa/' + str(n)+'_'+str(count) + '.jpg', 'wb') as f:
#             f.write(temp.content)
#             f.close()
#         count+=1
#         if not temp:
#             break






#
# import requests
# from bs4 import BeautifulSoup
# import threading
#
#
#
# def get_html(url):
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
#     }
#     r= requests.get(url,headers=headers)
#     print(url)
#     return r.text
#
# def get_pic(html,n):
#     soup = BeautifulSoup(html, 'lxml')
#     div = soup.find_all(class_='pic')
#     count = 1
#     for a in div:
#
#         try:
#             src = a.img.attrs['src']
#             print(src)
#             temp= requests.get(src)
#         except AttributeError as e:
#             continue
#
#         with open('/Users/hogen/Pictures/aaa/' + str(n)+'_'+str(count) + '.jpg', 'wb') as f:
#             f.write(temp.content)
#             f.close()
#         count+=1
#
#
#
# if __name__=='__main__':
#     root_url = 'http://www.meizitu.com/a/more_'
#     thread_list = []
#     for n in range(1, 5):
#         url = root_url + str(n) + '.html'
#         html = get_html(url)
#         ac = threading.Thread(target=get_pic,args=(html,n))
#         thread_list.append(ac)
#     for i in thread_list:
#         i.start()
#     for i in thread_list:
#         i.join()
#
#


import requests
from bs4 import BeautifulSoup
import threading



def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    }
    r= requests.get(url,headers=headers)
    print(url)
    return r.text


    # soup = BeautifulSoup(html, 'lxml')
    # div = soup.find_all(class_='pic')
    # count = 1
    # for a in div:
def get_pic(a,n,count):

    try:
        src = a.img.attrs['src']
        print(src)
        temp= requests.get(src)
    except AttributeError as e:
        return 

    with open('/Users/hogen/Pictures/aaa/' + str(n)+'_'+str(count) + '.jpg', 'wb') as f:
        f.write(temp.content)
        f.close()
    count+=1



if __name__=='__main__':
    root_url = 'http://www.meizitu.com/a/more_'
    thread_list = []
    for n in range(1, 4):
        url = root_url + str(n) + '.html'
        html = get_html(url)
        soup = BeautifulSoup(html, 'lxml')
        div = soup.find_all(class_='pic')
        count = 1
        for a in div:
            ac = threading.Thread(target=get_pic,args=(a,n,count))
            thread_list.append(ac)
    for i in thread_list:
        i.start()
    for i in thread_list:
        i.join()


