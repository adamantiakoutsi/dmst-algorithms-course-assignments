import argparse
from collections import defaultdict
import math

def cycle_f(a):
    f={}
    file=open(a, "r")
    x=int(file.readline())
    x1=x
    for k in file:
        f[x1]=int(k)
        x1=int(k)
    y,i,j=DetectCycle(f,x)
    l,c=RecoverCycle(f,y,i,j)
    print("cycle",c,"leader",l )
    if t:
      for i in range(0,len(table)):
        print(min(table)[0],min(table)[1])
        table.remove(min(table))

def DetectCycle(f,x):
    global b
    y = x
    i= 0
    m=0
    global table
    table=[]
    while True :
        if (i % b == 0) & (m == table_size) :
            b=2*b
            table = Purge(b)
            m=math.ceil(m/2);
        if (i % b == 0):
            l=(y,i)
            table.append(l)
            m=m+1
        y = f [y]
        i=i+1
        if (i % (g*b) < b ):
            j = SearchTableY(y)
            if j != -1 :
                return (y ,i, j)

def Purge(x):
    for i in table:
        if (((i[1]) % x ) != 0):
            table.remove(i)
    return table

def SearchTableY(y):
    for i in range(0,len(table)):
        if table[i][0]==y:
            return(table[i][1])
    return -1

def SearchTableJ(j):
    for i in range(0,len(table)):
        if table[i][1]==j:
            return(table[i][0])
    return -1

def RecoverCycle(f,y,i,j):
    c= 1
    found_c = False
    y1 = y
    while (c <= (g + 1) * b)  & (found_c == False) :
        y1 = f[y1]
        if y == y1 :
            found_c = True
        else:
            c = c + 1
    if (found_c == False) :
        c= i-j
    block_length = g*b
    final_block = block_length * math.floor(i/block_length)
    previous_block = final_block - block_length
    i1 = max(c, previous_block)
    j1 = i1-c
    l=j1+1
    fl=findfk(l,f)
    flc=findfk(l+c,f)
    while (fl != flc)&(fl!=-1)&(flc!=-1):
        l=l+1
        fl=findfk(l,f)
        flc=findfk(l+c,f)
    return l,c

def findfk(k,f):
    kb=SearchTableJ( b* math.floor(k/b))
    i=0
    while (i<(k%b))&(kb!=-1):
        kb=f[kb]
        i=i+1
    return kb

if __name__ == "__main__":  
  parser = argparse.ArgumentParser()
  parser.add_argument("-t", "--type", action="store_true")
  parser.add_argument("b", type=int, help="the b")
  parser.add_argument("g", type=int, help="the g")
  parser.add_argument("table_size", type=int, help="the table_size")
  parser.add_argument("input_sequence",  help="the first") 
  args = parser.parse_args()
  
  global t ,b, g ,table_size
  b = args.b
  g = args.g
  table_size = args.table_size
  t = args.type

  cycle_f(args.input_sequence)
  
