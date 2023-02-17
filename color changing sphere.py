import turtle as t
import random
import colorsys
t.bgcolor("black")
t.speed("fastest")
t.pensize(1)
t.tracer(20)
hue=0.0
t.hideturtle()
for i in range(50):
    x=random.randint(0,0)
    y=random.randint(0,0)
    t.penup()
    t.goto(x,y)
    t.pendown()
    size=random.randint(10,300)
    for i in range(37):
        color=colorsys.hsv_to_rgb(hue,1,1)
        t.pencolor(color)
        hue+=0.005
        t.fd(size)
        t.bk(size)
        t.lt(13)
        t.rt(40)
        t.circle(150)
t.mainloop()