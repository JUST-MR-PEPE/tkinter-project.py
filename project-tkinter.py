from tkinter import*
from math import*
wind=Tk()
wind.title('Calculater')
wind.geometry('210x250')
wind.config(background='powder blue')
wind.resizable(0,0)
#functions
#numbers
def Number0():
    Ent.insert('end','0')
def Number1():
    Ent.insert('end','1')
def Number2():
    Ent.insert('end','2')
def Number3():
    Ent.insert('end','3')
def Number4():
    Ent.insert('end','4')
def Number5():
    Ent.insert('end','5')
def Number6():
    Ent.insert('end','6')
def Number7():
    Ent.insert('end','7')
def Number8():
    Ent.insert('end','8')
def Number9():
    Ent.insert('end','9')
#operations
def Addition():
    Ent.insert('end','+')
def Subtraction():
    Ent.insert('end','-')
def Multiplication():
    Ent.insert('end','*')
def Division():
    Ent.insert('end','/')
def Modulation():
    Ent.insert('end','%')
def Root():
    Ent.insert('end','√')
def Point():
    Ent.insert('end','.')
def Inverse():
    Ent.insert('end','1/')
def Clear():
    Ent.delete('0','end')
def Delete():
    Ent.delete(len(Ent.get())-1,'end')
def Result():
    operation = Ent.get()
    root='√'
    if operation.startswith(root) == True:
        operation=operation[1:]
        result = sqrt(int(operation))
    else:
        result = eval(operation)
    Ent.delete('0','end')
    Ent.insert('end',result)

def At_sign():
    value = Ent.get()
    value = -int(value)
    Ent.delete('0','end')
    Ent.insert('end',value)
   
Ent = Entry(wind,bd=3,font=20)
#----numbers-----#
number0=Button(wind,text='0',font=20,command=Number0)
number1=Button(wind,text='1',font=20,command=Number1)
number2=Button(wind,text='2',font=20,command=Number2)
number3=Button(wind,text='3',font=20,command=Number3)
number4=Button(wind,text='4',font=20,command=Number4)
number5=Button(wind,text='5',font=20,command=Number5)
number6=Button(wind,text='6',font=20,command=Number6)
number7=Button(wind,text='7',font=20,command=Number7)
number8=Button(wind,text='8',font=20,command=Number8)
number9=Button(wind,text='9',font=20,command=Number9)
#----operations----#
addition=Button(wind,text='+',font=20,command=Addition)
subtraction=Button(wind,text='-',font=20,command=Subtraction)
multiplication=Button(wind,text='*',font=20,command=Multiplication)
division=Button(wind,text='/',font=20,command=Division)
point=Button(wind,text='.',font=20,command=Point)
modulation=Button(wind,text='%',font=20,command=Modulation)
inverse=Button(wind,text='1/x',font=20,command=Inverse)
result=Button(wind,text='=',font=30,command=Result)
delete=Button(wind,text='CE',font=20,command=Clear)
clear1=Button(wind,text='C',font=20,command=Clear)
atsign=Button(wind,text='<',font=20,command=Delete)
clear=Button(wind,text='+/-',font=20,command=At_sign)
root1=Button(wind,text='√',font=20,command=Root)
#----show----#
Ent.place(x=10,y=10,width=190,height=45)
delete.place(x=10,y=60,width=36,height=30)
clear.place(x=49,y=60,width=36,height=30)
clear1.place(x=88,y=60,width=36,height=30)
atsign.place(x=127,y=60,width=36,height=30)
root1.place(x=165,y=60,width=36,height=30)
#numbers
number7.place(x=10,y=95,width=36,height=30)
number8.place(x=49,y=95,width=36,height=30)
number9.place(x=88,y=95,width=36,height=30)
number4.place(x=10,y=130,width=36,height=30)
number5.place(x=49,y=130,width=36,height=30)
number6.place(x=88,y=130,width=36,height=30)
number1.place(x=10,y=165,width=36,height=30)
number2.place(x=49,y=165,width=36,height=30)
number3.place(x=88,y=165,width=36,height=30)
number0.place(x=10,y=200,width=73,height=30)
#operations
division.place(x=127,y=95,width=36,height=30)
modulation.place(x=165,y=95,width=36,height=30)
multiplication.place(x=127,y=130,width=36,height=30)
inverse.place(x=165,y=130,width=36,height=30)
subtraction.place(x=127,y=165,width=36,height=30)
result.place(x=165,y=165,width=36,height=65)
point.place(x=88,y=200,width=36,height=30)
addition.place(x=127,y=200,width=36,height=30)

wind.mainloop()
