import urllib.request
url = 'https://www.baidu.com'
# url组成 协议 https安全 反爬虫
headers = {
    # 存储伪装自身参数
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'
}
#请求对象的定制
request = urllib.request.Request(url = url,headers =headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf8')
print(content)
