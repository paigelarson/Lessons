import turtle
from random import randint

t=turtle.Turtle()
screen=turtle.Screen()
t.penup()


def forward():
  t.fd(16)

def backward():
  t.backward(16)

def up():
  t.left(90)
  t.forward(20)
  t.right(90)
def down():
  t.right(90)
  t.forward(20)
  t.left(90)

def key(key):
  t.write(key)
  t.forward(14)


screen.onkey(lambda:key("a"),"a")
screen.onkey(lambda:key("b"),"b")
screen.onkey(lambda:key("c"),"c")
screen.onkey(lambda:key("d"),"d")
screen.onkey(lambda:key("e"),"e")
screen.onkey(lambda:key("f"),"f")
screen.onkey(lambda:key("g"),"g")
screen.onkey(lambda:key("h"),"h")
screen.onkey(lambda:key("i"),"i")
screen.onkey(lambda:key("j"),"j")
screen.onkey(lambda:key("k"),"k")
screen.onkey(lambda:key("l"),"l")
screen.onkey(lambda:key("m"),"m")
screen.onkey(lambda:key("n"),"n")
screen.onkey(lambda:key("o"),"o")
screen.onkey(lambda:key("p"),"p")
screen.onkey(lambda:key("q"),"q")
screen.onkey(lambda:key("r"),"r")
screen.onkey(lambda:key("s"),"s")
screen.onkey(lambda:key("t"),"t")
screen.onkey(lambda:key("u"),"u")
screen.onkey(lambda:key("v"),"v")
screen.onkey(lambda:key("w"),"w")
screen.onkey(lambda:key("x"),"x")
screen.onkey(lambda:key("y"),"y")
screen.onkey(lambda:key("z"),"z")


screen.onkey(forward,"space")
screen.onkey(backward,"BackSpace")
screen.onkey(up,"Up")
screen.onkey(down,"Down")

screen.listen()
