from tkinter import Tk, Entry, Button , StringVar
class Calculator:
    def __init__(self,master):
        master.title("Calculator")
        master.geometry('357*420+0+0')
        master.config(bg='gray')
        master.resilable(False,False)

        self.equation=StringVar()
        self.entry_value=''
        Entry(width=17,bg="#fff",front=('Arial Bold',28),textvariable=self.equation).place(x=0,y=0)

        Button(width=11,height=4,text='',relief='flat')

    def show(self,value):
        self.entry_value+=str(value)
        self.equation.set(self.entry_value)
    def clear(self):
        self.entry_value=''
        self.equation.set(self.entry_value)

    def solve(self):
        result=eval(self.entry_value)
        self.equation.set(result)
root = Tk()
calculator=Calculator(root)
root.mainloop()