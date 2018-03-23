#-*- coding:utf8 -*-
import random
import requests
import json
import BaiduOCR


def Init():
    BaiduOCR.GetToken()

def GetResponse_Kw(keyword):
    url='https://www.doutula.com/api/search?keyword=%s&mime=0&page=2'
    req=requests.get(url%keyword)
    reqJson=json.loads(req.text)
    cnt=len(reqJson['data']['list'])
    index=int(random.uniform(0,cnt))
    return reqJson['data']['list'][index]['image_url']

def GetResponse(imagePath):
    kw=BaiduOCR.BaiduOCR(imagePath)
    if len(kw)==0:
        return None;
    return GetResponse_Kw(kw)

def GetResponse_Stream(stream):
    BaiduOCR.BaiduOCR_Stream(stream)
    return GetResponse_Kw(kw)

def GetImage(url):
    content=requests.get(url)
    fileName='temp\\'+url[url.rindex('/')+1:]
    fp=open(fileName,'wb')
    fp.write(content.content)
    fp.close()
    return fileName

if __name__=='__main__':
    BaiduOCR.GetToken()

    imgUrl=GetResponse('666.jpg')
    print GetImage(imgUrl)