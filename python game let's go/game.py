from tkinter import *
import keyboard
import time
import random
import itertools

menu=False
run=True
window=Tk()
window.configure(background='black')
window.state('zoomed')

score=0
speedx=1
speedy=1
balls_x=random.randint(0,1000)
balls_y=random.randint(100,200)
ball=Label(window,width=2,height=1,background='white')
racket=Label(window,width=30,background='red')
rackets_y=700
rackets_x=10

x1=0
x2=150
x3=300
x4=450
x5=600
x6=750
x7=900
x8=1050
x9=1200
x10=1350

y1=0
y2=50

text=Label(window,text='You lost, to try again press R')
text1=Label(window,text='Congratulations you won, press Q to quit')
label1=Label(window,width=20, height=2,background='red')
label2=Label(window,width=20,height=2,background='red')
label3=Label(window,width=20, height=2,background='red')
label4=Label(window,width=20,height=2,background='red')
label5=Label(window,width=20, height=2,background='red')
label6=Label(window,width=20,height=2,background='red')
label7=Label(window,width=20, height=2,background='red')
label8=Label(window,width=20,height=2,background='red')
label9=Label(window,width=20, height=2,background='red')
label10=Label(window,width=20,height=2,background='red')
label11=Label(window,width=20, height=2,background='red')
label12=Label(window,width=20,height=2,background='red')
label13=Label(window,width=20, height=2,background='red')
label14=Label(window,width=20,height=2,background='red')
label15=Label(window,width=20, height=2,background='red')
label16=Label(window,width=20,height=2,background='red')
label17=Label(window,width=20, height=2,background='red')
label18=Label(window,width=20,height=2,background='red')
label19=Label(window,width=20, height=2,background='red')
label20=Label(window,width=20,height=2,background='red')


ylist1=[label1,label3,label5,label7,label9,label11,label13,label15,label17,label19]
ylist2=[label2,label4,label6,label8,label10,label12,label14,label16,label18,label20]
all_list=[label2,label4,label6,label8,label10,label12,label14,label16,label18,label20
,label1,label3,label5,label7,label9,label11,label13,label15,label17,label19,ball,racket]


list=[y1,y2]
list2=[x1,x2,x3,x4,x5,x6,x7,x8,x9,x10]
list3=[x1,x2,x3,x4,x5,x6,x7,x8,x9,x10]
racket.place(x=rackets_x,y=rackets_y)
def start():
    global text
    global menu
    global score
    global rackets_x
    global rackets_y
    global speedx
    global speedy
    global balls_x
    global balls_y
    global ylist1
    global ylist2
    global all_list
    global list
    global list2
    global list3
    ball=Label(window,width=2,height=1,background='white')
    racket=Label(window,width=30,background='red')
    rackets_y=700
    rackets_x=10
    menu=False
    label1.place(x=x1,y=y1)
    label2.place(x=x1,y=y2)
    label3.place(x=x2,y=y1)
    label4.place(x=x2,y=y2)
    label5.place(x=x3,y=y1)
    label6.place(x=x3,y=y2)
    label7.place(x=x4,y=y1)
    label8.place(x=x4,y=y2)
    label9.place(x=x5,y=y1)
    label10.place(x=x5,y=y2)
    label11.place(x=x6,y=y1)
    label12.place(x=x6,y=y2)
    label13.place(x=x7,y=y1)
    label14.place(x=x7,y=y2)
    label15.place(x=x8,y=y1)
    label16.place(x=x8,y=y2)
    label17.place(x=x9,y=y1)
    label18.place(x=x9,y=y2)
    label19.place(x=x10,y=y1)
    label20.place(x=x10,y=y2)
    ylist1=[label1,label3,label5,label7,label9,label11,label13,label15,label17,label19]
    ylist2=[label2,label4,label6,label8,label10,label12,label14,label16,label18,label20]
    all_list=[label2,label4,label6,label8,label10,label12,label14,label16,label18,label20
    ,label1,label3,label5,label7,label9,label11,label13,label15,label17,label19,ball,racket]


    list=[y1,y2]
    list2=[x1,x2,x3,x4,x5,x6,x7,x8,x9,x10]
    list3=[x1,x2,x3,x4,x5,x6,x7,x8,x9,x10]

    global run
    score=0
    speedx=1
    balls_x=random.randint(0,1000)
    balls_y=random.randint(100,200)
    print(balls_x,balls_y)
    speedy=1
def s():
    global text
    global menu
    global score
    global rackets_x
    global rackets_y
    global speedx
    global speedy
    global balls_x
    global balls_y

    balls_x+=speedx
    balls_y+=speedy
    second_x=rackets_x+200
    ball.place(x=balls_x,y=balls_y)
    if balls_y<=80 and balls_y>40:

        for x,z in zip(list2,ylist2):
            if balls_x==x+150 or balls_x==x:
                speedx=-speedx
                z.place_forget()
                ylist2.remove(z)
                list2.remove(x)
                score+=1
            elif balls_x>x and balls_x<x+150:
                speedy=-speedy
                z.place_forget()
                ylist2.remove(z)
                list2.remove(x)
                score+=1
    elif balls_y<=30:
        for x,z in zip(list3,ylist1):
            if balls_x==x+150 or balls_x==x:
                speedx=-speedx
                z.place_forget()
                ylist1.remove(z)
                list3.remove(x)
                score+=1
            if balls_x>x and balls_x<x+150:
                speedy=-speedy
                z.place_forget()
                ylist1.remove(z)
                list3.remove(x)
                score+=1

    if balls_y==rackets_y:
        if  balls_x>rackets_x and balls_x<second_x:
            speedy=-speedy
    elif balls_x>=1530:
        speedx=-speedx
    elif balls_y<=0:
        speedy=-speedy
    elif balls_x<=0:
        speedx=-speedx
    elif balls_y>=800:
        menu=True
        text.place(x=500,y=300)
        for x in all_list:
            x.place_forget()
    elif score==20:
        menu=True
        speedx=0
        speedy=0
        text1.place(x=500,y=300)
def motion(event):
    global rackets_x
    rackets_x = event.x
    racket.place(x=rackets_x)
def quit(event):
    window.destroy()
start()
def menue(event):
    global text
    text.place(x=1000,y=20000)
    if menu==True:
        text.place_forget()
        text1.place_forget()
        start()
        return
    else:print("you didn't lost yet")
    return
while run:
    window.bind('<Motion>', motion)
    window.bind('<q>',quit)
    window.bind('<r>',menue)
    s()
    rackets_y=700
    time.sleep(0.00001)
    window.update()
window.mainloop()
