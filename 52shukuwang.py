# coding=utf-8
# 52shukuwang
#  咸鱼真少爷上交了系统后 https://www.52shukuwang.com/yanqing/79546.html
import requests
import re
from lxml import etree
url = "https://www.52shukuwang.com"
print('开始获取章节列表')
print(url+'/yanqing/79546' + '.html')
page = requests.get('https://www.52shukuwang.com/yanqing/79546.html')
page.encoding = 'UTF-8'
html = etree.HTML(page.text)
aList = html.xpath('//*[@class="column4"]/a')
print("aList",aList)
urlList = []
for i in aList:
    href = i.get('href')
    nodeHref = url + href
    urlList.append(nodeHref)
print(urlList)
print(len(urlList))
print('获取章节目录成功')
print('获取小说内容')
fileTitle = html.xpath('//*[@class="art_tit"]')[0].text
fileTitle = fileTitle + '.txt'
print(fileTitle)
file = open(fileTitle, 'a')
index = 0
for index,val in enumerate(urlList):
    print(index)
    print("urlList[index]",urlList[index])
    nodePage = requests.get(urlList[index])
    print("nodePageUrl",urlList[index])
    nodePage.encoding = 'UTF-8'
    nodeHtml = etree.HTML(nodePage.text)
    contentLen = nodeHtml.xpath('//*[@class="book_con fix"]/p/text()')
    print("contentLen",contentLen)
    for item in contentLen:
        item = item.replace(' ', '')
        item = re.sub('\s', '', item)
        item = re.sub('\n', '', item)
        file.write(item.encode('UTF-8', 'ignore').decode('UTF-8')+'\n')
    print('第'+str(index+1)+'章获取成功')
file.close()
print('写入小说内容成功')