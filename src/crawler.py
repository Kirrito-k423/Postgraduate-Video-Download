
import os
import re
import global_variable as glv
from tsjPython import *
from urllib import request
import urllib.request
#导入 bs4 库
import bs4
from bs4 import BeautifulSoup
from multiBar import barString
from requests import Session

def crawlerDownload():
    filepaths = os.getcwd() + glv._get("taskfilePath")
    filelist = os.listdir(filepaths)
    for html_file in filelist:
        if html_file[-5:] != '.html':
            continue
        [taskList,taskType] = crawlerStraightChain(filepaths,html_file)
        for taskFileName, taskUrl in taskList.items():
            downloadFromUrl(taskFileName, taskUrl,taskType)

def crawlerStraightChain(filepaths,html_file):
    ic("read html file %s" % html_file)
    taskType = judgeHTMLSourceType(filepaths,html_file)
    regexString = glv._get(taskType)["baseUrl"]+glv._get(taskType)["regexList"]
    urlList = downloadUrlList(filepaths,html_file,regexString,taskType)
    return [urlList,taskType]

def judgeHTMLSourceType(filepaths,html_file):
    with open(filepaths + html_file, "r", encoding='utf-8') as html:
        text = html.read()
        taskTypeList = glv._get("taskType")
        for taskKey, taskRegex in taskTypeList.items():
            ifNullList = re.findall(taskRegex, text)
            if ifNullList:
                ic("html file type %s" % taskKey)
                return taskKey
        errorPrint("Not find the html file type")
        return NULL

def downloadUrlList(filepaths,html_file,regexString,taskType):
    with open(filepaths + html_file, "r", encoding='utf-8') as html:
        text = html.read()
        lesson_urls = set(re.findall(regexString, text))
        ic(lesson_urls)
        ic("下载个数：%s" % len(lesson_urls))

        # add filename with url
        urlNameList = dict()
        for url in lesson_urls:
            regexFilename = url + glv._get(taskType)["regexNamesuffix"]
            # print(regexFilename)
            # ic(regexFilename)
            matchObj  = re.search(regexFilename,text)
            filename = matchObj.group(1)
            ic(url,filename)
            urlNameList[filename]=url
        return urlNameList



def downloadFromUrl(taskFileName, taskUrl,taskType):
    ic(taskUrl)
    # regexString=glv._get(taskType)["baseUrl"]+glv._get(taskType)["regexMp4"]

    # 先通过学校验证再下载网页，
    # https://stackoverflow.com/questions/1825438/download-html-page-and-its-contents
    opener = urllib.request.FancyURLopener({})
    f = opener.open(taskUrl)
    content = f.read()

    #1.得到beautifulsoup对象
    soup = BeautifulSoup(content,'html.parser')

    #通过指定的 属性获取对象
    ic(soup.find(id=glv._get(taskType)["data1id"]).attrs['value'])#单个对象
    ic(soup.find(id=glv._get(taskType)["data2id"]).attrs['value'])#单个对象

    data1Value=soup.find(id=glv._get(taskType)["data1id"]).attrs['value']
    data2Value=soup.find(id=glv._get(taskType)["data2id"]).attrs['value']

    videoUrl = getVideoUrl(data1Value, data2Value,taskType)
    videoDownload(videoUrl,taskFileName,taskType)

def getVideoUrl(data1Value, data2Value,taskType):
    session = Session()
    lesson_info_url = glv._get(taskType)["phpApi"]

    headers = glv._get(taskType)["headers"]


    data = {
            glv._get(taskType)["data1name"]: data1Value,
            glv._get(taskType)["data2name"]: data2Value
        }

    resp = session.post(url=lesson_info_url, headers=headers, data=data)
    # get php
    ic(resp.text)
    return resp.text

#下载进度函数
def report(a,b,c):
    '''
    a:已经下载的数据块
    b:数据块的大小
    c:远程文件的大小
    '''
    step=1
    per = int(100 * a * b / c)
    if per > 100:
        per = 100
    if per % step == 0:
        printString=barString("downloading",per,100)
        print(printString, end = "\r")

def videoDownload(videoUrl,taskFileName,taskType):
    base_url=glv._get(taskType)["baseUrl"]+videoUrl
    try:
        request.urlretrieve(url=base_url,filename=glv._get("downloadPath")+taskFileName,reporthook=report,data=None)
    except error.HTTPError as e:
        print(e)
        print('\r\n' + base_url + ' download failed!' + '\r\n')
    else:
        print('\r\n' + base_url + ' download successfully!')