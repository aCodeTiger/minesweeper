from tkinter import *

def test(a):
    if a<8:
        raise ValueError
def run(self,b):
    a=inp1.get()
    try:
        a=int(a)
    except ValueError:
        c='必须输入整数!'
        b.insert(END,c)
        return None
    try:
        test(a)
    except ValueError:
        c='整数必须大于8!'
        b.insert(END,c)
        return None
    b.insert(END,a)
    self.mainloop()

a= Tk()
a.title('tiger')
a.geometry('400x400')
inp1=Entry(a)
inp1.place(relx=0.2,rely=0.1,relheight=0.1,relwidth=0.3)
c1=Button(a,text='Enter',command=lambda:run(a,c2))
c1.place(relx=0.3,rely=0.3,relheight=0.1,relwidth=0.2)
c2=Text(a)
c2.place(relx=0.0,rely=0.5,relheight=0.3)
a.mainloop()