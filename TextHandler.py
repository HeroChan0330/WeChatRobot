#-*-coding:utf8-*-
import BaiduTranslation

def ReceivedText(text):#如果直接返回对应内容而不经过AI就把第0个元素复制true
    return text

def ResponseText(rcvText,rspText):
    #print "origin text:"+rspText
    res=BaiduTranslation.Translate("auto","yue",rspText.encode("utf8"))
    #print "translate text:"+res
    return res

if __name__=="__main__":
    print ReceivedText("Hello?")
    print ResponseText("",u"吃了饭没aaa")