# coding=utf-8
# This is a sample Python script.
import requests
from lxml import etree
# 获取章节列表
url = "http://www.linghunshuxuan.com/36739381/"
print('开始获取章节列表')
urlList = []
nameList = []
for i in range(17):
    page = requests.get(url+'/page'+ str(i+1)+'.html')
    page.encoding = 'utf-8'
    html = etree.HTML(page.text)
    aList = html.xpath('/html/body/div[1]/div[3]/div[1]/div[3]/div/ul/li/a')
    for index in aList:
        href = index.get('href')
        text = index.text
        urlList.append(href)
        nameList.append(text)
    print('第'+str(i+1)+'页章节列表获取成功')
print(urlList)
print(nameList)
print('获取章节目录成功')
print('开始获取小说内容')
text = ""
file = open("1.txt", 'a')

# 根据章节列表获取小说详情
for index,val in enumerate(urlList):
    file.write('\n' + nameList[index] + '\n')
    nodePage = requests.get(val)
    nodePage.encoding = 'utf-8'
    nodeHtml = etree.HTML(nodePage.text)
    nodeContent = nodeHtml.xpath('/html/body/section/div/div[1]/div[3]/p/text()')
    for contentIndex,value in enumerate(nodeContent):
        file.write(value.encode('gbk', 'ignore').decode('gbk'))
    url = val.split('.html')[0]
    for i in range(5):
        nodePage2 = requests.get(url+'_'+str(i+2)+'.html')
        nodePage2.encoding = 'utf-8'
        nodeHtml2 = etree.HTML(nodePage2.text)
        nodeContent2 = nodeHtml2.xpath('/html/body/section/div/div[1]/div[3]/p/text()')
        print(len(nodeContent2))
        for nodeIndex,nodeVal in enumerate(nodeContent2):
            file.write(nodeVal.encode('gbk', 'ignore').decode('gbk'))
        if(len(nodeContent2) == 1):
            break
    print('第'+str(index+1)+'章获取成功')
file.close()
print('写入小说内容成功')