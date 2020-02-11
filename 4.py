# 根据查询时的状态，如果URL发生变化，则不是阿贾克斯请求，如果没有发生变化，则是
import requests
import json
if __name__ =="__main__":
    for i in range(1,6):

        number=i


        url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword"


        keyword = {
            "cname":"",
            "pid":"",
            "keyword": "北京",
            "pageIndex":number,
            "pageSize": "10",
        }
        header={
            "User-Agent": "Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1"
        }
        r=requests.post(url=url,data=keyword,headers=header)
        r.raise_for_status()
        r.encoding=r.apparent_encoding


        page_text = r.text
        print(page_text)

        fileName ="keyword.text"  # 搜索关键字
        with open (fileName,"w",encoding="UTF-8") as fp:
            fp.write(page_text)

        print(fileName,"保存成功")
