# 京东页面的抓取
import requests
url="https://item.jd.com/100004727377.html"
try:
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:1000]) # 爬取前1000条
except:
    print("爬虫失败")
