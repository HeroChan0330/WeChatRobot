#-*-coding:utf8-*-
import requests
import json
import random
import hashlib   

def Translate(origin,target,text):
    m2 = hashlib.md5()
    salt=random.uniform(10086,1008611)
    sign='20180304000130870'+text+str(salt)+'i49S4rCGnrDR_qSqUTAA'
    m2.update(sign)   
    sign=m2.hexdigest()   
    requestUrl='http://api.fanyi.baidu.com/api/trans/vip/translate?q=%s&from=%s&to=%s&appid=20180304000130870&salt=%s&sign=%s'
    response=requests.get(requestUrl%(text,origin,target,salt,sign))
    response.encoding='utf8'
    res=json.loads(response.text)
    if(len(res['trans_result'])>0):
        return res['trans_result'][0]['dst']


if __name__=="__main__":
    print Translate("auto","yue","吃了饭没")