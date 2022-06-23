
import os
import re
import global_variable as glv
from tsjPython import *
from urllib import request

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

#下载进度函数
def report(a,b,c):
    '''
    a:已经下载的数据块
    b:数据块的大小
    c:远程文件的大小
    '''
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
    if per % 1 == 1:
        print ('%.2f%%' % per)

def downloadFromUrl(taskFileName, taskUrl,taskType):
    ic(taskUrl)
    regexString=glv._get(taskType)["baseUrl"]+glv._get(taskType)["regexMp4"]

    # 先通过学校验证再下载网页，然后再找到php直连
    # 或者直接分析出


    #使用下载函数下载视频并调用进度函数输出下载进度
    request.urlretrieve(url=taskUrl,filename=glv._get("downloadPath")+taskFileName,reporthook=report,data=None)