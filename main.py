import turtle

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


  s = turtle.Screen()
  s.bgcolor("Black")
  s.tracer(0)


  while True:
    t.clear()
    show_circle(t, "white", "white", 25)
    s.update()
    t.forward(0.1)



