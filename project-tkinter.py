from tkinter import *
#import datetime
#x=datetime.datetime.now
wind=Tk()
wind.title('@ calicatrise @')
wind.geometry('210x250')
wind.config(background='powder blue')

Ent = Entry(wind,bd=3,font=20)
Ent.place(x=10,y=10,width=190,height=45)
#-----------Button 1
b_1=Button(wind,text='<',font=20)
b_1.place(x=10,y=60,width=36,height=30)
#-----------Button 2
b_2=Button(wind,text='CE',font=20)
b_2.place(x=49,y=60,width=36,height=30)
#-----------butt3
b_3=Button(wind,text='C',font=20)
b_3.place(x=88,y=60,width=36,height=30)
#------------Butt4
b_4=Button(wind,text='+/-',font=20)
b_4.place(x=127,y=60,width=36,height=30)
#------------Butt4
b_5=Button(wind,text='√',font=20)
b_5.place(x=165,y=60,width=36,height=30)
#**********************************
#----button 1
bu_1=Button(wind,text='7',font=20)
bu_1.place(x=10,y=95,width=36,height=30)
#-----------Button 2
bu_2=Button(wind,text='8',font=20)
bu_2.place(x=49,y=95,width=36,height=30)
#-----------butt3
bu_3=Button(wind,text='9',font=20)
bu_3.place(x=88,y=95,width=36,height=30)
#------------Butt4
bu_4=Button(wind,text='/',font=20)
bu_4.place(x=127,y=95,width=36,height=30)
#------------Butt4
bu_5=Button(wind,text='%',font=20)
bu_5.place(x=165,y=95,width=36,height=30)
#********************************************
#----button 1
but_1=Button(wind,text='4',font=20)
but_1.place(x=10,y=130,width=36,height=30)
#-----------Button 2
but_2=Button(wind,text='5',font=20)
but_2.place(x=49,y=130,width=36,height=30)
#-----------butt3
but_3=Button(wind,text='6',font=20)
but_3.place(x=88,y=130,width=36,height=30)
#------------Butt4
but_4=Button(wind,text='*',font=20)
but_4.place(x=127,y=130,width=36,height=30)
#------------Butt5
but_5=Button(wind,text='1/x',font=20)
but_5.place(x=165,y=130,width=36,height=30)
#----------
#*******************
#----button 1
butt_1=Button(wind,text='1',font=20)
butt_1.place(x=10,y=165,width=36,height=30)
#-----------Button 2
butt_2=Button(wind,text='2',font=20)
butt_2.place(x=49,y=165,width=36,height=30)
#-----------butt3
butt_3=Button(wind,text='3',font=20)
butt_3.place(x=88,y=165,width=36,height=30)
#------------Butt4
butt_4=Button(wind,text='-',font=20)
butt_4.place(x=127,y=165,width=36,height=30)
#------------
butt_5=Button(wind,text='=',font=30)
butt_5.place(x=165,y=165,width=36,height=65)
#**************** 
but1=Button(wind,text='0',font=20)
but1.place(x=10,y=200,width=73,height=30)
#-----------butt3
but2=Button(wind,text='.',font=20)
but2.place(x=88,y=200,width=36,height=30)
#------------Butt4
but3=Button(wind,text='+',font=20)
but3.place(x=127,y=200,width=36,height=30)



wind.mainloop()
