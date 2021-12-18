import urllib.request
url = 'http://www.baidu.com/s?wd=ip'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'

}
proxies={
    '182.101.207.11'
}
# 请求对象定制
request = urllib.request.Request(url = url,headers= headers)
# 代理
handler = urllib.request.ProxyHandler(proxies=proxies)
opener = urllib.request.build_opener(handler)
# 访问服务器
response = opener.open(request)

content = response.read().decode('utf-8')

with open('daili.html','w',encoding='utf-8') as fp:
    fp.write(content)