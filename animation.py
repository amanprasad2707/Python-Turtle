import turtle as t
import colorsys
t.bgcolor('black')
t.speed('fastest')

t.pensize(2)
h=0.0
t.hideturtle()
t.setpos(0,0)
for i in range(2000):
    color=colorsys.hsv_to_rgb(h,1,1)
    t.pencolor(color)
    h+=0.005
    t.fd(i)
    t.bk(i)
    t.rt(64)
    t.lt(90)
    t.tracer(10)
t.exitonclick()
