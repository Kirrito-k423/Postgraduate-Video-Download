from requests import Session

session = Session()
lesson_info_url = "http://wlkt.ustc.edu.cn/ajaxprocess.php?menu=getvideourl"

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36 Edg/102.0.1245.44'
}


data = {
        'videourl1': "8272NXnV7nQXpNbXpK5DqqkoXz3/UFCylJALVF+2aSZ4E6lseD4KLKgYHfGl0LGda+2rq/38bQh6/Kr0/42V+EkVrjYK1p0DBK6m",
        'hid_topicid': '2101'
    }

resp = session.post(url=lesson_info_url, headers=headers, data=data)
# get php
print(resp.text)
