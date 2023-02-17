import turtle
a=3
b=300
turtle.bgcolor("black")
turtle.speed(0)
turtle.pencolor("cyan")
turtle.pensize(2)
turtle.penup()
turtle.goto(1,-100)
turtle.pendown()
while True:
    turtle.right(b)
    turtle.forward(a)
    a=22
    b+=1+2006