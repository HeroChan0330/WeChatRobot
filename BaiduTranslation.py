#-*-coding:utf8-*-
import requests
import json
import random
import hashlib   

APPID=''
SECRETKEY=''
def Translate(origin,target,text):
    global APPID,SECRETKEY
    m2 = hashlib.md5()
    salt=random.uniform(-1008611,1008611)
    sign=APPID+text+str(salt)+SECRETKEY
    m2.update(sign)   
    sign=m2.hexdigest()   
    requestUrl='http://api.fanyi.baidu.com/api/trans/vip/translate?q=%s&from=%s&to=%s&appid=%s&salt=%s&sign=%s'
    response=requests.get(requestUrl%(text,origin,target,APPID,salt,sign))
    response.encoding='utf8'
    res=json.loads(response.text)
    if len(res['trans_result'])>0:
        return res['trans_result'][0]['dst']


if __name__=="__main__":
    print Translate("auto","yue","吃了饭没")