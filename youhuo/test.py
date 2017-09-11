# _*_ coding:utf-8 _*_
import requests
from PIL import Image
import time
import os
url = 'http://www.bjgjj.gov.cn/wsyw/wscx/gjjcx-choice.jsp'
headers={'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
         'Accept-Encoding':'gzip, deflate',
         'Accept-Language':'zh-CN,zh;q=0.8',
         'Cache-Control':'max-age=0',
         'Cookie':'JSESSIONID=DF9C0E3E1A2619FCE36E30838FA72751.tomcat1; JSESSIONID=C2B7A18C3E8E561CB7CBCD11C0420237.tomcat1',
         'Host':'www.bjgjj.gov.cn',
         'Origin':'http://www.bjgjj.gov.cn',
         'Referer':'http://www.bjgjj.gov.cn/wsyw/wscx/gjjcx-login.jsp',
         'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'}


try:
    import cookielib
except:
    import http.cookiejar as cookielib

session = requests.session()
def get_captcha():
    t = str(int(time.time() * 1000))
    captcha_url = 'http://www.bjgjj.gov.cn/wsyw/servlet/PicCheckCode1'
    r = session.get(captcha_url, headers=headers)
    with open('captcha.jpg', 'wb') as f:
        f.write(r.content)
        f.close()
    # 用pillow 的 Image 显示验证码
    # 如果没有安装 pillow 到源代码所在的目录去找到验证码然后手动输入
    try:
        im = Image.open('captcha.jpg')
        im.show()
        im.close()
    except:
        print(u'请到 %s 目录找到captcha.jpg 手动输入' % os.path.abspath('captcha.jpg'))
    captcha = input("please input the captcha\n>")
    return captcha
captcha = get_captcha()
data = {'bh1':'522130199107162455',
                    'mm1':'651102',
                    'gjjcxjjmyhpppp1':captcha,
                    'gjjcxjjmyhpppp':captcha,
                    'lb':'1'}
print(data)
response = session.post(url=url,data=data ,headers=headers)
print(response.text)