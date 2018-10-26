import requests
from bs4 import BeautifulSoup
import queue
import threading
index_urls_list = []


def get_html_doc(url):
    # 根据指定的url获取html文档
    res = requests.get(url)
    print(res.content)
    return res.content.decode("utf8")

def prase_detail(tasks):
    while True:
        #tasks如果是list:为空报错 如果为queue:为空阻塞 不会消耗cpu
        tmp_url = tasks.get()
        res = get_html_doc(tmp_url)
        print(res)


def parse_index(url,tasks):
    # 解析列表页面
    html_doc = get_html_doc(url)
    data = BeautifulSoup(html_doc)
    # 把index里面的url取出来再取下面的url
    # data.select调用css选择器 选择出来是dict
    detail_urls = data.select('[class=post-thumb] a')

    for i in detail_urls:
        #详情页面的url
        url = i['href']
        # get_html_doc(url)
        #tasks的数据结构 list queue
        tasks.put(url)
    # 取出所有其他index页面的翻页url 去解析其他的url
    index_urls = data.select('a[class=page-numbers]')
    for i in index_urls:
        if i not in index_urls_list:
            index_urls_list.append(i)
            url = i['href']
            parse_index(url,tasks)


# def start(url):
#     parse_index(url)


if __name__ == "__main__":
    tasks = queue.Queue()
    url="http://blog.jobbole.com/all-posts/"
    t1 = threading.Thread(target=parse_index,args=(url,tasks))
    t2 = threading.Thread(target=prase_detail,args=(tasks,))

    t1.start()
    t2.start()
    #
    t1.join()
    t2.join()