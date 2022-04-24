from sys import argv
import math
import hashlib

def compress(f):
  e=[]
  for x in f:
    e.append(int(x))
  
  l= math.floor( math.log2(e[len(e)-1]/len(e)))
  u=math.ceil(math.log2(e[len(e)-1]))-l
  print("l",l)
  U=bytearray(math.ceil((len(e)+math.floor((e[len(e)-1])/math.pow(2, l)))/8))
  L=bytearray(math.ceil((l*len(e))/8))
  s = 255
  take= s >> 8-l
  e2=[]
  for x in e:
    e2.append(take & x)

  b=0
  m=0
  for i in range(0,math.ceil((l*len(e))/8)) :
    k=8
    while (k!=0) & (m < len(e2)):
      b1=0
      if k >=l:
        if b!=0:
          s = 255
          take= s >> 8-b
          L[i]= (L[i] | ( take & e2[m])) 
          m=m+1
          k=k-b 
          b=0
        elif b==0: 
          L[i] = (L[i] | e2[m]) 
          m=m+1
          k=k-l 
      elif k!=0:
        L[i]=(L[i] | (e2[m]>>l-k))
        b1=l-k
        k=0
      if k >=l:
        L[i]=L[i]<< l 
      elif k!=0:
        L[i]=L[i]<< k
      if (m==len(e2)) & ((k-l)>=0):
        L[i] = L[i] << k-l
    b=b1 

  take=""
  for i in range(0,u):
    take += "1"
  for i in range(0,l):
    take += "0"

  e3=[]
  for x in e:
    e3.append((int(take,2) & x)>>l)

  e4=[]
  e4.append(e3[0])
  for i in range(1,len(e3)):
    e4.append(e3[i]-e3[i-1])

  b=0
  m=0
  for i in range(0,math.ceil((len(e)+math.floor((e[len(e)-1])/math.pow(2, l)))/8)) :
    k=8
    while (k!=0) & (m < len(e4)):
      b1=0
      if k >=(e4[m]+1):
        if b!=0:
          U[i] = (U[i] << b)|1
          m=m+1
          k=k-b 
          b=0
        elif b==0: 
          U[i] = (U[i] << (e4[m]+1))| 1
          k=k-e4[m]-1 
          m=m+1      
      elif k!=0:
        U[i] = (U[i] << k)
        b1=e4[m]+1-k
        k=0
    if m==len(e4) :
      U[i]=U[i] << k
    b=b1
  
  print("L")
  for x in L:
    bit_repr = format(x, '08b')
    print(bit_repr) 
  print("U")
  for x in U:
    bit_repr = format(x, '08b')
    print(bit_repr)

  m = hashlib.sha256()
  m.update(L)
  m.update(U)
  digest = m.hexdigest()
  print(digest)

if __name__ == "__main__":  
  file=open(argv[1], "r")
  compress(file)
  file.close()
