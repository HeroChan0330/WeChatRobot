#coding:utf8
import os
import random

def GetRandomExp():
    directory=os.listdir("Expressions")
    index=int(random.uniform(1,len(directory)))    
    return "Expressions\\"+directory[index]


if __name__=='__main__':
    print GetRandomExp()