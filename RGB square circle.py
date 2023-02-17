import turtle as t
import colorsys
t.bgcolor('black')
t.speed(0)
t.tracer(1)
hue=0.0
for i in range(800):
    col=colorsys.hsv_to_rgb(hue,1,1)
    t.pencolor(col)
    hue+=0.005
    t.left(i)
    t.forward(22)
    t.right(i-90)
    t.forward(40)
    t.circle(100-i)
    t.forward(200)