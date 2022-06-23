# coding=utf-8
# fn39
# 爬取《辞职后我爆红全宇宙[快穿]》https://www.fn39.com/chuanyuezhongsheng/2022/0518/11674.html
# 爬取《暗恋我的豪门大佬也重生了》 https://www.fn39.com/xiandaidushi/2022/0429/11069.html

import requests
import re
import time
from lxml import etree
# 获取章节列表
url = "https://www.fn39.com/chuanyuezhongsheng/2022/0518/"
novelNumber = 11674
novelLenth = 5
chapterLenth = [172,191,222,213,208]
urlList = []
nameList = []
for i in range(novelLenth):
    novelUrl = url + str(novelNumber+i) + '.html'
    for index in range(chapterLenth[i]):
        if index == 0:
            urlList.append(url + str(novelNumber + i) + '.html')
        else:
            urlList.append(url + str(novelNumber+i) + '_' + str(index+1) + '.html')
print('获取章节目录成功')
print("urlList", urlList)
print('开始获取小说内容')
page = requests.get(urlList[0])
page.encoding = 'gb2312'
html = etree.HTML(page.text)
fileTitle = html.xpath('//div[@class="single-header"]/h1')[0].text
fileTitle = fileTitle.split()[0]
fileTitle = fileTitle + '.txt'
print(fileTitle)
file = open(fileTitle, 'a')
print(len(urlList))
index = 0
# 根据章节列表获取小说详情
for index, val in enumerate(urlList):
    time.sleep(3)
    nodePage = requests.get(urlList[index])
    nodePage.encoding = 'gb2312'
    nodeHtml = etree.HTML(nodePage.text)
    nodeContent = nodeHtml.xpath('//div[@class="entry-content"]/p/text()')
    for contentIndex, value in enumerate(nodeContent):
        value = re.sub('\s', '', value)
        value = re.sub('h','沨',value)
        file.write(value.encode('gb2312', 'ignore').decode('gb2312')+'\n')
    print('第'+str(index+1)+'章获取成功,还有'+ str(len(urlList)-index-1)+'章节还未获取')
file.close()
print('写入小说内容成功')
