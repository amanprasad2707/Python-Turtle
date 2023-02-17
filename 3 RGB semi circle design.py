from turtle import*
import colorsys
speed(0)
hue=0.0
pensize(3)
bgcolor('black')
for i in range(150):
    col=colorsys.hsv_to_rgb(hue,1,1)
    pencolor(col)
    hue+=0.005
    circle(i,200)
    for j in range(4):
        rt(40)
        circle(i,20)
turtle.exitonclick()