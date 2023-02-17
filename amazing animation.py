import turtle as t
import colorsys
t.bgcolor('black')
t.speed('fastest')
t.tracer(10)
t.pensize(2)
h=0.0
t.hideturtle()
t.setpos(0,0)
for i in range(800):
    color=colorsys.hsv_to_rgb(h,1,1)
    t.pencolor(color)
    h+=0.005
    t.fd(i)
    t.rt(160)
    for j in range(2):
        t.fd(i)
        t.rt(130)
t.exitondisplay()