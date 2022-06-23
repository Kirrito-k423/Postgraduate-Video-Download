
import os
import re
import global_variable as glv

def crawlerStraightChain():
    straightChain=[]
    filepaths = os.getcwd() + glv._get("taskfilePath")
    filelist = os.listdir(filepaths)
    for html_file in filelist:
        if html_file[-5:] != '.html':
            continue
        ic("read html file %s" % html_file)
        with open(filepaths + html_file, "r", encoding='utf-8') as html:
            text = html.read()
            lesson_urls = 
            lesson_urls = re.findall(glv._get("baseUrl")+glv._get("regexList"), text)
            ic(lesson_urls)
            ic(len)
            for lesson_url in lesson_urls:
                print(lesson_url + "下载失败！")

    return straightChain