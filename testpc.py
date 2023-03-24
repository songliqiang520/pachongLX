from  bs4 import BeautifulSoup
import  urllib.request
x = 1
def crawl(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    req = urllib.request.Request(url,headers=headers)#创建对象
    page = urllib.request.urlopen(req,timeout=20)#设置超时
    contents = page.read().decode('utf-8')#获取源码
    soup = BeautifulSoup(contents, 'html.parser')
    my_girl = soup.find_all('img')
    for girl in my_girl:  # 遍历
        link = girl.get('src')  # 获取到src的值，即图片链接，如果图片链接是相对路径，还需要‘协议 + 主机名 + 端口号 + link’拼接完整
        print(link)  # 打印获取到的图片url
        global x
        urllib.request.urlretrieve(link, '/Users/mac/Desktop/imge\%s.jpg' % x)
        # x +=1
        print('正在下载第%s张图片' % x)
        x += 1


for page in range(1, 3):  # 爬取第1-2页的图片
    # print(page)
    # url = 'http://www.dbmeinv.com/?pager_offset=%s'%page # 也可以写%d
    url = 'http://www.dbmeinv.com/?pager_offset={}'.format(page)
    crawl(url)
print('恭喜你，图片下载完成啦！')