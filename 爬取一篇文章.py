import requests
root_url='http://python.jobbole.com/'
for i in range(89290,89291):
    root_url=root_url + str(i) +'/'
    r = requests.get(root_url).text
    with open('/Users/hogen/Pictures/bbb/' + str(1) + '.txt', 'wb') as f:
        f.write(r.encode('utf8'))
        f.close()