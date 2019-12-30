# -*- coding: utf-8 -*-
import wave as we
import numpy as np
import math
import json
import random as r
__author__ = 'blessing'

#总的数据加载
WhereCanGo=[] #能去哪里
WhoCanGo = [] #谁能去

x = {'name':'blessing','score':[1,2,3]}
class where:
    sub = ""
    dst = ""

    def __init__(self, sub,dst):
        self.sub = sub
        self.dst = dst


class who:
    name = ""
    score = []

    def __init__(self, name,score):
        self.name = name
        self.score = score

def savewhere():
    with open("where.txt","w",encoding="utf-8") as f:
        for where1 in WhereCanGo:
            json1={}
            json1['sub'] = where1.sub
            json1['dst'] = where1.dst
            x1 = json.dumps(json1,ensure_ascii=False)#添加这句话，可以使得文本中保持中文
            f.write(x1)
            f.write("\n")
def loadwhere():
    global WhereCanGo
    with open("where.txt","r",encoding="utf-8") as f:
        for line in f.readlines():
            out = json.loads(line,encoding='utf-8')#设置utf-8，不然默认是gbk
            WhereCanGo.append(where(out['sub'],out['dst']))

def savewho():
    with open("who.txt","w",encoding='utf-8') as f:
        for who1 in WhoCanGo:
            json1={}
            json1['name'] = who1.name
            json1['score'] = who1.score
            x1 = json.dumps(json1,ensure_ascii=False)
            f.write(x1)
            f.write("\n")

def loadwho():
    global WhoCanGo
    with open("who.txt","r",encoding='utf-8') as f:
        for line in f.readlines():
            out = json.loads(line,encoding='utf-8')
            WhoCanGo.append(who(out['name'],out['score']))
def load():
    loadwhere()
    loadwho()
    for who1 in WhoCanGo:
        while len(who1.score) < len(WhereCanGo):
            who1.score.append(0)
def init():
    who1 = who("blessing", [1, 2, 3])
    who2 = who("blessing2", [4, 5, 6])
    WhoCanGo.append(who1)
    WhoCanGo.append(who2)
    where1 = where("羊蝎子", "东门")
    where2 = where("金谷园", "东门")
    WhereCanGo.append(where1)
    WhereCanGo.append(where2)
    savewho()
    savewhere()

def TakeSecond(elem):
    return elem[1]
def choose():
    avg = []
    rdm = []
    all=0
    i=-1 #where的下标，score的下标
    for where1 in WhereCanGo:
        i+=1
        whonum=0
        for who1 in WhoCanGo:
            whonum+=1
            all+=who1.score[i]
        avg.append(all/whonum)
        rdm.append((i,r.randint(900,1000)*all/whonum))
    rdm = sorted(rdm, key=TakeSecond,reverse=True)#从大到小
    for tuple1 in rdm:
        print(WhereCanGo[tuple1[0]].sub,WhereCanGo[tuple1[0]].dst,tuple1[1])





def main():
    #init()
    load()
    choose()




if __name__ == '__main__':
    main()


