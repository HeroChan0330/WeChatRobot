#-*-coding:utf8-*-
import BaiduTranslation

def ReceivedText(text):#转发给小冰前的信息处理
    return text

def ResponseText(rcvText,rspText):#从小冰接收到信息的后处理
    #res=BaiduTranslation.Translate("auto","yue",rspText)
    #return res
    #print rspText
    return rspText.decode('utf8')

if __name__=="__main__":
    print ReceivedText("Hello?")
    print ResponseText("","吃了饭没aaa")