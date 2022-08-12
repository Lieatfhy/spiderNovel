# coding=utf-8
# bookba
# 爬取《我没信息素，你闻错了》 https://www.biquge.city/59_59142/
import requests
import re
import time
from lxml import etree
import random
time.sleep(0.5)
url = "https://www.biquge.city"
user_agent_list = ["Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/61.0",
                    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
                    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
                    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
                    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15",
                    ]
print('开始获取章节列表')
page = requests.get(url+'/59_59142/',params={'params':'1'},headers = {'User-Agent': random.choice(user_agent_list)})
page.encoding = 'gbk'
html = etree.HTML(page.text)
aList = html.xpath('//*[@id="list"]/dl/dd/a')
print("aList",aList)
urlList = []
startPush = False
urlStart = ""
for i in aList:
    if '第1页' in i.text:
        startPush = True
    if startPush:
        print('i',i)
        href = i.get('href')
        text = i.text
        urlList.append(href)
print(urlList)
print(len(urlList))
print('获取章节目录成功')
print('获取小说内容')
fileTitle = html.xpath('//*[@id="info"]/h1')[0].text
fileTitle = fileTitle + '.txt'
print(fileTitle)
file = open(fileTitle, 'a')
index = 0
for index,val in enumerate(urlList):
    time.sleep(0.5)
    print(index)
    nodePage = requests.get(url+urlList[index])
    print("nodePageUrl",url+urlList[index])
    nodePage.encoding = 'gbk'
    nodeHtml = etree.HTML(nodePage.text)
    contentLen = nodeHtml.xpath('//*[@id="content"]/text()')
    print("contentLen",contentLen)
    for item in contentLen:
        item = item.replace(' ', '')
        item = re.sub('\s', '', item)
        item = re.sub('\n', '', item)
        file.write(item.encode('gbk', 'ignore').decode('gbk')+'\n')
    print('第'+str(index+1)+'章获取成功')
file.close()
print('写入小说内容成功')