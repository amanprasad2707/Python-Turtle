import turtle as t
import random
import colorsys
t.bgcolor('black')
t.speed('fastest')
t.pensize(2)

hue=0.0
t.hideturtle()
t.setpos(0,0)
for i in range(2000):
        color=colorsys.hsv_to_rgb(hue,1,1)
        t.pencolor(color)
        hue+=0.005
        t.fd(i)
        t.bk(i)
        t.rt(64)
        t.lt(73)
        t.circle(40)
        t.tracer(30)
        
        
t.exitonclick()