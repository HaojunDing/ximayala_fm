import requests as r
from lxml import etree
from urllib import parse

url = 'https://www.ximalaya.com/youshengshu/7966543/'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}

html = r.get(url, headers=headers).text

html_element = etree.HTML(html)

# 搜索 过滤筛选
url_element = html_element.xpath('//ul[@class="dOi2"]/li/div[2]/a/@href')
for i in url_element:
    full_url = parse.urljoin(url,i)
    print(full_url)