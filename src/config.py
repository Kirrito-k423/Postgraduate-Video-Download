import global_variable as glv
from collections import defaultdict
import time

glv._init()

glv._set("ProcessNum",20)
glv._set("debug","yes")

glv._set("taskfilePath", "/todo/")
glv._set("downloadPath", "Download/")
glv._set("taskfilenamesubfix","html")

glv._set("taskType", 
                {        
                "科大研究生教育":"http://wlkt.ustc.edu.cn/",
                })

glv._set("科大研究生教育", 
                {        
                "baseUrl":"http://wlkt.ustc.edu.cn/",
                "regexList":"video/detail_[0-9]*_[0-9]*.htm",
                # "regexNamePrefix":"video/detail_[0-9]*_[0-9]*.htm",
                "regexNamesuffix":"\" style=\"color:#\w*;\">([^<]*)</a>",
                "regexMp4":"mp4.php?file=\w*"
                })
