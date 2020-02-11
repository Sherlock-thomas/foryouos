import requests
import os
url = "https://videocdn.taobao.com/oss/ali-video/d6bc4ae3eb3c866bee9903d47d1210c6/video.mp4"
root = "D://pics//"
path = root + url.split("/")[-1] # 定义文件名称及目录
try:
    if not os.path.exists(root): # 以数字权限模式创建目录，默认模式是八进制
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path,"wb") as f: #二进制写入（图片为二进制格式）
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件已成功")
except:
    print("爬取失败")
