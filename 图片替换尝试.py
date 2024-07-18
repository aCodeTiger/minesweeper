from tkinter import *
from PIL import ImageTk, Image
import time

def r1():
    c=ImageTk.PhotoImage(b)
    d=Label(a,image=c)
    d.place(relx=0.2,rely=0.2,relheight=0.3,relwidth=0.3)
    a.update()
    a.after(600)
    c=ImageTk.PhotoImage(e)
    d=Label(a,image=c)
    d.place(relx=0.2,rely=0.2,relheight=0.3,relwidth=0.3)
    while True:
     a.update()
    
def r2():
    c=ImageTk.PhotoImage(b)
    d=Label(a,image=c)
    d.place(relx=0.5,rely=0.2,relheight=0.3,relwidth=0.3)
    a.update()
    a.after(600)
    c=ImageTk.PhotoImage(e)
    d=Label(a,image=c)
    d.place(relx=0.5,rely=0.2,relheight=0.3,relwidth=0.3)
    while True:
     a.update()
    
def r3():
    c=ImageTk.PhotoImage(b)
    d=Label(a,image=c)
    d.place(relx=0.2,rely=0.5,relheight=0.3,relwidth=0.3)
    a.update()
    a.after(600)
    c=ImageTk.PhotoImage(e)
    d=Label(a,image=c)
    d.place(relx=0.2,rely=0.5,relheight=0.3,relwidth=0.3)
    while True:
      a.update()
def r4():
    c=ImageTk.PhotoImage(b)
    d=Label(a,image=c)
    d.place(relx=0.5,rely=0.5,relheight=0.3,relwidth=0.3)
    a.update()
    a.after(600)
    c=ImageTk.PhotoImage(e)
    d=Label(a,image=c)
    d.place(relx=0.5,rely=0.5,relheight=0.3,relwidth=0.3)
    while True:
     a.update()
    

b=Image.open('E:\乐\python\minesweeper\image\mine.png')
b=b.resize((120, 120),Image.LANCZOS)
e=Image.open('E:\乐\python\minesweeper\image\zha.png')
e=e.resize((120, 120),Image.LANCZOS)
a= Tk()
a.title('tiger')
a.geometry('400x400')
b1=Button(a,bg='#d3fbfb',command=r1)
b2=Button(a,bg='#d3fbfb',command=r2)
b3=Button(a,bg='#d3fbfb',command=r3)
b4=Button(a,bg='#d3fbfb',command=r4)
b1.place(relx=0.2,rely=0.2,relheight=0.3,relwidth=0.3)
b2.place(relx=0.5,rely=0.2,relheight=0.3,relwidth=0.3)
b3.place(relx=0.2,rely=0.5,relheight=0.3,relwidth=0.3)
b4.place(relx=0.5,rely=0.5,relheight=0.3,relwidth=0.3)
while True:
 a.update()
