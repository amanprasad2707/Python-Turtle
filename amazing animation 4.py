import turtle as t
t.speed(0)
t.tracer(10)
t.bgcolor('black')
color=('red','yellow','blue','white')
for i in range(800):
    t.pencolor(color[i%4])
    t.pensize(2)
    
    t.rt(120)
    t.bk(i)
    t.circle(40,60)
    t.fd(60)
    t.right(90)
t.exitonclick()