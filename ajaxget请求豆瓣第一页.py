#get请求
#
import urllib.request
url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=100'
headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'
}
# 请求对象定制
req = urllib.request.Request(url = url,headers = headers)
# 获取响应数据
res = urllib.request.urlopen(req)
content = res.read().decode('utf-8')
# 数据下载到本地
fp = open('douban.json','w',encoding='utf-8')
fp.write(content)

