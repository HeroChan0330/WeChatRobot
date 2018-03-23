# -*- coding: utf8 -*-
from wxpy import *
import XiaoIce.XiaoIce as XiaoIce
import TextHandler
import RandomExpression
import DouTuLa

XiaoIce.Init()
DouTuLa.Init()
robot = Bot(cache_path=True)
#从控制台获取输入，好友列表中需要转发机器人的好友序号
#如果为0，则转发所有好友
#不为0则用'|'间隔序号
index=1
friendList=[]
temp=robot.friends()+robot.groups()
for friend in temp:
    print index,u' : ',friend.name.encode('gbk','ignore')
    index+=1
command=raw_input()
if command=='0':
    friendList=robot.friends()
else:
    for i in command.split('|'):
        friendList.append(temp[int(i)-1])
#friendList=robot.friends()

@robot.register(friendList,[TEXT,PICTURE])
def print_messages(msg):
    if msg.type==TEXT:
        print msg.sender,'>>>',msg.text
        #print type(msg.text)
        temp=TextHandler.ReceivedText(msg.text)
        res=XiaoIce.GetResponse(temp)
        #print res.type+res.content
        if res.type=='text':
            res2=TextHandler.ResponseText(temp,res.content)
            print msg.sender,'<<<',res2
            msg.reply_msg(u'「小冰」'+res2)
        elif res.type=='image':
            imagePath=XiaoIce.GetImage(res.content)
            msg.reply_image(imagePath)
    elif msg.type==PICTURE:
        msg.get_file('temp\\imgSave')
        imgUrl=DouTuLa.GetResponse('temp\\imgSave')
        if imgUrl ==None:
            imgPath=RandomExpression.GetRandomExp()
        else:
            imgPath=DouTuLa.GetImage(imgUrl)
        msg.reply_image(imgPath)
    elif msg.type==RECORDING:
        pass

embed()

