# coding=utf-8
# 巴巴鱼
# 《撒旦Alpha的娇宠甜妻[穿书]》： /book_other_137912
# 《被迫上萌娃综艺后爆红[重生]》： /book_other_144948
# 《病美人放弃挣扎[重生]》： /book_other_84610
# 《拯救偏执反派Alpha》： /book_other_9419
# 《猫为你操碎了心[穿书]》： /book_other_140010
# 《拯救偏执反派Alpha》： /book_other_141424
# 《二爷家的麻雀成精了》： /book_other_141260
# 《带球跑后大美人后悔了》： /book_other_141806
# 《重生后国师靠玄学爆红了》： /book_other_96615
# 《人鱼崽崽修仙爆红星际》： /book_other_140809
# 《和人鱼大佬联姻后》： /book_other_139166
import random
import time

import requests
import re
from lxml import etree
time.sleep(0.5)

url = "http://www.babayu.com"
user_agent_list = ["Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/61.0",
                    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
                    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
                    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
                    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15",
                    ]
page = requests.get(url + '/book_other_139166' + '.html',params={'params':'1'},headers = {'User-Agent': random.choice(user_agent_list)})
page.encoding = 'utf-8'
html = etree.HTML(page.text)
aList = html.xpath('//*[@class="clearfix chapter-list"]/li/span/a')
nameList = []
urlList = []
urlStart = ""
print("aList",aList)
time.sleep(0.5)
for i in aList:
    href = i.get('href')
    text = i.text
    urlList.append(href)
    nameList.append(text)
print(urlList)
print(len(urlList))
print(nameList)
print('获取章节目录成功')
print('获取小说内容')
fileTitle = html.xpath('//div[@class="chapter-hd"]/h1')[0].text
fileTitle = fileTitle + '.txt'
print(fileTitle)
file = open(fileTitle, 'a')
for index,val in enumerate(urlList):
    print(index)
    print(nameList[index])
    file.write(nameList[index] + '\n')
    nodePage = requests.get(url+urlList[index])
    time.sleep(0.5)
    nodePage.encoding = 'utf-8'
    nodeHtml = etree.HTML(nodePage.text)
    contentLen = nodeHtml.xpath('//*[@class="article-title"]/text()')[0]
    print("contentLen",contentLen)
    if len(str(contentLen).split('/'))>1 :
        contentLen = str(contentLen).split('/')[1].split(')')[0]
        contentLen = int(contentLen)
        print("contentLen",contentLen)
    else:
        contentLen = 1
    for i in range(contentLen):
        nodeurl = ""
        if i == 0:
            nodeurl = url+urlList[index]
        else:
            nodeurl = url + urlList[index].split('.html')[0] + '_' + str(i+1)+'.html'
        nodePage = requests.get(nodeurl,params={'params':'1'},headers = {'User-Agent': random.choice(user_agent_list)})
        nodePage.encoding = 'utf-8'
        nodeHtml = etree.HTML(nodePage.text)
        nodeContent = nodeHtml.xpath('//*[@id="BookText"]/p/text()')
        print("nodeurl",nodeurl)
        print(nodeContent)
        for item in nodeContent:
            item = item.replace(' ', '')
            item = re.sub('\s', '', item)
            item = re.sub('\n', '', item)
            file.write(item.encode('gb2312', 'ignore').decode('gb2312')+'\n')
    print('第'+str(index+1)+'章获取成功')
file.close()
print('写入小说内容成功')