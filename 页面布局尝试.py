from tkinter import *
a= Tk()
a.title('tiger')
a.geometry('400x400')
b=[0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
c=[['n']*10]*10
for i in range(10):
  for j in range(10):
    c[i][j]= Label(a,relief=RAISED,bg='#d3fbfb')
    c[i][j].place(relx=b[i],rely=b[j],relheight=0.1,relwidth=0.1)
a.mainloop()