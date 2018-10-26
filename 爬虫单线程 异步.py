import socket
from urllib import parse
import select

class Crawler:
    def __init__(self):
        self.read_list = list()
        self.write_list = list()
        self.header_dict = dict()
        self.msg_dict = dict()



    def loop(self,url):
        # header = self.gen_header(url)
        while 1:
            try:
                #windows如果select中三个list都是空会报错
                rlist, wlist,xlist = select.select(self.read_list, self.write_list, [])
            except OSError:
                continue
            for i in wlist:
                i.send(self.header_dict[i])
                self.write_list.remove(i)
                self.read_list.append(i)

            for i in rlist:
                if i not in self.msg_dict.keys():
                    self.msg_dict[i] = b''
                try:
                    msg = i.recv(10)
                    if not msg:
                        print(self.msg_dict[i])
                        del(self.msg_dict[i])
                        self.read_list.remove(i)
                    self.msg_dict[i] += msg
                except Exception:
                    if i in self.msg_dict.keys():
                        del(self.msg_dict[i])
                        try:
                            self.read_list.remove(i)
                        except Exception:
                            pass






    def add_task(self,url):

        if isinstance(url,list):
            for i in url:
                self.do_tasks(i)
        else:
            self.do_tasks(url)





    def do_tasks(self,url):
        header = self.gen_header(url)
        host, _ = self.parse_url(url)
        ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        ss.connect((host,80))
        ss.setblocking(False)
        self.write_list.append(ss)
        self.header_dict[ss]=header






    def parse_url(self,url):
        url_dict = parse.urlparse(url)
        host = url_dict.hostname
        path = url_dict.path
        if len(path)==0:
            path='/'
        return host,path

    def gen_header(self,url):
        host, path = self.parse_url(url)
        data = "GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\nUser-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497" \
               ".100 Safari/537.36\r\n\r\n".format(
            path, host).encode('utf8')
        return data

if __name__ =='__main__':
    url = "http://blog.jobbole.com/1142{}/"

    crawler = Crawler()
    for i in range(100):
        temp_url = url.format(i)
        crawler.add_task(temp_url)
    crawler.loop(url)


