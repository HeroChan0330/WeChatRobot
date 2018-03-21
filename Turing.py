# -*- coding: utf8 -*-
import requests
import json

def GetResponse(msg):
    response=requests.post("http://www.tuling123.com/openapi/api",{"info":msg,"key":"09ee9b00f8b3703015f982b1ce987697","userid":"D0BDCC001A88F255F7581B910E7A3748"})
    response.encoding='utf8'
    #print response.text
    res=json.loads(response.text)
    return res['text']

def GetResponse2(msg):
    content={"perception": {"inputText": {"text": msg}},"userInfo": {"apiKey": "09ee9b00f8b3703015f982b1ce987697","userId": "D0BDCC001A88F255F7581B910E7A3748"}}
    #content={"perception":{"inputText":{"text":msg}},"userInfo":{"apiKey":"09ee9b00f8b3703015f982b1ce987697","userId":"D0BDCC001A88F255F7581B910E7A3748"}}
    response=requests.post("http://openapi.tuling123.com/openapi/api/v2",str(content))
    response.encoding='utf8'
    #print response.text
    res=json.loads(response.text)
    return res['results'][0]['values']['text']

if __name__=="__main__":
    print GetResponse2("Hello")