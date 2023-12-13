import requests
from datetime import datetime
import re
import execjs
from bs4 import BeautifulSoup
import time

now = datetime.now()
formatted_time = now.strftime("%Y/%m/%d %H:%M:%S")
url = 'http://jxjy.stdu.edu.cn/student/BootStrap_index.aspx?last=1'
payload = {
    '__EVENTTARGET': 'Rep_wlkclist$ctl00$Lbtn_kcmc',
    '__EVENTARGUMENT': '',
}

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'no-cache',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': f'ASP.NET_SessionId=jt1ralktcpda43zmzznutzjn; xh=c2019620354; ECVIKybG50GU62z5=%2BbC0H5JRu0PnhG21cWOtvLo8bsjOn9%2Bg5OeAxpgrdjU%3D; CYLHWULC1ZNPMW4F=2%2BTBkLkqwRP79aH_wv3Mw__YX8YQaPEmiVT4%2BiBEo%2BxRRePFBNIW%2Bn3bT3FgpmAsAD2EteSaU60TtsC5_LMr%2BHKgJ%2BWtW9w0y3hI0gp_5qhFDXBJMA1Gz4zOFWLfpWm269wbDuDvD0VeejrgsXByKg%3D%3D; pageVideo=/student/BootStrap_CourseIndex.aspx?wlkcID=255&ziylbbh=06&zjID=14783&wlkckkID=778; timeVideo={formatted_time}',
        'Origin': 'http://jxjy.stdu.edu.cn',
        'Proxy-Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        'X-MicrosoftAjax': 'Delta=true',
        'X-Requested-With': 'XMLHttpRequest',
    # 添加其他可能需要的请求头
}

response = requests.post(url, data=payload, headers=headers)
print(response.text)
