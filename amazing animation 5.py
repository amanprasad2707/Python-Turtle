import turtle as t
import colorsys
t.speed(0)
t.tracer(10)
t.setpos(0,0)
hue=0.0
t.bgcolor("black")
color=('red','cyan',"white")
for i in range(400):
    color=colorsys.hsv_to_rgb(hue,1,1)
    t.pencolor(color)
    hue+=0.005
    t.pensize(2)
    t.rt(i)
    t.circle(120,i)
    t.bk(i)
    t.rt(120)
t.exitonclick()