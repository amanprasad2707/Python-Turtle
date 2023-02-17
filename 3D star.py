import turtle
colors=["silver","grey","black"]
colorss=["grey","black","silver"]
draw=turtle.Pen()
turtle.bgcolor('white')
draw.speed(1000)
draw.hideturtle()
for a in range(400):
    draw.pencolor(colors[a%3])
    draw.width(a/100+2)
    draw.forward(a)
    draw.left(-180)
    draw.right(30)
turtle.exit()