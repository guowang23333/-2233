
from loguru import logger
import requests
from datetime import datetime
import re
import execjs
from bs4 import BeautifulSoup
import time
import sys
from tqdm import tqdm


class mainProgram:

    def __init__(self,cookie_value):
        self.login=sys.argv[1]
        self.passd=sys.argv[2]
        self.b = []
        self.c = []
        self.d = []
        self.cookies = {
            'ASP.NET_SessionId': cookie_value,
            'xh': self.login,
        }

        self.headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'no-cache',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        #'Cookie': f'ASP.NET_SessionId=jt1ralktcpda43zmzznutzjn; xh=c2019620354; ECVIKybG50GU62z5=%2BbC0H5JRu0PnhG21cWOtvLo8bsjOn9%2Bg5OeAxpgrdjU%3D; CYLHWULC1ZNPMW4F=2%2BTBkLkqwRP79aH_wv3Mw__YX8YQaPEmiVT4%2BiBEo%2BxRRePFBNIW%2Bn3bT3FgpmAsAD2EteSaU60TtsC5_LMr%2BHKgJ%2BWtW9w0y3hI0gp_5qhFDXBJMA1Gz4zOFWLfpWm269wbDuDvD0VeejrgsXByKg%3D%3D; pageVideo=/student/BootStrap_CourseIndex.aspx?wlkcID=255&ziylbbh=06&zjID=14783&wlkckkID=778; timeVideo={formatted_time}',
        'Origin': 'http://jxjy.stdu.edu.cn',
        'Proxy-Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        'X-MicrosoftAjax': 'Delta=true',
        'X-Requested-With': 'XMLHttpRequest',
        
        }
    def log(self):

        data = {
            '__VIEWSTATE': '/wEPDwUKMjA2ODgxNjQyMQ8WBB4EZGxjcwUBNR4HY291bnRYaAUBMWRk9w8O6cw530qGTRTyhSSEErWFyA44C4SXt8FNbrN2N4U=',
            '__VIEWSTATEGENERATOR': '31ED0DB1',
            '__EVENTVALIDATION': '/wEdAAXU0hsfMYdGyZcoVVstV3Cg2Ta/DdPUmiPavsa51vj6/c6ALwuTnuqUMyjuluo1NfJRvMePuMX6lQrt/rTy171qdDlmqzbR2b7nqJgQp10tGuiyLodvjjz2ES4BRJbvBVH6/Utjjq6DbgpZ3ALf6XgX',
            'txt_userName': self.login,
            'txt_passWord': self.passd,
            'txt_yzm': '1223',
            'btn_login': '登\xA0\xA0\xA0\xA0\xA0录',
        }

        response = requests.post('http://jxjy.stdu.edu.cn/loginStu_BootStrap.aspx', headers=self.headers, data=data, verify=False, allow_redirects=False)
        print(response.text)
        # 获取 Set-Cookie 头部信息
        set_cookie_header = response.headers.get('Set-Cookie')

        # 切割多个 Set-Cookie 信息
        set_cookie_list = set_cookie_header.split(',')

        # 用于存储 UNTYXLCOOKIE 的值
        untyxlcookie_value = None

        # 遍历输出每个 Set-Cookie 信息
        for i, set_cookie in enumerate(set_cookie_list, start=1):
            print(f"Set-Cookie {i}: {set_cookie.strip()}")
            
            # 寻找 UNTYXLCOOKIE
            if 'ASP.NET_SessionId' in set_cookie:
                untyxlcookie_value = set_cookie.split('=')[1].split(';')[0].strip()

        # 输出 UNTYXLCOOKIE 的值
        print(f"\nUNTYXLCOOKIE 的值: {untyxlcookie_value}")
        program_instance = mainProgram(untyxlcookie_value)
        return program_instance
    def shichang(self,name,wlkcID,wlkckkID,zjid):
        now = datetime.now()
        formatted_time = now.strftime("%Y/%m/%d %H:%M:%S")
        print(f'准备开始刷{name}')
        params = {
            'wlkcID': wlkcID,
            'wlkckkID': wlkckkID,
            'zjid': zjid,
        }
        response = requests.get('http://jxjy.stdu.edu.cn/student/BootStrap_PPT.aspx', cookies=self.cookies,params=params, headers=self.headers, verify=False)
        # 使用 BeautifulSoup 解析 HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        # 查找 __VIEWSTATE 的 input 元素
        viewstate_input = soup.find('input', {'id': '__VIEWSTATE'})
        # 提取 __VIEWSTATE 的值
        viewstate_value = viewstate_input['value']
        # 查找 __EVENTVALIDATION 的 input 元素
        event_validation_input = soup.find('input', {'id': '__EVENTVALIDATION'})
        # 提取 __EVENTVALIDATION 的值
        event_validation_value = event_validation_input['value']
        # 获取总时长
        total_duration = soup.find('span', id='Lbl_spsc').text.strip()
        # 获取已学习时长
        learned_duration = soup.find('span', id='lbl_zsc').text.strip()
        endTime = (int(total_duration) - int(learned_duration))*60
        print(f'应刷时长{endTime}秒')
        logger.debug(f'应刷时长{endTime}秒',name)

        js_code = execjs.compile(""" 
            function add(event_validation_value){
                var value = event_validation_value
                var formBody = ''
                var tagName = 'INPUT';
                formElements = '8',
                count = 1
                type='hidden'
                for (i = 0; i < count; i++) {
                    var element = formElements[i];
                    var name = '__EVENTVALIDATION';
                    if (tagName === 'INPUT') {
                        var type = 'hidden';
                            formBody += encodeURIComponent(value) ;
                        }
                    }
                var decodedUrl = decodeURIComponent(formBody);
                return decodedUrl;
        }""")

        # 使用 compile 而不是 eval
        

        # 调用 JavaScript 函数
        result = js_code.call("add",event_validation_value)
        

        data2={
            'ScriptManager1':'UpdatePanel3|btn_jldqsj0',
            '__EVENTTARGET':'',
            '__EVENTARGUMENT':'',
            '__VIEWSTATE':viewstate_value,
            '__VIEWSTATEGENERATOR':'D2659B19',
            '__EVENTVALIDATION':result, 
            '__ASYNCPOST':'true',
            'btn_jldqsj0':'开始计时'
        }
        guowangdaqingqiu=requests.post('http://jxjy.stdu.edu.cn/student/BootStrap_PPT.aspx',cookies=self.cookies,params=params,headers=self.headers,data=data2,verify=False)
        print(guowangdaqingqiu.status_code)
        # 使用BeautifulSoup解析HTML
        soup = BeautifulSoup(guowangdaqingqiu.text, 'html.parser')


        # 从字符串中提取__VIEWSTATE的值
        viewstate_match = re.search(r'__VIEWSTATE\|([^|]+)\|', guowangdaqingqiu.text)

        # 从字符串中提取__EVENTVALIDATION的值
        eventvalidation_match = re.search(r'__EVENTVALIDATION\|([^|]+)\|', guowangdaqingqiu.text)

        if viewstate_match and eventvalidation_match:
            viewstate_value_true = viewstate_match.group(1)
            eventvalidation_value_true = eventvalidation_match.group(1)
            print("__VIEWSTATE:", viewstate_value_true)
            print("__EVENTVALIDATION:", eventvalidation_value_true)
        else:
            print("未找到__VIEWSTATE或__EVENTVALIDATION元素,可能是已经刷完了")
        data3={
            'ScriptManager1':'UpdatePanel3|btn_jldqsj0',
            '__EVENTTARGET':'',
            '__EVENTARGUMENT':'',
            '__VIEWSTATE':viewstate_value_true,
            '__VIEWSTATEGENERATOR':'D2659B19',
            '__EVENTVALIDATION':eventvalidation_value_true, 
            '__ASYNCPOST':'true',
            'btn_jldqsj0':'结束计时'
        }
        print(f'等待刷取{name}时间跑满')
        for i in tqdm(range(endTime)):
                time.sleep(1)
        guowangjieshu=requests.post('http://jxjy.stdu.edu.cn/student/BootStrap_PPT.aspx',cookies=self.cookies,params=params,headers=self.headers,data=data3,verify=False)
        print(guowangjieshu.status_code)
        print(f'应该是已经刷完了{name}')
        logger.debug('上传时长完毕',name)



    def chapterList(self,wlkcID, zjID, wlkckkID):
        now = datetime.now()
        params = {
            'wlkcID': wlkcID,
            'wlkckkID': wlkckkID,
            'zjid': zjID,
        }
        response = requests.get('http://jxjy.stdu.edu.cn/student/BootStrap_CourseIndex.aspx', cookies=self.cookies,params=params, headers=self.headers, verify=False)
        soup = BeautifulSoup(response.text, 'html.parser')
        # 查找所有大章节
        chapters = soup.select('.menu_head')
        self.b=[]
        # 遍历每个大章节
        for chapter in chapters:
            # 查找大章节下的小章节
            sub_chapters = chapter.find_next('div', class_='menu_body').find_all('span')
            # 遍历每个小章节
            for sub_chapter in sub_chapters:
                # 找到对应小章节的链接
                link = sub_chapter.find_next('a', class_='fa-file-powerpoint-o')
                # 如果找到链接，则提取链接的部分内容
                if link:
                    href = link.get('href', '')
                    # 使用正则表达式提取wlkcID，wlkckkID和zjid
                    match = re.search(r'wlkcID=(\d+)&wlkckkID=(\d+)&zjid=(\d+)', href)
                    if match:
                        wlkcID, wlkckkID, zjid = match.groups()
                        #直接写入b的列表里面 名字
                        self.b.append((sub_chapter.get_text(strip=True), wlkcID, wlkckkID, zjid))
        #主界面的课程查找
    def courseList(self):
        now = datetime.now()
        formatted_time = now.strftime("%Y/%m/%d %H:%M:%S")
        response = requests.get('http://jxjy.stdu.edu.cn/student/BootStrap_index.aspx?last=1', cookies=self.cookies,headers=self.headers, verify=False)   
        soup = BeautifulSoup(response.text, 'html.parser')

        # 定义正则表达式模式
        pattern = re.compile(r'(Rep_wlkclist\$ctl\d+\$Lbtn_kcmc).*?>(.*?)</a>', re.DOTALL)

        # 在HTML内容中搜索匹配项
        matches = pattern.finditer(response.text)

        subjects = []

        for match in matches:
            full_string = match.group(1)
            subject_name = match.group(2)
            subjects.append({"full_string": full_string, "subject_name": subject_name})

        # 打印结果
        for subject in subjects:
            self.c.append(f"completeString: {subject['full_string']}, subject: {subject['subject_name']}")
        viewstate_element = soup.find('input', {'name': '__VIEWSTATE'})
        if viewstate_element:
            self.viewstate_value = viewstate_element['value']
        else:
            print('__VIEWSTATE not found')

        # 找到__EVENTVALIDATION元素
        eventvalidation_element = soup.find('input', {'name': '__EVENTVALIDATION'})
        if eventvalidation_element:
            self.eventvalidation_value = eventvalidation_element['value']
        else:
            print('__EVENTVALIDATION not found')

        # 找到__VIEWSTATEGENERATOR元素
        viewstategenerator_element = soup.find('input', {'name': '__VIEWSTATEGENERATOR'})
        if viewstategenerator_element:
            self.viewstategenerator_value = viewstategenerator_element['value']
        else:
            print('__VIEWSTATEGENERATOR not found')



    #具体科目信息
    def specificSubject(self,target_subject):
        url = 'http://jxjy.stdu.edu.cn/student/BootStrap_index.aspx'
        data={
            '__EVENTTARGET':'',
            '__EVENTARGUMENT':'',
            '__VIEWSTATE':self.viewstate_value,
            '__VIEWSTATEGENERATOR':self.viewstategenerator_value,
            '__EVENTVALIDATION':self.eventvalidation_value,
            target_subject: '进入学习',

        }
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            # Requests sorts cookies= alphabetically
            # 'Cookie': 'ASP.NET_SessionId=wqzg35anx5kdgwxzjwpk4atw; xh=C2019620385; ECVIKybG50GU62z5=%2BbC0H5JRu0PnhG21cWOtvD13COKY%2BzoX7_KLls3fOf4%3D; CYLHWULC1ZNPMW4F=VX1_vGag7vK9xokDIMs8atCqp1TVvkPSelTEBD4YeyuawZUzPxssy0UEGLo%2BZhs8m1O5PxpZBWfQ0omrvb1UGB0ifMWOZ1aw%2BA7tdd97JR1m6dWFakKs9hl5AO5nNjU9Q96dDVoxVwhnkFWiNep1_g%3D%3D',
            'Origin': 'http://jxjy.stdu.edu.cn',
            'Proxy-Connection': 'keep-alive',
            'Referer': 'http://jxjy.stdu.edu.cn/student/BootStrap_index.aspx?last=1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        }
        params = {
        'last': '1',
        }
        response = requests.post('http://jxjy.stdu.edu.cn/student/BootStrap_index.aspx', cookies=self.cookies,data=data,params=params,headers=headers, verify=False) 
        # 使用正则表达式提取参数
        pattern = re.compile(r"window\.open\('IndexWlkc_BootStrap\.aspx\?wlkcID=(\d+)&.*?zjID=(\d+)&.*?wlkckkID=(\d+)'")
        matches = pattern.search(response.text)
        if matches:
            wlkcID = matches.group(1)
            zjID = matches.group(2)
            wlkckkID = matches.group(3)
            self.d.append((wlkcID, zjID, wlkckkID))


            print("wlkcID:", wlkcID)
            print("zjID:", zjID)
            print("wlkckkID:", wlkckkID)
        else:
            print("No match found.")
            

    def find_complete_string(self, target_subject):
        # 在self.c中查找匹配target_subject的完整字符串
        matching_elements = [element for element in self.c if target_subject in element]

        # 如果找到匹配的元素，输出
        if matching_elements:
            complete_string = matching_elements[0]
            return complete_string
        else:
            return None

    
    def choice(self):
        # 查课
        self.courseList()
        
        # 获取名字
        print(self.c)
        
        # 输入你要查找的科目名字
        target_subject = sys.argv[3]

        # 在self.c中查找匹配target_subject的完整字符串
        complete_string = self.find_complete_string(target_subject)

        # 如果找到匹配的完整字符串，输出
        if complete_string:
            # 使用正则表达式提取完整字符串中的部分内容
            match = re.search(r'completeString: (.*), subject:', complete_string)
            if match:
                # 输出匹配的部分
                print(f"匹配成功: {match.group(1)}")
            else:
                print(f"找不到匹配的元素 {target_subject}")
        else:
            print(f"找不到匹配的元素 {target_subject}")
        # 获取具体科目的值
    
        self.specificSubject(match.group(1))
        
        # 获取所有小科目的三个值
        for item2 in self.d:
            wlkcID, zjID, wlkckkID = item2
            self.chapterList(wlkcID, zjID, wlkckkID)
            print(self.b)
            # 刷课主程序
            # 遍历课程列表
            for item in self.b:
                name, wlkcID, wlkckkID, zjid = item
                try:
                    self.shichang(name, wlkcID, wlkckkID, zjid)
                except Exception as e:
                    print(f"An error occurred while processing {name}: {str(e)}")
                    continue


print("这一版本还没写自动重连，我懒得写了，凑活着用吧")


if __name__ == "__main__":
    program_instance = mainProgram("value1")
    program_instance = program_instance.log()
    program_instance.choice()
    