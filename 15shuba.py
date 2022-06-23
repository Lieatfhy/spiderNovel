# coding=utf-8
# 15shuba
# 《毒舌顶流是小结巴》：/html/68/68355/0.html

import requests
import re
from lxml import etree
# 获取章节列表
url = "https://www.15shuba.net"
print('开始获取章节列表')
urlList = []
nameList = []
page = requests.get(url + '/html/68/68355/0.html')
page.encoding = 'gbk'
html = etree.HTML(page.text)
aList = html.xpath('//div[@class="mulu"]/ul/li/a')
for index in aList:
    href = index.get('href')
    text = index.text
    nodeHref = url + href
    urlList.append(nodeHref)
    nameList.append(text)
print('获取章节目录成功')
print('开始获取小说内容')
text = ""
fileTitle = html.xpath('//div[@class="rt"]/h1')[0].text
fileTitle = fileTitle + '.txt'
print(fileTitle)
file = open(fileTitle, 'a')
print(len(urlList))
# 根据章节列表获取小说详情
for index,val in enumerate(urlList):
    file.write('\n' + nameList[index] + '\n')
    nodePage = requests.get(val)
    nodePage.encoding = 'gbk'
    nodeHtml = etree.HTML(nodePage.text)
    nodeContent = nodeHtml.xpath('//div[@class="yd_text2"]/text()')
    for contentIndex,value in enumerate(nodeContent):
        value = re.sub('\n', '', value)
        file.write(value.encode('gbk', 'ignore').decode('gbk'))
    print('第'+str(index+1)+'章获取成功')
file.close()
print('写入小说内容成功')