import argparse

def hirschberg(a,b):
    if len(a)==0 :
        WW = "-"*len(b)
        ZZ = b
    elif len(b)==0 :
        WW = a
        ZZ = "-"*len(a)
    elif (len(a)==1) |( len(b)==1 ):
        WW,ZZ = NeedlemanWunsch(a,b)
    else :
        i= int(len(a)/2)
        sl=ComputeAlignementScore(a[0:i],b)
        ar1=a[i:len(a)]
        ar=ar1[::-1]
        br=b[::-1]
        s2=ComputeAlignementScore(ar,br)
        sr=s2[::-1]
        s=[]
        for (item1, item2) in zip(sl, sr):
             s.append(item1+item2)
        J = ma(s)
        WW=[]
        ZZ=[]
        WW1=[]
        ZZ1=[]
        for j in J: 
           if t:
               print(i,j)       
           wwl,zzl= hirschberg(a[0:i],b[0:j])
           wwr,zzr= hirschberg(a[i:len(a)],b[j:len(b)])
           for x in wwl:
               for y in wwr:
                        WW1.append(x+y)                        
           for x in zzl:
               for y in zzr:
                        ZZ1.append(x+y)          
           if len(WW)==0:
                for y in range (0,len(WW1)):
                    if (not(WW1[y] in WW) ) | (not(ZZ1[y] in ZZ)):  
                        WW.append(WW1[y])
                        ZZ.append(ZZ1[y])
           else :
            for x in range(0,len(WW)):
                for y in range (0,len(WW1)):
                    if (WW1[y]!=WW[x]) | (ZZ1[y]!=ZZ[x]):
                        WW.append(WW1[y])
                        ZZ.append(ZZ1[y])
    return(WW,ZZ)

def ma(s) :
   l=[]
   for i in range(0,len(s)):
       if max(s)==s[i]:
           l.append(i)
   return l

def ComputeAlignementScore(a,b):
    L= []
    K=[]
    for j in range(0,len(b)+1):
        L.append(j*g)
    for j in range(0,len(b)+1):
        K.append(0)
    for i in range(1,len(a)+1):
        tmp = K[:]
        K[:] = L[:]
        L[:] = tmp[:]
        L[0]=i*g
        for j in range(1,len(b)+1):
            md = Compare(a[i-1],b[j-1])
            L[j]=max(L[j-1]+g,K[j]+g,K[j-1]+ md)
    return L

def EnumerateAlignments(a,b,F,w,z):
    i=len(a)
    j=len(b)
    if (i==0) & (j==0):
        ww.append(w)
        zz.append(z)
        return 
    if (i>0) & (j>0) :
        n=Compare(a[i-1],b[j-1])
        if F[i][j]==F[i-1][j-1] + n:
            EnumerateAlignments(a[0:i-1],b[0:j-1],F,a[i-1]+w,b[j-1]+z)
    if (i> 0) & (F[i][j] == (F[i-1][j] + g)):
        EnumerateAlignments(a[:i-1],b,F,a[i-1]+ w,"-"+z)
    if (j > 0 )& (F[i][j] ==F[i][j-1] + g):
        EnumerateAlignments(a,b[:j-1],F,"-"+ w ,b[j-1]+z)

def Compare(a,b) :
    if a == b :
        n = m
    else:
        n = d
    return n

def NeedlemanWunsch(a,b):
    global ww
    global zz 
    ww=[]
    zz=[]
    w =""
    z =""
    F=[[0 for x in range(len(b)+1)] for x2 in range(len(a)+1)]
    F[0][0]=0
    for i in range(1,len(a)+1):
        F[i][0]= g * i
    for i in range(1,len(b)+1):
        F[0][i]= g * i
    for i in range (1,len(a)+1):
        for j in range(1, len(b)+1):
            a1 =  F[i-1][j-1] + Compare(a[i-1],b[j-1])
            b1 =  F[i-1][j] + g
            c =  F[i][j-1] +g 
            if (a1 >= b1) & (a1>=c):
                F[i][j]= a1
            elif b1>=c:
                F[i][j]= b1
            else:
                F[i][j]= c
    EnumerateAlignments(a,b,F,w,z)
    return ww ,zz
    
if __name__ == "__main__":  
  parser = argparse.ArgumentParser()
  parser.add_argument("-t", "--type", action="store_true")
  parser.add_argument("-f", "--file", action="store_true")
  parser.add_argument("-l", "--line", action="store_true")
  parser.add_argument("gap", type=int, help="the g")
  parser.add_argument("match", type=int, help="the m")
  parser.add_argument("differ", type=int, help="the d")
  parser.add_argument("a",  help="the first")
  parser.add_argument("b",  help="the second")  
  args = parser.parse_args()
  
  global t ,f , l , g ,m ,d
  g = args.gap
  m = args.match
  d = args.differ
  t = args.type
  f = args.file
  l =args.line

  if f:
      file1=open(args.a, "r") 
      file2=open(args.b, "r")
      if l:
        f1=[]
        f2=[]
        for x in file1:
            f1.append(x)
        for x in file2:
            f2.append(x)
        WL,ZL=hirschberg(f1,f2)
        for x in range(0,len(WL)):
            if WL[x]==ZL[x]:
                print("=",WL[x])
                print("=",ZL[x]) 
            elif WL[x]=="-":
                print("<",WL[x])
                print(ZL[x])
            elif ZL[x]=="-":
                print(WL[x])
                print(">",ZL[x])
            else:
                print("<",WL[x])
                print(">",ZL[x])
      else:
          data1 = file1.read()
          data2 = file2.read()
          WL,ZL=hirschberg(data1,data2)
  else:
    WL,ZL=hirschberg(args.a,args.b)
    for x in range(0,len(WL)):
       print(WL[x])
       print(ZL[x],"\n") 
