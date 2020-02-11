# 采用中文字符的空格填充 chr(12288)
import requests
from bs4 import BeautifulSoup
import bs4
def getHTMLText(url): # 获取网站信息
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return " "
def fillUnivList(ulist, html): # 提取网页信息
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:#tbody标签下儿子节点，tr对应每一个大学的信息
        if isinstance(tr, bs4.element.Tag):#instance()函数来判断一个对象是否是一个已知的类型
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[3].string])
def printUnivList(ulist,num):# 网页信息输出，增加可读性
    tplt="{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(tplt.format("排名","学校名称","总分",chr(12288)))
    for i in range(num):
        u=ulist[i]
        print(tplt.format(u[0],u[1],u[2],chr(12288)))
def main():# 至顶向下构建
    uinfo =[]
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
    html =getHTMLText(url)
    fillUnivList(uinfo,html)
    printUnivList(uinfo,10)
main()

