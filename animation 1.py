import turtle as t
import random
import colorsys
t.bgcolor('black')
t.speed('fastest')
t.tracer(30)
t.pensize(2)
h=0.0
t.hideturtle()

for i in range(50):
    x=random.randint(0,0)
    y=random.randint(0,0)
    t.penup()
    t.goto(x,y)
    t.pendown()
    size=random.randint(10,300)
    for i in range(37):
        color=colorsys.hsv_to_rgb(h,1,1)
        t.pencolor(color)
        h+=0.005
        t.fd(size)
        t.bk(size)
        t.fd(i)
        t.rt(217)
t.mainloop()