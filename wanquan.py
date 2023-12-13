
import requests
from datetime import datetime
import re
import execjs
from bs4 import BeautifulSoup
import time
import sys
from tqdm import tqdm

def log():
    print('假装已经登陆了')
class mainProgram:

    def __init__(self):
        self.b = []
        self.cookies = {

        }
        self.wlkcID=sys.argv[1]
        self.wlkckkID=sys.argv[2]
        self.zjid=sys.argv[3]
    def shichang(self,name,wlkcID,wlkckkID,zjid):
        now = datetime.now()
        formatted_time = now.strftime("%Y/%m/%d %H:%M:%S")
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'max-age=0',
            #'Cookie': f'ASP.NET_SessionId=dwld2ey5l1zb2cckxx5bk31e; xh=c2019620354; ECVIKybG50GU62z5=%2BbC0H5JRu0PnhG21cWOtvKCG9zLXd14mZx31Wl9JbrI%3D; CYLHWULC1ZNPMW4F=4nzJBGpye7yA5oMORTtG4JnnTWUPbC9hHKHbJxLjq_bt7oxsB40LwhL%2BFg15NicvJ6KkzxSH2CARwBrQyhkjWYg1PZtvSO4oFGHkCcObJEiqRc1B7xkaBKlJiM1s7o07WMDn2gKhmv_qXPbUHTXSVA%3D%3D',
            'Proxy-Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        }
        print(f'准备开始刷{name}')
        params = {
            'wlkcID': wlkcID,
            'wlkckkID': wlkckkID,
            'zjid': zjid,
        }
        response = requests.get('http://jxjy.stdu.edu.cn/student/BootStrap_PPT.aspx', cookies=self.cookies,params=params, headers=headers, verify=False)
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
        
        headers2 = {
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
        guowangdaqingqiu=requests.post('http://jxjy.stdu.edu.cn/student/BootStrap_PPT.aspx',cookies=self.cookies,params=params,headers=headers2,data=data2,verify=False)
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
        guowangjieshu=requests.post('http://jxjy.stdu.edu.cn/student/BootStrap_PPT.aspx',cookies=self.cookies,params=params,headers=headers2,data=data3,verify=False)
        print(guowangjieshu.status_code)
        print(f'应该是已经刷完了{name}')



    def chapterList(self):
        now = datetime.now()
        formatted_time = now.strftime("%Y/%m/%d %H:%M:%S")
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'max-age=0',
            
            'Proxy-Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        }
        params = {
            'wlkcID': self.wlkcID,
            'wlkckkID': self.wlkckkID,
            'zjid': self.zjid,
        }
        response = requests.get('http://jxjy.stdu.edu.cn/student/BootStrap_CourseIndex.aspx', cookies=self.cookies,params=params, headers=headers, verify=False)
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
    def courseList(self):
        now = datetime.now()
        formatted_time = now.strftime("%Y/%m/%d %H:%M:%S")
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'max-age=0',
            #'Cookie': f'ASP.NET_SessionId=jt1ralktcpda43zmzznutzjn; xh=c2019620354; ECVIKybG50GU62z5=%2BbC0H5JRu0PnhG21cWOtvLo8bsjOn9%2Bg5OeAxpgrdjU%3D; CYLHWULC1ZNPMW4F=2%2BTBkLkqwRP79aH_wv3Mw__YX8YQaPEmiVT4%2BiBEo%2BxRRePFBNIW%2Bn3bT3FgpmAsAD2EteSaU60TtsC5_LMr%2BHKgJ%2BWtW9w0y3hI0gp_5qhFDXBJMA1Gz4zOFWLfpWm269wbDuDvD0VeejrgsXByKg%3D%3D; pageVideo=/student/BootStrap_CourseIndex.aspx?wlkcID=255&ziylbbh=06&zjID=14783&wlkckkID=778; timeVideo={formatted_time}',
            'Proxy-Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        }
        response = requests.get('http://jxjy.stdu.edu.cn/student/BootStrap_index.aspx?last=1', cookies=self.cookies,headers=headers, verify=False)   
        soup = BeautifulSoup(response.text, 'html.parser')

        # 遍历每个科目的a标签，提取科目名称
        subjects = soup.find_all('a', class_='kcmc')
        course_list = []    
        # 打印每个科目的名称
        print(1)
    # 打印每个科目的名称，并将信息添加到列表
        for index, subject in enumerate(subjects, start=1):
            course_name = subject.text.strip()
            course_link = subject['href']
            course_list.append({'index': index, 'name': course_name, 'link': course_link})
            print(f"第{index}个科目的名称: {course_name}, 链接: {course_link}")
        return course_list
    def choice(self):
        #查找课程列表
        self.chapterList()
        print(self.b)
            #遍历课程列表
        for item in self.b:
            name, wlkcID, wlkckkID, zjid = item
            try:
                self.shichang(name, wlkcID, wlkckkID, zjid)
            except:
                continue





if __name__ == "__main__":
    program_instance = mainProgram()
    program_instance.choice()