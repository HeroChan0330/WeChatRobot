# -*- coding: utf8 -*-
import requests
import re
import json



def GetToken():
    appId='10836602'
    apiKey='YGFfngKGaIK5e9Tq0IsVhbE8'
    secretKey='seMmhU7RkRwawDD6dmk7G7MNgcdLgkXs'
    url='https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s'
    res=requests.get(url%(apiKey,secretKey))
    data=json.loads(res.text)
    #print data['access_token']
    return data['access_token']

def GetAudioUrl(tarText,savaPath):
    cuid='AC-D1-B8-C6-33-69'
    ctp='1'
    lan='zh'
    tok=GetToken()
    spd='3'
    pit='0'
    vol='5'
    per='3'
    requestUrl='http://tsn.baidu.com/text2audio?tex=%s&tok=%s&cuid=%s&ctp=%s&lan=%s&spd=%s&pit=%s&vol=%s&per=%s'
    return requestUrl

def GetAudio(tarText,savaPath):
    requestUrl=GetAudioUrl(tarText,savaPath)
    requestRes=requests.get(requestUrl%(tarText,tok,cuid,ctp,lan,spd,pit,vol,per))
    fp=open(savaPath,'wb')
    for chunk in requestRes.iter_content(chunk_size=512):
        if chunk:
            fp.write(chunk)
    fp.close()


if __name__=="__main__":
    GetAudio(u"我从未见过如此厚颜无耻之人","E:\\Hello World.mp3")