from turtle import*
import colorsys
speed(0)
hue=0.0
bgcolor('black')
pensize(2)
for i in range(150):
    col=colorsys.hsv_to_rgb(hue,1,1)
    pencolor(col)
    hue+=0.005
    for j in range(2):
        fd(i*2)
        lt(200)
        fd(i*2)
        rt(100)
        for j in range(2):
            rt(65)
            bk(10)
done()