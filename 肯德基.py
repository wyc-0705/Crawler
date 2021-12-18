import urllib.request
import urllib.parse

#   请求对象定制 post请求使用urlencode(data).encode('utf-8') 再定制headers request的定制 url headers data
def creat_request(page):
    base_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
    data = {
        'cname': '北京',
        'pid':'',
        'pageIndex': page,
        'pageSize': '10'
    }
    data=urllib.parse.urlencode(data).encode('utf-8')
    headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'

    }
    request=urllib.request.Request(url=base_url,headers=headers,data=data)
    return request
# 得到响应的方法 传入请求 content = response.read().decode('utf-8)
def get_content(request):
    response =urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content
# 下载的方法
def down_load(page,content):
    with open('kfc_'+str(page)+'.json','w',encoding='utf-8') as fp:
        fp.write(content)
        fp.close()
if __name__ == '__main__':
    start_page = int(input('请输入起始页码'))
    end_page = int(input('请输入结束页码'))
    for page in range(start_page,end_page+1):
        request = creat_request(page)
        content = get_content(request)
        down_load(page,content)