# _*_ coding:utf-8 _*_
import requests

url = 'https://item.yohobuy.com/51664144.html'
response = requests.get(url=url)
print(response.text)