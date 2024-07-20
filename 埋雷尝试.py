from tkinter import *
from PIL import ImageTk, Image
import time
import pyautogui as pa
import random as ra

def run(f:'list'):
   b=a.winfo_x()
   c=a.winfo_y()
   d,e=pa.position()
   d=int((d-b)/80-0.1)
   e=int((e-c)/80-0.3875)
   print(f[d][e])
def mailei(a:'list',b:'int',c:'int'):
    d=ra.randint(1,b-1)
    e=ra.randint(1,c-1)
    if a[d][e]==9:
        d,e=mailei(a,b,c)
        return d,e
    else:
        return d,e


a= Tk()
a.title('tiger')
a.resizable(0,0)
inp1=4
inp2=4
lei=2
m1=80*inp1
m2=80*inp2
ch=str(m1)+'x'+str(m2)
print(ch)
a.geometry(ch)
b=[[None for _ in range(inp1)] for _ in range(inp2)]

#埋雷
c=[[0 for _ in range(inp1)] for _ in range(inp2)]
for i in range(lei):
    x,y=mailei(c,inp1,inp2)
    c[x][y]=9
    if x+1>=0 and x+1<inp1 and y>=0 and y<inp2:
        if c[x+1][y]!=9 :
            c[x+1][y]+=1
    if  x-1>=0 and x-1<inp1 and y>=0 and y<inp2:
        if c[x-1][y]!=9 :
            c[x-1][y]+=1
    if x>=0 and x<inp1 and y-1>=0 and y-1<inp2:
        if c[x][y-1]!=9 :
            c[x][y-1]+=1
    if x>=0 and x<inp1 and y+1>=0 and y+1<inp2:
        if c[x][y+1]!=9 :
            c[x][y+1]+=1
    if x+1>=0 and x+1<inp1 and y+1>=0 and y+1<inp2:
        if c[x+1][y+1]!=9 :
            c[x+1][y+1]+=1
    if x+1>=0 and x+1<inp1 and y-1>=0 and y-1<inp2:
        if c[x+1][y-1]!=9 :
            c[x+1][y-1]+=1
    if x-1>=0 and x-1<inp1 and y+1>=0 and y+1<inp2:
        if c[x-1][y+1]!=9 :
            c[x-1][y+1]+=1
    if x-1>=0 and x-1<inp1 and y-1>=0 and y-1<inp2:
        if c[x-1][y-1]!=9 :
            c[x-1][y-1]+=1

for i in range(0,inp1):
    for j in range(0,inp2):
        b[i][j]=Button(a,relief=RAISED,bg='#d3fbfb',command=lambda:run(c))
        b[i][j].place(relx=(1/inp1)*i,rely=(1/inp2)*j,relheight=1/inp1,relwidth=1/inp2)
a.mainloop()