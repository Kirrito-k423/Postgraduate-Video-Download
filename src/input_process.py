from icecream import ic
from icecream import install
import global_variable as glv
from tsjPython.tsjCommonFunc import *
import argparse

def inputParameters():
    yellowPrint("In addition to entering some parameters, you can also modify all parameters in config.py")
    parser = argparse.ArgumentParser()
    parser.description = "please enter some parameters"
    parser.add_argument(
        "-p",
        "--ProcessNum",
        help="multiple Process Numbers",
        dest="ProcessNum",
        type=int, default="20"
    )
    parser.add_argument(
        "-d",
        "--debug",
        help="is print debug informations",
        dest="debug",
        type=str,
        choices=["yes", "no"],
        default="yes",
    )
    args = parser.parse_args()
    glv._set("ProcessNum",args.ProcessNum)
    glv._set("debug",args.debug)
    pPrint(glv.GLOBALS_DICT)
    passPrint("parameter ProcessNum is : %s" % args.ProcessNum)
    passPrint("parameter debug is : %s " % args.debug)
    return args

def isIceEnable(isYes):
    install()
    ic.configureOutput(prefix='Debug -> ', outputFunction=yellowPrint)
    if isYes=="yes" : 
        ic.enable()
    else:
        ic.disable()