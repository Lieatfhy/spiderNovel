# coding=utf-8
# This is a sample Python script.
import requests
import re
from lxml import etree
url = "https://dijiubook.net"
print('开始获取章节列表')
page = requests.get(url+'/73_73546/')
page.encoding = 'gbk'
html = etree.HTML(page.text)
aList = html.xpath('//*[@id="list"]/dl/dd/a')
nameList = html.xpath('//*[@id="list"]/dl/dd')
urlList = []
afterApk = False
startPush = False
for i in aList:
    href = i.get('href')
    text = i.text
    if 'apk' in href:
        afterApk = True
    if afterApk:
        if '第1章' in text:
            startPush = True
            urlStart = href
        if startPush:
            urlList.append(href)
print(urlList)
startPush = False
name = 0
print(nameList)
for index,val in enumerate(nameList):
    text = val.text
    if type(text) == str:
        if 'App' in text:
            afterApk = True
        if '第3章' in text:
            startPush = True
            name = 3
    if startPush:
        name = name + 1
print('获取章节目录成功')
print(name)
print(urlStart)
nodeBaseUrl = int(urlStart.split('/')[2].split('.html')[0])
print('获取小说内容')
# name = 283
text = ""
# index = 0
for index in range(name):
    nodeurl = '/' + urlStart.split('/')[1] + '/' + str(int(nodeBaseUrl)+int(index)) + '.html'
    nodePage = requests.get(url+nodeurl)
    nodePage.encoding = 'gbk'
    nodeHtml = etree.HTML(nodePage.text)
    # nodeTitle = nodeHtml.xpath('//*[@id="wrapper"]/div[3]/div/div[2]/h1')[0].text
    # text = text+nodeTitle
    nodeContent = nodeHtml.xpath('//*[@id="content"]/text()')
    for item in nodeContent:
        text = text + item
    print('第'+str(index)+'章获取成功')
text = re.sub('\n','',text)
print(text)
text = text.encode('gbk', 'ignore').decode('gbk')
file = open("1.txt", 'w')
file.write(text)
file.close()
print('写入小说内容成功')