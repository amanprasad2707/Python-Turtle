import turtle as t
t.speed(0)
t.tracer(2)
t.setpos(0,0)
t.bgcolor("black")
color=('red', 'steel blue','white')

for i in range(400):
    
    t.fillcolor(color[1%3])
    t.pensize(2)
    t.begin_fill()
    t.fd(i)
    t.rt(160)
    for j in range (3):
        t.fd(i)
        t.rt(190)
    t.end_fill()
t.exitonclick()