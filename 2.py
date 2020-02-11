#破解百度翻译
"""对应的请求是post请求，
响应数据是一组json数据"""
import requests
import json
if __name__=="__main__":
    post_url= "https://fanyi.baidu.com/sug"
    # UA 伪装
    header = {
        "User-Agent": "Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1"
    } # 浏览器所对应的身份标识
    # post请求参数处理，（同get请求一致）
    word=input("word")
    data={
        "kw":word
    }
    # 请求发送

    r=requests.post(url=post_url,data=data,headers=header)# data 为请求的参数
    #获取相应数据
    #r.text #字符串类型的json数据
    # json()方法返回的是obj，如果确认服务器响应数据是json类型才能够使用json（）
    #从header的connect-type看是不是json
    dic_obj=r.json()
    #print(dic_obj)
    #进行持久化存储
    fileNmae=word+".json"
    fp=open(fileNmae,"w",encoding="UTF_8")
    json.dump(dic_obj,fp=fp,ensure_ascii=False,indent=4) # 最后
    print("over")
