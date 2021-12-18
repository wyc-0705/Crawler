# 使用handler访问百度 获取网页源码
import urllib.request
url = 'http://www.baidi.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'

}
req = urllib.request.Request(url= url ,headers=headers)
handler = urllib.request.HTTPHandler()
opener = urllib.request.build_opener(handler)
res = opener.open(req)
content = res.read().decode('utf-8')
print(content)