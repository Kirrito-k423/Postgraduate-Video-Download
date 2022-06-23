import global_variable as glv
from collections import defaultdict
import time

glv._init()

glv._set("ProcessNum",20)
glv._set("debug","yes")

glv._set("taskfilePath", "/todo/")
glv._set("taskfilenamesubfix","html")


glv._set("baseUrl", "http://wlkt.ustc.edu.cn/")
glv._set("regexList", "video/detail_[0-9]*_[0-9]*.htm")
glv._set("regexMp4", "mp4.php?file=")