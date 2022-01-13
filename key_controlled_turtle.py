import turtle
t = turtle.Turtle()
screen = turtle.Screen()
t.shape("turtle")
t.speed(0)

def up_arrow():
  t.forward(10)

def down_arrow():
  t.backward(10)

def left_arrow():
  t.left(10)

def right_arrow():
  t.right(10)

def make_blue():
  t.color("blue")

def make_red():
  t.color("red")

screen.onkey(up_arrow, "Up")
screen.onkey(down_arrow, "Down")
screen.onkey(left_arrow, "Left")
screen.onkey(right_arrow, "Right")
screen.onkey(make_blue, "b")
screen.onkey(make_red, "r")

screen.listen()
