# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 17:36:19 2019

@author: Caleb Foo
"""
import copy

f=open(r'C:\Users\Caleb Foo\Documents\School\3DC\mrtline.txt',"r")

def read_stations(f):
    mrt_lines={}
    lines = f.read().splitlines()
    
    for i,l in enumerate(lines):
        if i==0 or i%2==0:
            buff=l.strip("= ")
        else:
            mrt_lines[buff]=[i.strip(" ") for i in l.split(",")]
    return mrt_lines
def get_stationline(mrt):
    stations={}
    for v in mrt.values():
        for st in v:
            if st not in stations:
                    buffer=[]
                    for k,v2 in mrt.items():
                        if st in v2:
                            buffer.append(k)
                    stations[st]=copy.deepcopy(buffer)
    return stations

def get_interchange(stationline):
    buffer=copy.deepcopy(stationline)
    for k,v in stationline.items():
        if len(v)<2:
            del buffer[k]
    return buffer




def find_path(f,start,end):
    mrtline=read_stations(f)
    stationline=get_stationline(mrtline)
    line1=stationline[start]
    line2=stationline[end]
    def checkline(s1,s2):
        if len(s1)>1 or len(s2)>1:
            if len(s1)<len(s2):
                return s1[0] if s1[0] in s2 else False
            elif len(s1)>len(s2):
                return s2[0] if s2[0] in s1 else False
            else:
                return set(s1).intersection(set(s2)) if set(s1).intersection(set(s2)) else False
        else:
            return True if s1==s2 else False
    line=checkline(line1,line2)            
    if line==True:
        i1=mrtline[line].index(start)
        i2=mrtline[line].index(end)
        num=i2-i1
        if num>0:
            return mrtline[line][i1:i2]
        if num<0:
            return [mrtline[line][i2-i] for i in range(abs(num))]
    else:
        interchange=get_interchange(stationline)
        ic1=[]
        ic2=[]
        
print(find_path(f,'Boon Lay','Clementi'))
f.close()