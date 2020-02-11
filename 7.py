import requests
try:
    kv ={"wd":"python"}
    r = requests.get("http://www.baidu.com/s",params = kv)
    print(r.status_code)
    print(r.request.url)
    print(len(r.text)) # 百度的安全限制，数据被拦截
    #print(r.text)
except:
    print("爬取失败")
