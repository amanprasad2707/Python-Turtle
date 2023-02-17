import turtle as t
import colorsys
t.bgcolor('black')
t.speed('fastest')
t.pensize(2)
h=0.0
t.hideturtle()
for i in range(400):
    color=colorsys.hsv_to_rgb(h,1,1)
    t.pencolor(color)
    h+=0.005
    t.fd(i)
    t.bk(i)
    t.lt(120)
    t.rt(90)
    for j in range(3):
        t.bk(i)
        t.right(120)
        t.forward(100)
        t.right(120)
        t.right(120*2+0.1)
        t.tracer(3)
t.exitonclick()