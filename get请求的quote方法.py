#需求是获取、
import urllib.request
import urllib.parse
url = 'https://www.baidu.com/s?ie=utf-8&wd='
#   请求对象定制
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'
}
# 将汉字变为unicode编码
name = urllib.parse.quote('周杰伦')
url = url+name
request = urllib.request.Request(url=url,headers=headers)
# 模拟浏览器发送请求
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
# 打印数据
print(content)