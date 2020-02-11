import requests
import json
if __name__ =="__main__":
    header = {
        "User-Agent": "Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1"
    }
    id_list = [] # c存储企业ID
    all_data_list = [] # 存储所有企业详情数据信息
    url="http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsList"
    for page in range(1,6):
        page=str(page)
        data ={
            "on": "true",
            "page": page,
            "pageSize":"15",
            "productName":"",
            "conditionType": "1",
            "applyname":"",

        }
        json_ids =requests.post(url=url,headers=header,data=data).json()

        for dic in json_ids["list"]:
            id_list.append(dic["ID"])
        #获取企业详情数据
        #print(all_data_list)
    post_url ="http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsById"
    for id in id_list:
        data={
           "id":id
        }
        datail_json = requests.post(url=post_url,headers=header,data=data).json()
            #print(datail_json)
        all_data_list.append(datail_json)
        # 持久化存储
    fp=open("./allDate.json","w",encoding="utf-8")
    json.dump(all_data_list,fp=fp,ensure_ascii=False,indent=4)
print("爬虫成功")
