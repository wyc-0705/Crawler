#urlencode 多个参数的时候

# import urllib.parse
# data={
#     'wd' : '周杰伦',
#     'sex' : '男'
# }
# # 多个参数拼接的方法
# a=urllib.parse.urlencode(data)
# print(a)
import urllib.parse
import urllib.request

base_url = 'https://www.baidu.com/s?'
data = {
    'wd':'周杰伦',
    'sex':'男',
    'location':'中国台湾省'
}
new_data = urllib.parse.urlencode(data)
# 发请求
url = base_url+new_data

hearders ={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'
}
request = urllib.request.Request(url = url,headers = hearders)
response = urllib.request.urlopen(request)

# 获取源码数据
content = response.read().decode('utf-8')
print(content)
