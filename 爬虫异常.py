import urllib.request
url = 'https://blog.csdn.net/cuiyaonan2000/article/details/52119486'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'

}
try:
    request = urllib.request.Request(url = url,headers = headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    print(content)
except urllib.error.HTTPError:
    print('系统正在升级')
except urllib.error.HTTPError:
    print('真的吗')