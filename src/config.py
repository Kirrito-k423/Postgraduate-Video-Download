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
                "phpApi":"http://wlkt.ustc.edu.cn/ajaxprocess.php?menu=getvideourl",
                "headers":{
                    'Accept': '*/*',
                    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36 Edg/102.0.1245.44'
                },
                "data1id":"videourl1",
                "data2id":"htopicid",
                "data1name":"videourl1",
                "data2name":"hid_topicid"
                # "regexMp4":"mp4.php?file=\w*"
                })
