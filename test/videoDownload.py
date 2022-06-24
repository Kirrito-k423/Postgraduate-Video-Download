
from urllib import request, error
import  time
from tsjPython.tsjCommonFunc import *
# import curses
# from curses import wrapper
# import multiprocessing as mp
barTotalNum=dict()
barCurrentNum=dict()
barStartTime=dict()
barBeforeTime=dict()
barName=set()

def is_positive(value):
    value = int(value)
    if value < 0:
        return False
    return True

def time2String(timeNum):
    if timeNum < 60:
        return "{:.2f}".format(timeNum)
    elif timeNum < 3600:
        timeNum=int(timeNum)
        minutes=timeNum//60
        secends=timeNum%60
        return "{:0>2d}:{:0>2d}".format(minutes,secends)
    else:
        timeNum=int(timeNum)
        hour=timeNum//3600
        minutes=(timeNum-hour*3600)//60
        secends=timeNum%60
        return "{:0>2d}:{:0>2d}:{:0>2d}".format(hour,minutes,secends)

def barString(name,current=0,total=-1):
    global barBeforeTime,barName,barStartTime,barTotalNum
    retSting=""
    if name not in barName:
        if is_positive(total):
            barName.add(name)
            barBeforeTime[name]=time.time()
            barStartTime[name]=time.time()
            barTotalNum[name]=total
            barCurrentNum[name]=0
        return "bar is ready……"
    elif is_positive(current):       
        total=barTotalNum[name]
        if total<current:
            current=total
        lastTime=time.time()-barBeforeTime[name]
        if current > barCurrentNum[name]:
            lastTime=lastTime/(current-barCurrentNum[name])
            barCurrentNum[name]=current
            barBeforeTime[name]=time.time()
        else:
            current=barCurrentNum[name]
        pastTime=time.time()-barStartTime[name]
        if current > 0:
            restTime=pastTime/current*(total-current)
        else:
            restTime=0   
        retSting+="[{}:{:3d}%] > |".format(format(name," <10"),int(100*current/total))  #█
        space='█'
        spaceNum=int(format(100*current/total,'0>2.0f'))
        leftNum=100-spaceNum
        retSting=retSting.ljust(spaceNum+len(retSting),space)
        retSting=retSting.ljust(leftNum+len(retSting),' ')
        retSting+="| {} [{}<{}, {} s/it]".format(str(current)+"/"+str(total),time2String(pastTime),time2String(restTime),time2String(lastTime))
    return retSting 

def report(a,b,c,name):
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

base_url="http://wlkt.ustc.edu.cn/"+"/mp4.php?file=ZNZBBHYB71OK38I9UV5M3N8SY3E7CX70"
try:
    request.urlretrieve(url=base_url,filename='Download/1.mp4',reporthook=report,data=None)
except error.HTTPError as e:
    print(e)
    print('\r\n' + base_url + ' download failed!' + '\r\n')
else:
    print('\r\n' + base_url + ' download successfully!')