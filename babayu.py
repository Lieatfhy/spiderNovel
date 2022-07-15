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
import requests
import re
from lxml import etree
url = "https://www.babayu.com"
page = requests.get(url + '/book_other_141806' + '.html')
page.encoding = 'utf-8'
html = etree.HTML(page.text)
aList = html.xpath('//*[@class="clearfix chapter-list"]/li/span/a')
nameList = []
urlList = []
startPush = False
urlStart = ""
print("aList",aList)
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
        nodePage = requests.get(nodeurl)
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