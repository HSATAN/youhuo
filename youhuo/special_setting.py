# _*_ coding:utf-8 _*_
import requests
header = {'referer':'https://www.yohobuy.com/',
          'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'}

url = 'https://www.v2ex.com/t/364904'
response = requests.get(url=url)
print(response.text)

