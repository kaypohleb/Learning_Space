#------Midterm_2014-------
#Category A

def stc(s1,s2):
    return abs(len(s1)-len(s2))

def sumVal(d):
    sumV=0
    if len(d.keys())==0:
        sumV = None
    else:
        for k,v in d.items():
            if int(k)<3:
                sumV+=v
            
    return sumV

def count(a,b,c):
    return True if len(range(a,b))>len(range(b,c)) else False

def getMRT(f):
    mrt_dict={}
    lines = f.read().splitlines()
    for l in lines:
        words = l.split(",")
        mrt_dict[words[0]]=words[1:]
    return mrt_dict
    
def distance(d,s):
    stations = s.split(",")
    if not stations:
        return -2
    elif len(stations)==1:
        return -1
    else:
        station1,station2=stations
        for k,v in d.items():
            if station1 in v:
                mrtline1=(k,v.index(station1))
            if station2 in v:
                mrtline2=(k,v.index(station2))

        if mrtline1[0]==mrtline2[0]:
            return abs(mrtline1[1]-mrtline2[1])-1
        else:
            return -1

def test():
    f=open(r'C:\Users\Caleb Foo\Documents\School\3DC\mrt.txt',"r")
    d=getMRT(f)
    done=False
    while not done:
        a=input("Two stations please:")
        dist=distance(d,a)
        if dist!=-2:
            print(dist)
        else:
            done=True
    print("Bye!")
    f.close()
    
class Matrix:

    def __init__(self,m=[],s="Matrix A",f="%6.2f"):
        self.s=s
        self.f=f
        self.m=m
    def __str__(self):
        strings=[]
        strings.append("{0} Rows:{1} Column:{2}".format(self.s,str(len(self.m)),str(len(self.m[0]))))
        for i in self.m:
            strings.append(" ".join(str(x) for x in i))
        return '\n'.join(strings)
    def diag(self):
        return all(self.m[x][x]!=0 for x in range(len(self.m)))
    def upperDiag(self):
        test=False
        fail=False
        for i in range(len(self.m)):
            for x in range(i,len(self.m)):
                if self.m[i][x]!=0 and fail==False:
                    test=True
                else:
                    test=False
                    fail=True
        return test
    def lowerDiag(self):
        test=False
        fail=False
        for i in range(len(self.m)):
            for x in range(i):
                if self.m[i][x]!=0 and fail==False:
                    test=True
                else:
                    test=False
                    fail=True
        return test
    def triDiag(self):
        test=False
        fail=False
        a=int(len(self.m)/2)
        for i in range(int(len(self.m)/2)):
            for x in range(a,len(self.m)):
                if self.m[i][x]!=0 and self.m[len(self.m)-i-1][len(self.m)-x-1]!=0 and fail==False:
                    test=True
                else:
                    test=False
                    fail=True
            a+=1
        return test
    
a=Matrix([[1,4,0,0],[3,4,1,0],[0,2,3,4],[0,0,1,3]])
print(a)

m2=[[1,0,0,0],[3,4,1,0],[0,2,3,4],[0,0,1,3]]
b=Matrix(m2)
print(b.upperDiag())
print(b.lowerDiag())

m3=[[1,4,0,0], [3, 0, 1, 0], [0, 2, 3, 4], [0,0,1,3]]
c=Matrix(m3, "DW Matrix", "%6.1f") 
print(c) 
        