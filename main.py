# -*- coding: utf8 -*-
from wxpy import *
import XiaoIce.XiaoIce as XiaoIce
import TextHandler
import RandomExpression

XiaoIce.Init()
robot = Bot(cache_path=True)

#从控制台获取输入，好友列表中需要转发机器人的好友序号
#如果为0，则转发所有好友
#不为0则用'|'间隔序号
index=1
friendList=[]
temp=robot.friends()
for friend in temp:
    print '%d:%s'%(index,friend)
    index+=1
command=raw_input()
if command=='0':
    friendList=robot.friends()
else:
    for i in command.split('|'):
        friendList.append(temp[int(i)-1])


@robot.register(friendList,[TEXT,PICTURE])
def print_messages(msg):
    if msg.type==TEXT:
        print '>>>',msg
        #print type(msg.text)
        temp=TextHandler.ReceivedText(msg.text)
        res=XiaoIce.GetResponse(temp)
        #print res.type+res.content
        if res.type=='text':
            res2=TextHandler.ResponseText(temp,res.content)
            print u'%s<<<'%msg.sender.name+res2
            msg.sender.send_msg(u'「小冰」'+res2)
        elif res.type=='image':
            imagePath=XiaoIce.GetImage(res.content)
            msg.sender.send_image(imagePath)
    elif msg.type==PICTURE:
        msg.sender.send_image(RandomExpression.GetRandomExp())
    elif msg.type==RECORDING:
        pass

embed()

