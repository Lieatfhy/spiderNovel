# coding=utf-8
# bookba
# 爬取《全网黑被小祖宗在综艺带飞》 http://fushutxt.cc/chuanyuechongsheng/44414.html
import ast
import json
import os.path

import requests
import re
import time
from lxml import etree
import random
time.sleep(0.5)
def str_to_dict(fileName):
    f = open(fileName, 'r')
    size = os.path.getsize(fileName)
    string = f.read(size)
    print(string)
    if len(string) == 0:
        return {}
    result = json.loads(string)
    return result

config = str_to_dict('config')
print(config)
jsonAddress = config['json']
fileAddress = config['data']

url = "http://fushutxt.cc"
novelUrl = "/chuanyuechongsheng/44210.html"
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
page = requests.get(url+novelUrl)
page.encoding = 'utf-8'
print("page",page)
html = etree.HTML(page.text)
print("html",html)
print(html.xpath('/html/head/title'))
fileTitle = html.xpath('/html/head/title/text()')[0]
print("title",fileTitle)
aList = html.xpath('//*[@name="titleselect"]/option')
print("aList",len(aList))
jsonTitle = jsonAddress + '/' + fileTitle + '.json'

with open(jsonTitle, 'r') as jsonFile:
    print(os.path.getsize(jsonTitle) == 0)
    if os.path.getsize(jsonTitle) == 0:
        fileJson = {}
    else:
        fileJson = str_to_dict(jsonTitle)
print("fileJson",fileJson)
urlList = []
for i in aList:
    href = i.get('value')
    text = i.text
    fileJson.setdefault(href,'')
    urlList.append(href)
jsonFile = open(jsonTitle, 'w')
jsonFile.write(json.dumps(fileJson, ensure_ascii=False, indent=4))
print(len(urlList))
print('获取章节目录成功')
print('获取小说内容')
fileTitle = fileAddress + '/' + fileTitle + '.txt'
print(fileTitle)
file = open(fileTitle, 'w')
# index = 0
for index,val in enumerate(urlList):
    if fileJson[urlList[index]] == '':
        time.sleep(0.5)
        print(index)
        nodePage = requests.get(url+urlList[index])
        print("nodePageUrl",url+urlList[index])
        nodePage.encoding = 'utf-8'
        nodeHtml = etree.HTML(nodePage.text)
        contentLen = nodeHtml.xpath('//*[@class="wwwfushutxtcc"]/p/text()')
    else:
        print(fileJson[urlList[index]])
        contentLen = fileJson[urlList[index]]
    print("contentLen",contentLen)
    for item in contentLen:
        item = item.replace(' ', '')
        item = re.sub('\s', '', item)
        item = re.sub('\n', '', item)
        file.write(item.encode('utf-8', 'ignore').decode('utf-8')+'\n')
    print('第'+str(index+1)+'章获取成功')
    fileJson[urlList[index]] = contentLen
    jsonFile = open(jsonTitle, 'w')
    jsonFile.write(json.dumps(fileJson, ensure_ascii=False, indent=4))
file.close()
jsonFile.close()
print('写入小说内容成功')
