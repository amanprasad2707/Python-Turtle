import turtle as t
t.speed(0)
t.tracer(10)
t.bgcolor('black')
color=('red','yellow','blue','white')
for i in range(800):
    t.pencolor(color[i%4])
    t.pensize(2)
    t.backward(i)
    t.rt(90)
    t.fd(90)
    t.right(120)
t.exitonclick()