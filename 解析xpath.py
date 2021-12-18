from lxml import etree
# 本地文件 etree.parse
# 服务器 etree.html
tree = etree.parse("解析xpath.html")
# # 查找ul下面的li
# li_list = tree.xpath('//body/ul/li')

# 查找有id的li标签
# li_list = tree.xpath('//ul/li[@id]/text()')

#找到id为l1注意引号问提
# li_list = tree.xpath('//ul/li[@id="l1"]/text()')
# 找到id为1 的class的属性
# li = tree.xpath('//ul/li[@id="l1"]/@class')


print(li)
print(len(li))