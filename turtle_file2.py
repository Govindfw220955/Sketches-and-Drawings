import turtle
from sketchpy import canvas
sk = canvas.sketch_from_svg("D:\\2023_07_21 (1).svg")
te = turtle.Turtle
t = turtle
t.up()
t.goto(150, -180)
t.down()
t.bgcolor("black")
t.shape("turtle")
color = ["red", "green", "blue", "yellow", "orange", "pink", "violet", "dark red"]
j=0
m=100
for i in range(65):
    t.pencolor(color[j])
    j += 1
    if j==len(color):
        j=0
    t.fd(m)
    m -= 5
    t.lt(90)

t.up()
t.goto(150, 200)
t.down()
t.bgcolor("black")
t.shape("turtle")
color = ["red", "green", "blue", "yellow", "orange", "pink", "violet", "dark red"]
r = 0

n=10
for i in range(100):
    t.pencolor(color[r])
    r += 1
    if r == len(color):
        r = 1
    t.fd(i)
    n += 2
    t.lt(59)
t.fd(20)
t.hideturtle()
t.bgcolor("silver")
sk.draw()
t.done()