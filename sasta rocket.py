import turtle as t
import colorsys

t.bgcolor("black")
t.speed('fastest')
t.pensize(2)
t.tracer(10)
h=0.0
t.hideturtle()
t.setpos(0,0)
for i in range(600):
    color=colorsys.hsv_to_rgb(h,1,1)
    t.fillcolor(color)
    h+=0.005
    t.begin_fill()
    t.fd(i)
    t.circle(40)
    t.right(120)
    t.end_fill()
t.exitonclick()