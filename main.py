import turtle
from random import random

def show_circle(t, color, pencolor, radius):
  t.pencolor(pencolor)
  t.fillcolor(color)
  t.begin_fill()
  t.circle(radius)
  t.end_fill()

if __name__ == '__main__':
  t = turtle.Turtle()
  t.speed(10000)
  t.hideturtle()


  def up():
    t.setheading(90)


def down():
  t.setheading(270)




def left():
  t.setheading(180)






def right():
  t.setheading(0)



s = turtle.Screen()
s.bgcolor("Black")
s.tracer(0)
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 600
RADIUS = 25

s.setup(SCREEN_HEIGHT, SCREEN_WIDTH)
s.listen()
s.onkey(up, 'Up')
s.onkey(down, 'Down')
s.onkey(left, 'Left')
s.onkey(right, 'Right')
s.onkey(up,'w')
s.onkey(down, 's')
s.onkey(left, 'a')
s.onkey(right, 'd')
x = 0
y = 0
step = 0.1
t.setheading(90)


colors = ["white", "red", "orange", "yellow", "green", "blue", "purple"]
ballcolor = "white"
while True:
    t.clear()
    show_circle(t, ballcolor, ballcolor, RADIUS)
    s.update()
    t.forward(step)
    heading = t.heading()
    if heading == 0:
        x = x + step
    elif heading == 180:
        x = x - step
    elif heading == 90:
        y = y + step
    elif heading == 270:
        y = y - step

    print(x, y, heading)

    if x >= SCREEN_WIDTH/2:
      x = -SCREEN_WIDTH/2
      ballcolor = "red"
      t.goto(x, y)
      t.forward(step)

    elif x  <= -SCREEN_WIDTH/2:
        x = SCREEN_WIDTH /2
        ballcolor = "orange"
        t.goto(x, y)
        t.forward(-step)

    if y >= SCREEN_HEIGHT/2:
        y = -SCREEN_HEIGHT / 2
        ballcolor = "yellow"
        t.goto(x, y)
        t.forward(step)

    elif y <= -SCREEN_HEIGHT/2:
        y = SCREEN_HEIGHT / 2
        ballcolor = "green"
        t.goto(x, y)
        t.forward(-step)

