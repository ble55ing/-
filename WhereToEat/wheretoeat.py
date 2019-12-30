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
    dislike = ""
    score = []

    def __init__(self, name,dislike,score):
        self.name = name
        self.dislike = dislike
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
            json1['dislike'] = who1.dislike
            json1['score'] = who1.score
            x1 = json.dumps(json1,ensure_ascii=False)
            f.write(x1)
            f.write("\n")

def loadwho():
    global WhoCanGo
    with open("who.txt","r",encoding='utf-8') as f:
        for line in f.readlines():
            out = json.loads(line,encoding='utf-8')
            WhoCanGo.append(who(out['name'],out['dislike'],out['score']))
def load():
    loadwhere()
    loadwho()
    for who1 in WhoCanGo:
        while len(who1.score) < len(WhereCanGo):
            who1.score.append(0)
def init():
    who1 = who("blessing","粥", [1, 2, 3])
    who2 = who("blessing2","",[4, 5, 6])
    WhoCanGo.append(who1)
    WhoCanGo.append(who2)
    where1 = where("餐厅", " 南门 粥 近 ")
    where2 = where("饭店", " 东门 饺子 近 ")
    WhereCanGo.append(where1)
    WhereCanGo.append(where2)
    savewho()
    savewhere()

def TakeSecond(elem):
    return elem[1]
def choose(WhereToGo,WhoToGo):
    avg = []
    rdm = []
    all=0
    i=-1 #where的下标，score的下标
    for where1 in WhereToGo:
        i+=1
        whonum=0
        all=0
        for who1 in WhoToGo:
            whonum+=1
            all+=who1.score[i]
        avg.append(all/whonum)

        rdm.append((i,r.randint(900,1000)*all/whonum))
    rdm = sorted(rdm, key=TakeSecond,reverse=True)#从大到小
    for tuple1 in rdm:
        print(WhereToGo[tuple1[0]].sub,WhereToGo[tuple1[0]].dst,tuple1[1])

def menu():
    newWho = []
    newWhere = []
    dis = ""
    print("都谁去啊:")
    print("输入序号，空格分开:")
    for i in range(0,len(WhoCanGo)):
        print(str(i)+" "+WhoCanGo[i].name)
    strin = input()
    strlist1 = strin.split(" ")
    for str1 in strlist1:
        newWho.append(WhoCanGo[int(str1,10)])
        dis+=WhoCanGo[int(str1,10)].dislike+" "
    print("有啥不想吃的没:")# 种类
    print("填中文即可:")
    strin = input()
    strlist1 = strin.split(" ")
    dislist1 = dis.split(" ")
    print(strlist1)
    for where1 in WhereCanGo:
        flag=1
        for str1 in strlist1:
            if where1.dst.find(" "+str1+" ")>0:
                flag = 0
            if flag == 0:
                break;
        for str1 in dislist1:
            if where1.dst.find(" "+str1+" ")>0:
                flag = 0
            if flag==0:
                break;
        if flag==1:
            newWhere.append(where1)

    return [newWhere,newWho]

def main():
    #init()
    load()
    [newWhereo, newWho] = menu()
    choose(newWhereo, newWho)
    savewho()
    savewhere()




if __name__ == '__main__':
    main()


