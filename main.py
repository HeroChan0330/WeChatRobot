# -*- coding: utf8 -*-
from wxpy import *
from queue import Queue
import Turing
import msxiaoiceapi.XiaoBing as XBAPI
import TextHandler
import RandomExpression

XBAPI.Init()
robot = Bot(cache_path=True)
mesQueue=Queue()


def ReceiveFromXB(msg):
    print "received from xb"
    global mesQueue
    requestMsg=mesQueue.get()
    target=requestMsg.sender
    content=msg.text
    target.send_msg(content)
    print "response:"+target.name+":"+content

def MsgEnQueue(msg):
    global mesQueue
    mesQueue.put(msg)


def MsgHandler(msg):
    print "Handling"
    print msg.sender.name
    if msg.sender.name==u'小冰':
        ReceiveFromXB(msg)
    else:
        print "receive:"+msg
        SendToXB(msg)
        
@robot.register(robot.friends(),[TEXT,PICTURE])
def print_messages(msg):
    if msg.type==TEXT:
        print(msg)
        #print type(msg.text)
        temp=TextHandler.ReceivedText(msg.text)
        res=XBAPI.GetResponse(temp)
        res2=TextHandler.ResponseText(temp,res)
        print res2
        msg.sender.send_msg(u'[AI回复]'+res2)
        #MsgHandler(msg)
    elif msg.type==PICTURE:
        msg.sender.send_image(RandomExpression.GetRandomExp())

embed()

