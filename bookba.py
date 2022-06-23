# coding=utf-8
# bookba
# 爬取《我没信息素，你闻错了》 https://www.bookba.net/mulu-218628-list.html
import requests
import re
from lxml import etree
url = "https://www.bookba.net"
print('开始获取章节列表')
page = requests.get(url+'/mulu-218628-list'+'.html')
page.encoding = 'gbk'
html = etree.HTML(page.text)
aList = html.xpath('//*[@class="txt-list"]/li/a')
print("aList",aList)
nameList = []
urlList = []
startPush = False
urlStart = ""
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
fileTitle = html.xpath('//div[@class="detail-title fn-clear"]/h2')[0].text
fileTitle = fileTitle + '.txt'
print(fileTitle)
file = open(fileTitle, 'a')
index = 0
for index,val in enumerate(urlList):
    print(index)
    print(nameList[index])
    file.write(nameList[index] + '\n')
    nodePage = requests.get(url+urlList[index])
    print("nodePageUrl",url+urlList[index])
    nodePage.encoding = 'gbk'
    nodeHtml = etree.HTML(nodePage.text)
    contentLen = nodeHtml.xpath('//*[@class="page-content"]/div/text()')
    print("contentLen",contentLen)
    for item in contentLen:
        item = item.replace(' ', '')
        item = re.sub('\s', '', item)
        item = re.sub('\n', '', item)
        file.write(item.encode('gbk', 'ignore').decode('gbk')+'\n')
    print('第'+str(index+1)+'章获取成功')


file.close()
print('写入小说内容成功')