# coding=utf-8
# 52shuku
# 爬取《全娱乐圈都在磕我和前男友的CP_苏芒【完结+番外】》# https://www.52shuku.vip/xiandaidushi/b/h7Li.html
import requests
import re
from lxml import etree
url = "//www.52shuku.vip"
print('开始获取章节列表')
page = requests.get('https://www.52shuku.vip/xiandaidushi/b/h7Li.html')
page.encoding = 'UTF-8'
html = etree.HTML(page.text)
aList = html.xpath('//*[@class="mulu"]/a')
print("aList",aList)
urlList = []
for i in aList:
    href = i.get('href')
    urlList.append(href)
print(urlList)
print(len(urlList))
print('获取章节目录成功')
print('获取小说内容')
fileTitle = html.xpath('//*[@class="article-title"]')[0].text
fileTitle = fileTitle + '.txt'
print(fileTitle)
file = open(fileTitle, 'a')
index = 0
for index,val in enumerate(urlList):
    print(index)
    nodePage = requests.get(urlList[index])
    print("nodePageUrl",urlList[index])
    nodePage.encoding = 'UTF-8'
    nodeHtml = etree.HTML(nodePage.text)
    contentLen = nodeHtml.xpath('//*[@class="article-content"]/p/text()')
    print("contentLen",contentLen)
    for item in contentLen:
        item = item.replace(' ', '')
        item = re.sub('\s', '', item)
        item = re.sub('\n', '', item)
        file.write(item.encode('UTF-8', 'ignore').decode('UTF-8')+'\n')
    print('第'+str(index+1)+'章获取成功')
file.close()
print('写入小说内容成功')