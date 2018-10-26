import requests
from bs4 import BeautifulSoup
import threading

# url='https://market.douban.com/book/?utm_campaign=book_nav_freyr&utm_source=douban&utm_medium=pc_web'
record_list = []
a_list=[]
b_list=[]
n=1
def get_html(url):
    r = requests.get(url)
    return r.text

def start():
    # n=1
    url = 'http://blog.jobbole.com/category/career/'
    record_list.append(url)
    html=get_html(url)
    soup = BeautifulSoup(html,'lxml')

    books=soup.select('a.archive-title')
    a = threading.Thread(target=parse_book, args=(books,n)).start()

    page_nums = soup.select('a.page-numbers')
    b = threading.Thread(target=parse_pages, args=(page_nums,)).start()




    parse_pages(page_nums)

def parse_book(books,n):

    for book in books:
        book_href=book.attrs['href']

        res=get_html(book_href)
        print(res)
        with open('/Users/hogen/Pictures/bbb/' + str(n) + '.txt', 'wb') as f:
            f.write(str(res))
            f.close()
        n+=1

def parse_pages(page_nums):
    global record_list
    # global a_list
    # global b_list
    global n

    for i in page_nums:
        page_href=i.attrs['href']
        if page_href in record_list:
            continue
        record_list.append(page_href)
        html_page=get_html(page_href)
        page_soup = BeautifulSoup(html_page)
        books_list=page_soup.select('a.archive-title')
        parse_book(books_list,n)
        page_list = page_soup.select('a.page-numbers')
        parse_pages(page_list)



if __name__ == '__main__':
    start()
    print(record_list)
