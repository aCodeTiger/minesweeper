from tkinter import *
def f1():
    b=inp1.get()
    b='    input:'+b+'\n'
    c2.insert(END,b)
    inp1.delete(0,END)
a= Tk()
a.title('tiger')
a.geometry('400x400')
inp1=Entry(a)
inp1.place(relx=0.2,rely=0.1,relheight=0.1,relwidth=0.3)
c1=Button(a,text='Enter',command=f1)
c1.place(relx=0.3,rely=0.3,relheight=0.1,relwidth=0.2)
c2=Text(a)
c2.place(relx=0.0,rely=0.5,relheight=0.3)
a.mainloop()