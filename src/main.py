import config  # 加载配置
# from config import pasteFullFileName
import global_variable as glv
from input_process import inputParameters, isIceEnable
from terminal_command import mkdir
from crawler import crawlerStraightChain
# from excel import *
# from data import dataDictInit
# from multiProcess import *

def main():
    ## icecream & input
    args=inputParameters()
    isIceEnable(args.debug)
    mkdir(glv._get("taskfilePath"))

    taskList = crawlerStraightChain()
    # for taskKey, taskName in taskList.items():
    #     # glv._set("filename",pasteFullFileName(taskKey))
    #     filename=pasteFullFileName(taskKey)
    #     ic(filename)
    #     dataDict = dataDictInit()

    #     dataDict = readPartFile(taskName,filename, dataDict)
    #     print("blockSize {} {}".format(len(dataDict.get("unique_revBiblock")),len(dataDict.get("frequencyRevBiBlock"))))

if __name__ == "__main__":
    main()