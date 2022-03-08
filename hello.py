from email import contentmanager
import json
from multiprocessing import context
import requests  #用于向网站发送请求
from bs4 import    BeautifulSoup
import os
def init():
    os.environ.setdefault("BASE_RADARR_URL","http://mf.frp.renjilin.top")
    os.environ.setdefault("BASE_RADARR_API_KEY","fcbc9a39e08940808dab2dcd52c2c4a3")

def lookup(title):
    url=os.environ.get("BASE_RADARR_URL")
    apiKey=os.environ.get("BASE_RADARR_API_KEY")

    headers = {
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"
    }

    url=url+"/api/v3/movie/lookup?apiKey="+apiKey+"&term="+title
    response = requests.get(url, headers=headers, timeout=10)

    print(url)

    content = response.content
    jsonObjects = json.loads(content)
    for jsonObj in jsonObjects:
        if(jsonObj["title"]==title):
            return jsonObj
        else:
            print(jsonObj["title"])
            print(title)
    return None

init()

douban_url = 'https://movie.douban.com/mine?status=wish'
douban_headers = {
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
    'Cookie': "douban-fav-remind=1; bid=_x_1Ziqaz0I; ll=\"118163\"; ap_v=0,6.0; __utmz=30149280.1646626056.3.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmz=223695111.1646626056.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _vwo_uuid_v2=DC613AB0118D08B1A9809B07CF8F38F65|83254670f47ca1a4eb6422ff2fdc91e1; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1646627907%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3Dx-8axkKgpTGe75k3kFppK715fF9S1DxePL2lWJPAVMRa_n1D3YPVN241DnHYKAUv%26wd%3D%26eqid%3Da7cf497500029b3c0000000462258500%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.1194066918.1609336352.1646626056.1646627907.4; __utmc=30149280; __utma=223695111.814176257.1646626056.1646626056.1646627907.2; __utmb=223695111.0.10.1646627907; __utmc=223695111; dbcl2=\"253935038:S3V6Ha2xGYI\"; ck=Mv-r; push_noty_num=0; push_doumail_num=0; __utmt=1; __utmv=30149280.25393; __utmb=30149280.2.10.1646627907; _pk_id.100001.4cf6=51b6a2048d95de82.1646626056.2.1646628035.1646626070."
}
response = requests.get(douban_url, headers=douban_headers, timeout=10)
html = response.text  
soup=BeautifulSoup(html,'lxml')
items = soup.select('.grid-view>.item')
for item in items:
    href=item.select(".pic>a").pop().get("href")
    title=item.select(".info>ul>.title>a>em").pop().text
    if(title.find("/")!=-1):
        title= title.split("/")[0]
    date=item.select(".info>ul>li>.date").pop().text
    
    moiveInfo=lookup(title.strip())
    if(moiveInfo != None):
        print(moiveInfo)
        
    

def getYear(href,headers):
    response = requests.get(href, headers=headers, timeout=10)




