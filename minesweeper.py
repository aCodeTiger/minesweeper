from tkinter import *
from PIL import ImageTk, Image
import pyautogui as pa
import random as ra
#import sys
import os
import useimage as us


#permission=[[False for _ in range(40)] for _ in range(40)]#记录方格状态
number=0

def dele(a):
    if type(a)==list or type(a)==tuple:
        for i in a:
            i.destroy()
    else:
        a.destroy()
#
def out():
    us.uncreat()
    os._exit(0)

#
def page1(a):#第一页
    b=a.winfo_screenwidth()
    c=a.winfo_screenheight()
    b=int((b-600)/2)
    c=int((c-400)/2)
    a.geometry('600x400+%d+%d'%(b,c))
    #文本框
    txt1=Label(a,text='扫雷游戏',bg='#D3D3D3',font=('宋体',50,'bold'),fg='#0000FF',justify='center')
    txt2=Label(a,text='欢迎游玩，点击下面按钮开始游戏。',bg='#D3D3D3',font=('黑体',15),fg='#000000',justify='center')
    txt1.place(relx=0.2,rely=0.1,relheight=0.3,relwidth=0.6)
    txt2.place(relx=0.2,rely=0.5,relheight=0.1,relwidth=0.6)
    #按钮
    but1=Button(a,text='开始',bg='#00BFFF',font=('黑体',25,'bold'),fg='#FF3030',activeforeground='#00EE00',command=lambda:page2(a,(txt1,txt2,but1)))
    but1.place(relx=0.3,rely=0.7,relheight=0.2,relwidth=0.4)

    a.protocol("WM_DELETE_WINDOW",out)

    while True:
        a.update()
        d=a.winfo_x()
        e=a.winfo_y()
#
def page2(a,b):#第二页
    dele(b)
    a.geometry('300x400')
    #文本框
    txt1=Label(a,text='请在下面的框中输入\n所需要的行数、列数和地雷数,\n以开始对应难度的游戏。',bg='#BEBEBE',font=('黑体',15),fg='#000000',justify='center')
    txt2=Label(a,text='方格块列数：',bg='#D3D3D3',font=('黑体',10),fg='#000000',justify='center')
    txt3=Label(a,text='方格块行数：',bg='#D3D3D3',font=('黑体',10),fg='#000000',justify='center')
    txt4=Label(a,text='地雷的数量：',bg='#D3D3D3',font=('黑体',10),fg='#000000',justify='center')
    txt5=Label(a,text='注意：\n1.横为行，竖为列\n2.所输入内容须为整数\n3.行、列数均须大于4小于40\n4.地雷数量不超过格子数量的十分之一',bg='#D3D3D3',font=('黑体',10,'bold underline'),fg='#FF3030',justify='left')
    txt1.place(relx=0.05,rely=0.05,relwidth=0.9,relheight=0.2)
    txt2.place(relx=0.1,rely=0.3,relwidth=0.3,relheight=0.05)
    txt3.place(relx=0.1,rely=0.4,relwidth=0.3,relheight=0.05)
    txt4.place(relx=0.1,rely=0.5,relwidth=0.3,relheight=0.05)
    txt5.place(relx=0.05,rely=0.55,relwidth=0.9,relheight=0.3)
    #输入框
    inp1=Entry(a)
    inp2=Entry(a)
    inp3=Entry(a)
    inp1.place(relx=0.4,rely=0.3,relwidth=0.5,relheight=0.05)
    inp2.place(relx=0.4,rely=0.4,relwidth=0.5,relheight=0.05)
    inp3.place(relx=0.4,rely=0.5,relwidth=0.5,relheight=0.05)
    #按钮
    but1=Button(a,text='开始游戏',bg='#00BFFF',font=('黑体',15,'bold'),fg='#FF3030',activeforeground='#00EE00',command=lambda:test1(a,inp1,inp2,inp3,(txt1,txt2,txt3,txt4,txt5,inp1,inp2,inp3,but1)))
    but1.place(relx=0.3,rely=0.8,relwidth=0.4,relheight=0.1)
    while True:
        a.update()
#
def test1(a,b,c,d,e):
    try:
        num1=int(b.get())
        num2=int(c.get())
        num3=int(d.get())
        test2(num1,num2,num3)
        test3(num3)
    except ValueError:
        warn1(b,c,d)
    except NameError:
        warn2(b,c,d)
    except ZeroDivisionError:
        warn3(b,c,d)
    else:
        page3(a,num1,num2,num3,e)
#
def test2(a,b,c):
    if a>40 or a<4 or b>40 or b<4 or c>a*b/10:
        raise NameError
#
def test3(a):
    if a<=0:
        raise ZeroDivisionError
#
def warn1(g1,g2,g3):
    p1=Tk()
    p1.title('错误！')
    p1.config(background='#D3D3D3')
    a=p1.winfo_screenwidth()
    b=p1.winfo_screenheight()
    a=int((a-300)/2)
    b=int((b-200)/2)
    p1.geometry('300x200+%d+%d'%(a,b))
    p1.resizable(0,0)
    #sys
    p1.iconbitmap('\\image\\tanhao.ico')
    #文本
    txt1=Label(p1,text='输入内容应为整数\n且不能留空！',bg='#D3D3D3',font=('黑体',25),fg='#FF3030',justify='center')
    txt1.place(relx=0,rely=0.1,relwidth=1,relheight=0.35)
    #按钮
    but1=Button(p1,text='确定',bg='#00BFFF',font=('黑体',15),fg='#FF3030',activeforeground='#00EE00',command=lambda:dele(p1))
    but1.place(relx=0.3,rely=0.6,relwidth=0.4,relheight=0.2)
    g1.delete(0,END)
    g2.delete(0,END)
    g3.delete(0,END)
#
def warn2(g1,g2,g3):
    p1=Tk()
    p1.title('错误！')
    p1.config(background='#D3D3D3')
    a=p1.winfo_screenwidth()
    b=p1.winfo_screenheight()
    a=int((a-300)/2)
    b=int((b-200)/2)
    p1.geometry('300x200+%d+%d'%(a,b))
    p1.resizable(0,0)
    #sys
    p1.iconbitmap('\\image\\tanhao.ico')
    #文本
    txt1=Label(p1,text='行、列数均须大于4小于40！\n地雷的数量不能超过\n格子数量的十分之一！',bg='#D3D3D3',font=('黑体',18),fg='#FF3030',justify='center')
    txt1.place(relx=0,rely=0.1,relwidth=1,relheight=0.45)
    #按钮
    but1=Button(p1,text='确定',bg='#00BFFF',font=('黑体',15),fg='#FF3030',activeforeground='#00EE00',command=lambda:dele(p1))
    but1.place(relx=0.3,rely=0.6,relwidth=0.4,relheight=0.2)
    g1.delete(0,END)
    g2.delete(0,END)
    g3.delete(0,END)
#
def warn3(g1,g2,g3):
    p1=Tk()
    p1.title('错误！')
    p1.config(background='#D3D3D3')
    a=p1.winfo_screenwidth()
    b=p1.winfo_screenheight()
    a=int((a-300)/2)
    b=int((b-200)/2)
    p1.geometry('300x200+%d+%d'%(a,b))
    p1.resizable(0,0)
    #sys
    p1.iconbitmap('\\image\\tanhao.ico')
    #文本
    txt1=Label(p1,text='地雷的数量\n 必须为正整数！',bg='#D3D3D3',font=('黑体',30),fg='#FF3030',justify='center')
    txt1.place(relx=0,rely=0.1,relwidth=1,relheight=0.45)
    #按钮
    but1=Button(p1,text='确定',bg='#00BFFF',font=('黑体',15),fg='#FF3030',activeforeground='#00EE00',command=lambda:dele(p1))
    but1.place(relx=0.3,rely=0.6,relwidth=0.4,relheight=0.2)
    g1.delete(0,END)
    g2.delete(0,END)
    g3.delete(0,END)
#
def page3(a,b,c,d,e):
    if b>=c:
        true_rel=int(600/b)
        true_x=int(true_rel*b)
        true_y=int(true_rel*c)
        x_y=str(true_x)+'x'+str(true_y)
        a.geometry(x_y)
    else:
        true_rel=int(600/c)
        true_x=int(true_rel*b)
        true_y=int(true_rel*c)
        x_y=str(true_x)+'x'+str(true_y)
        a.geometry(x_y)
    buts=[[None for _ in range(c)] for _ in range(b)]
    #按钮
    for i in range(0,b):
        for j in range(0,c):
            buts[i][j]=Button(a,relief=RAISED,bg='#d3fbfb',command=lambda:page4(a,b,c,d,buts,true_rel))
            buts[i][j].place(relx=(1/b)*i,rely=(1/c)*j,relwidth=1/b,relheight=1/c)
    dele(e)
#
def mailei(b,c,d,g,h):
    e=ra.randrange(0,b)
    f=ra.randrange(0,c)
    if d[e][f]==9 or (e,f)==(g,h) or (e,f)==(g+1,h) or (e,f)==(g+1,h+1) or (e,f)==(g,h+1) or (e,f)==(g-1,h+1) or (e,f)==(g-1,h) or (e,f)==(g-1,h-1) or (e,f)==(g,h-1) or (e,f)==(g+1,h-1):
        e,f=mailei(b,c,d,e,f)
        return e,f
    else:
        return e,f

#
def page4(a,b,c,d,e,f):
    a.update()
    x_rel=int(f)
    y_rel=int(f)
    p_x=a.winfo_x()
    p_y=a.winfo_y()
    w_x,w_y=pa.position()
    free_x=int((w_x-p_x-8)/x_rel)
    free_y=int((w_y-p_y-31)/y_rel)
    #print(free_x,free_y)
    buts=[[None for _ in range(c)] for _ in range(b)]
    lei=[[0 for _ in range(c)] for _ in range(b)]
    #埋雷
    for i in range(0,d):
        x,y=mailei(b,c,lei,free_x,free_y)
        lei[x][y]=9
        if x-1>=0:
            if lei[x-1][y]!=9:
                lei[x-1][y]+=1
        if x-1>=0 and y+1<c:
            if lei[x-1][y+1]!=9:
                lei[x-1][y+1]+=1
        if y+1<c:
            if lei[x][y+1]!=9:
                lei[x][y+1]+=1
        if x+1<b and y+1<c:
            if lei[x+1][y+1]!=9:
                lei[x+1][y+1]+=1
        if x+1<b:
            if lei[x+1][y]!=9:
                lei[x+1][y]+=1
        if x+1<b and y-1>=0:
            if lei[x+1][y-1]!=9:
                lei[x+1][y-1]+=1
        if y-1>=0:
            if lei[x][y-1]!=9:
                lei[x][y-1]+=1
        if x-1>=0 and y-1>=0:
            if lei[x-1][y-1]!=9:
                lei[x-1][y-1]+=1
    #再次初始化
    
    for i in range(0,b):
        for j in range(0,c):
            buts[i][j]=Button(a,relief=RAISED,bg='#d3fbfb',command=lambda:run(a,b,c,buts,lei,f,d))
            buts[i][j].place(relx=(1/b)*i,rely=(1/c)*j,relwidth=1/b,relheight=1/c)
    for i in range(0,b):
        dele(e[i])
    a.update()
    global number
    number=b*c-d
    a.after(1,pa.click(w_x,w_y))
#
def run(a,b,c,d,e,f,num):
    a.update()
    x_rel=int(f)
    y_rel=int(f)
    p_x=a.winfo_x()
    p_y=a.winfo_y()
    w_x,w_y=pa.position()
    true_relx=int((w_x-p_x-8)/x_rel)
    true_rely=int((w_y-p_y-31)/y_rel)
    content=str(e[true_relx][true_rely])
    #sys
    #global permission
    #permission=[[False for _ in range(c)] for _ in range(b)]   
    global number    
 
    if content=='9':
        #permission[true_relx][true_rely]=True
        txt_inner1=Image.open('\\image\\mine.png')
        txt_inner1=txt_inner1.resize((f, f),Image.LANCZOS)
        txt_inner1=ImageTk.PhotoImage(txt_inner1)
        dele(d[true_relx][true_rely])
        txt1=Label(a,image=txt_inner1)
        txt1.place(relx=(1/b)*true_relx,rely=(1/c)*true_rely,relwidth=1/b,relheight=1/c)
        a.update()
        a.after(600)
        page5_defeat(a)
    elif content=='0':
        dele(d[true_relx][true_rely])
        txt=Label(a,bg='#FFFFFF')
        txt.place(relx=(1/b)*true_relx,rely=(1/c)*true_rely,relwidth=1/b,relheight=1/c)
        number=number-1
        #print(number)
        '''
        #自动点击
        if true_relx-1>=0 and permission[true_relx-1][true_rely]==False:
            pa.click(w_x-f,w_y)
            permission[true_relx-1][true_rely]=True
        if true_relx-1>=0 and true_rely+1<c and permission[true_relx-1][true_rely+1]==False:
            pa.click(w_x-f,w_y+f)
            permission[true_relx-1][true_rely+1]=True
        if true_rely+1<c and permission[true_relx][true_rely+1]==False:
            pa.click(w_x,w_y+f)
            permission[true_relx][true_rely+1]=True
        if true_relx+1<b and true_rely+1<c and permission[true_relx+1][true_rely+1]==False:
            pa.click(w_x+f,w_y+f)
            permission[true_relx+1][true_rely+1]=True
        if true_relx+1<b and permission[true_relx+1][true_rely]==False:
            pa.click(w_x+f,w_y)
            permission[true_relx+1][true_rely]=True
        if true_relx+1<b and true_rely-1>=0 and permission[true_relx+1][true_rely-1]==False:
            pa.click(w_x+f,w_y-f)
            permission[true_relx+1][true_rely-1]=True
        if true_rely-1>=0 and permission[true_relx][true_rely-1]==False:
            pa.click(w_x,w_y-f)
            permission[true_relx][true_rely-1]=True
        if true_relx-1>=0 and true_rely-1>=0 and permission[true_relx-1][true_rely-1]==False:
            pa.click(w_x-f,w_y-f)
            permission[true_relx-1][true_rely-1]=True
        '''
    else:
        dele(d[true_relx][true_rely])
        txt=Label(a,text=content,bg='#FFFFFF',fg='#000000',font=('黑体',f,'bold'))
        txt.place(relx=(1/b)*true_relx,rely=(1/c)*true_rely,relwidth=1/b,relheight=1/c)
        #permission[true_relx][true_rely]=True
        number=number-1
        #print(number)
    if number==0:
        page5_win(a)
#
def page5_win(a):
    a.destroy()
    win= Tk()
    win.title('扫雷')
    #sys
    win.iconbitmap('\\image\\tubiao1.ico')
    win.config(background='#D3D3D3')
    b=win.winfo_screenwidth()
    c=win.winfo_screenheight()
    b=int((b-600)/2)
    c=int((c-400)/2)
    win.geometry('400x300+%d+%d'%(b,c))
    win.resizable(0,0)
    txt1=Label(win,text='恭喜，你赢了！',bg='#D3D3D3',fg='#FF0000',font=('黑体',35,'bold'),justify='center')
    txt2=Label(win,text='不愧是你，要不要再来一局？',bg='#D3D3D3',fg='#000000',font=('黑体',17),justify='center')
    but1=Button(win,text='再来一局',font=('黑体',15,'bold'),relief=RAISED,bg='#d3fbfb',command=lambda:page2(win,(txt1,txt2,but2,but1)))
    but2=Button(win,text='结束游戏',font=('黑体',15,'bold'),relief=RAISED,bg='#d3fbfb',command=lambda:page_end(win,(txt1,txt2,but1,but2)))
    txt1.place(relx=0.1,rely=0.05,relwidth=0.9,relheight=0.3)
    txt2.place(relx=0,rely=0.35,relwidth=1,relheight=0.2)
    but1.place(relx=0.1,rely=0.7,relwidth=0.3,relheight=0.2)
    but2.place(relx=0.6,rely=0.7,relwidth=0.3,relheight=0.2)
    while True:
        win.update()
#
def page5_defeat(a):
    a.destroy()
    defeat= Tk()
    defeat.title('扫雷')
    #sys
    defeat.iconbitmap('\\image\\tubiao1.ico')
    defeat.config(background='#D3D3D3')
    b=defeat.winfo_screenwidth()
    c=defeat.winfo_screenheight()
    b=int((b-600)/2)
    c=int((c-400)/2)
    defeat.geometry('400x300+%d+%d'%(b,c))
    defeat.resizable(0,0)
    txt1=Label(defeat,text='很可惜，\n你踩到了地雷！',bg='#D3D3D3',fg='#FF0000',font=('黑体',30,'bold'),justify='center')
    txt2=Label(defeat,text='失败乃成功之母，要不要再来一局？',bg='#D3D3D3',fg='#000000',font=('黑体',15),justify='center')
    but1=Button(defeat,text='再来一局',font=('黑体',15,'bold'),relief=RAISED,bg='#d3fbfb',command=lambda:page2(defeat,(txt1,txt2,but2,but1)))
    but2=Button(defeat,text='结束游戏',font=('黑体',15,'bold'),relief=RAISED,bg='#d3fbfb',command=lambda:page_end(defeat,(txt1,txt2,but1,but2)))
    txt1.place(relx=0.1,rely=0.05,relwidth=0.9,relheight=0.3)
    txt2.place(relx=0,rely=0.35,relwidth=1,relheight=0.2)
    but1.place(relx=0.1,rely=0.7,relwidth=0.3,relheight=0.2)
    but2.place(relx=0.6,rely=0.7,relwidth=0.3,relheight=0.2)
    while True:
        defeat.update()
#
def page_end(a,b):
    dele(b)
    txt1=Label(a,text='感谢游玩，\n希望你能喜欢这款游戏\n并提出宝贵的改进建议。',bg='#D3D3D3',fg='#FF0000',font=('黑体',20),justify='center')
    txt2=Label(a,text='--Tiger',bg='#D3D3D3',fg='#00BFFF',font=('黑体',20),justify='center')
    txt1.place(relx=0,rely=0.15,relwidth=1,relheight=0.3)
    txt2.place(relx=0.6,rely=0.5,relwidth=0.3,relheight=0.1)
    but=Button(a,text='好的',font=('黑体',15,'bold'),relief=RAISED,bg='#d3fbfb',command=out)
    but.place(relx=0.3,rely=0.7,relwidth=0.4,relheight=0.2)
#main
a= Tk()
a.title('扫雷')

us.creat()
a.iconbitmap('\\image\\tubiao1.ico')
a.config(background='#D3D3D3')
a.resizable(0,0)
page1(a)