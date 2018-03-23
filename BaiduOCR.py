#-*- coding:utf8 -*-
import requests
import json
import base64

accessToken=''

def GetToken():
    global accessToken
    appId=''
    apiKey=''
    secretKey=''
    url='https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s'
    res=requests.post(url%(apiKey,secretKey))
    data=json.loads(res.text)
    #print data['access_token']
    accessToken=data['access_token']
    return accessToken


#读取图片
def GetFileContent(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


def BaiduOCR(imagePath):
    global accessToken
    url='https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic?access_token=%s'
    requestsHeaders={'Content-Type':'application/x-www-form-urlencoded'}
    imgContent=GetFileContent(imagePath)
    datas={'image':base64.b64encode(imgContent)}
    req=requests.post(url%accessToken,headers=requestsHeaders,data=datas)
    reqJson=json.loads(req.text)
    keywords=''
    for word in reqJson['words_result']:
        #print word['words']
        keywords+=word['words']+' '
    return keywords

def BaiduOCR_Stream(stream):
    global accessToken
    url='https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic?access_token=%s'
    requestsHeaders={'Content-Type':'application/x-www-form-urlencoded'}
    datas={'image':base64.b64encode(stream)}
    req=requests.post(url%accessToken,headers=requestsHeaders,data=datas)
    reqJson=json.loads(req.text)
    keywords=''
    for word in reqJson['words_result']:
        #print word['words']
        keywords+=word['words']+' '
    return keywords

if __name__=='__main__':
    GetToken()
    print BaiduOCR('666.jpg')