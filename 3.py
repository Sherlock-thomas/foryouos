# 电影详情数据
import requests
import json
if __name__ =="__main__":
    url="https://movie.douban.com/j/chart/top_list?"
    param = {
        "type":"11",
        "interval_id": "100:90",
        "action":"",
        "start": "0",
        "limit": "20",
    }
    header={
        "User-Agent":"Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1"
    }
    r=requests.get(url=url,params=param,headers=header)
    data_text=r.json()
    #永久性存储
    fd = open("./doubanban.json","w",encoding="utf-8")
    json.dump(data_text,fp=fd,ensure_ascii=False,indent=4)
    print("爬取成功")
