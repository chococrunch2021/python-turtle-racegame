

from turtle import *
from tkinter import messagebox
from random import randint


colors=["red","gold","blue","green","pink","orange","purple"]


def stars():
    s=Turtle()
    s.speed(0)
    s.color("yellow")
    for j in range(40):
        s.up()
        s.goto(randint(-300,300),randint(100,300))
        s.down()
        s.begin_fill()
        for i in range(5):
            s.fd(5)
            s.rt(144)
            s.end_fill()


def name():
    n=Turtle()
    n.color("white")
    n.up()
    n.goto(-159,199)
    n.down()
    n.write("Turtle Race Gambling Game",font=('Times New Roman',20,'bold'))
    n.color("#A566FF")
    n.up()
    n.goto(-160,200)
    n.down()
    n.write("Turtle Race Gambling Game",font=('Times New Roman',20,'bold'))
    n.up()
    n.goto(120,-170)
    n.down()
    n.write("Mady by Haerang Choi",font=('Times New Roman',10,'bold'))
    n.hideturtle()
    

def makepath():
    bgcolor("black")
    color("#F6F6F6")
    speed(0)
    penup()
    goto(-200,60)
    for step in range(20):
        write(step,align='center')
        right(90)
        forward(10)
        pendown()
        forward(150)
        penup()
        backward(160)
        left(90)
        forward(20)

    
    #goto(-300,170)
    #pendown()
    #fd(600)
    penup()

    #goto(-30,180)
    #write("접근금지라인")

    
    goto(-300,-135)
    pendown()
    fd(600)
    penup()

    goto(-40,-170)
    write("접근금지라인",font=('Times New Roman',10,'bold'))


def around():
    goto(-200,130)
    shape("turtle")
    for secondstep in range(9):
        pendown()
        stamp()
        right(90)
        penup()
        fd(220)
        pendown()
        left(90)
        stamp()
        penup()
        left(90)
        fd(220)
        right(90)
        if secondstep==8:
            break
        fd(50)

def deco():
    goto(-190,100)
    for thirdstep in range(8):
        pendown()
        dot(10,flower_colors[randint(0,4)])
        right(90)
        penup()
        fd(220)
        pendown()
        left(90)
        dot(10,flower_colors[randint(0,4)])
        penup()
        left(90)
        fd(220)
        right(90)
        fd(51)
        
    hideturtle()



def ready():

    a.penup()
    a.goto(-220,30)
    a.pendown()
    b.penup()
    b.goto(-220,0)
    b.pendown()
    c.penup()
    c.goto(-220,-30)
    c.pendown()
    d.penup()
    d.goto(-220,-60)
    d.pendown()

 
def go():
    speed(3)
    len1=len2=len3=len4=0
    for turn in range(140):
        if turn>=30 and turn<60:
            speed(6)
        elif turn>=60:
            speed(0)
 
        
        case1=randint(1,5)
        case2=randint(1,5)
        case3=randint(1,5)
        case4=randint(1,5)
        a.forward(case1)
        b.forward(case2)
        c.forward(case3)
        d.forward(case4)
        len1+=case1
        len2+=case2
        len3+=case3
        len4+=case4
        z,w=check(len1,len2,len3,len4)
        if z==1:
            return w
            break;

def check(l1,l2,l3,l4):

    flag=0
    winner=0
    if l1>=420 and l2<420 and l3<420 and l4<420:
        messagebox.showinfo("승리자","빨간 거북이 승리")
        flag=1
        winner="1"
        
    elif l2>=420 and l1<420 and l3<420 and l4<420:
        messagebox.showinfo("승리자","노란 거북이 승리")
        flag=1
        winner="2"
    elif l3>=420 and l1<420 and l2<420 and l4<420:
        messagebox.showinfo("승리자","파란 거북이 승리")
        flag=1
        winner="3"
    elif l4>=420 and l1<420 and l2<420 and l3<420:
        messagebox.showinfo("승리자","초록 거북이 승리")
        flag=1
        winner="4"

    if l1>=420 and (l2>=420 or l3>=420 or l4>=420):
        messagebox.showinfo("승리자","공동 우승입니다.")
        flag=1
        winner=choice
        return flag,winner
    elif l2>=420 and (l1>=420 or l3>=420 or l4>=420):
        messagebox.showinfo("승리자","공동 우승입니다.")
        flag=1
        winner=choice
        return flag,winner
    if l3>=420 and (l1>=420 or l2>=420 or l4>=420):
        messagebox.showinfo("승리자","공동 우승입니다.")
        flag=1
        winner=choice
        return flag, winner
    if l4>=420 and (l1>=420 or l2>=420 or l3>=420):
        messagebox.showinfo("승리자","공동 우승입니다.")
        flag=1
        winner=choice
        return flag,winner

        
    return flag,winner

 
def race(c):
    ready()
    player=go()
    if player==choice:
        c+=100
        messagebox.showinfo("현재상태","맞추셨습니다. 현재 코인은 "+str(c)+"입니다")
              
    else:
        c-=100
        messagebox.showinfo("현재상태","틀리셨습니다. 현재 코인은 "+str(c)+"입니다")
        
    return c


flower_colors=["#B2EBF4","#B7F0B1","#FFC19E","#FFA7A7","#D1B2FF"]
base=0
flower=0
def tree(length):
    global base
    global flower
    angle=randint(20,40)
    
    if length>5:
        t.fd(length)
        t.rt(angle)
        tree(length-10)
        t.lt(2*angle)
        tree(length-10)
        if length<base-5:
            t.dot(randint(15,30),flower_colors[flower])
        t.rt(angle)
        t.backward(length)


def celebrate():
    bak=Turtle()
    bak.lt(75)
    bak.fillcolor('#FAF4C0')
    bak.up()
    bak.goto(-290,280)
    bak.down()
    bak.begin_fill()
    bak.circle(30,180)
    bak.end_fill()
    bak.rt(45)
    bak.begin_fill()
    bak.circle(30,180)
    bak.end_fill()
    
    bak.rt(80)
    bak.up()
    bak.goto(300,240)
    bak.down()
    bak.begin_fill()
    bak.circle(30,180)
    bak.end_fill()
    bak.rt(30)
    bak.begin_fill()
    bak.circle(30,180)
    bak.end_fill()


def celebrate2():
    paper=Turtle()
    paper.pensize(3)
    for i in range(10):
        paper.up()
        paper.goto(randint(-320,-150),randint(160,270)) 
        paper.right(45)
        paper.color(flower_colors[randint(0,4)])
        paper.down()
        paper.fd(15)

    for j in range(10):
        paper.up()
        paper.goto(randint(150,320),randint(160,270)) 
        paper.right(45)
        paper.color(flower_colors[randint(0,4)])
        paper.down()
        paper.fd(15)







stars()
name()
celebrate2()
celebrate()


t=Turtle()


t.speed(0)
t.color("brown")
t.lt(45)

for i in range(20):
    t.penup()
    if i<10:
        t.goto(randint(-400,-100),-300)
    else:
        t.goto(randint(100,400),-300)
    if i==10:
        t.lt(90)
    t.pendown()
    flower=randint(0,4)
    t.pensize(randint(2,6))
    base=randint(30,40)
    tree(base)
makepath()
deco()





a=Turtle()
a.color("#FF0000")
a.shape('turtle')

 
b=Turtle()
b.color("#FFE400")
b.shape('turtle')


c=Turtle()
c.color("#0054FF")
c.shape('turtle')

d=Turtle()
d.color("#1DDB16")
d.shape('turtle')
coin=200

while True:
    choice=textinput("배팅","입찰할 선수를 선택하시오(번호입력)\n\n 1.red turtle\n2.yellowturtle\n3.blue turtle\n4.green turtle\n\n(한 건당 100코인 차감)")
    if choice==None:
        messagebox.showinfo("거북이선택","아무도 선택하지 않았습니다. 다시 선택해주세요")
        continue

    if choice=="1":
        messagebox.showinfo("거북이선택","당신은 빨간 거북이를 선택했습니다.")    
    elif choice=="2":
        messagebox.showinfo("거북이선택","당신은 노란 거북이를 선택했습니다.")
    elif choice=="3":
        messagebox.showinfo("거북이선택","당신은 파란 거북이를 선택했습니다.")
    elif choice=="4":
        messagebox.showinfo("거북이선택","당신은 초록 거북이를 선택했습니다.")
        
    coin=race(coin)
    
    if coin>=400:
        messagebox.showinfo("결과","축하합니다. 당신은 이제 부자입니다")
        break;
    elif coin==0:
        messagebox.showinfo("결과","당신은 파산했습니다. 안타깝군요.")
        break;



exitonclick() #게임 끝나고 클릭하면 종료 



    






