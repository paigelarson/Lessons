import pygame
from random import randint
from pygame import gfxdraw

pygame.init()


score = 0
total = 0
black = (0,0,0)
white = (255,255,255)
teal = (61, 255, 177)
lavender = (234, 146, 247)

myfont = pygame.font.SysFont('monospace', 50) 


display = {
    "width": 800,
    "height": 600
}

paddle = {
    "width": 200,
    "height": 20,
    "x": 300,
    "y": 580,
    "velocity": 10
}

ball = {
    "radius": 15,
    "y": 30,
    "x": randint(0, display["width"]),
    "velocity": 20
}

# creating a window, and launching our game
window = pygame.display.set_mode((display["width"], display["height"])) # 800 width, 600 height

while True:
  pygame.time.delay(100)
  window.fill(black)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        break

  keys = pygame.key.get_pressed()

  if keys[pygame.K_LEFT]:
    paddle["x"] -= paddle["velocity"]

  if keys[pygame.K_RIGHT]:
    paddle["x"] += paddle["velocity"]

  ball["y"] += ball["velocity"] 

  if ball["y"]+ball["radius"] >= paddle["y"]:
    if ball["x"]>paddle["x"] and ball["x"] < paddle["x"]+paddle["width"]: 
      score+=1
    total+=1
    ball["x"]= randint(0,display["width"])
    ball["y"]= -10

  #pygame.draw.circle(window, teal,( ball["x"] , ball["y"] ), ball["radius"])
  pygame.gfxdraw.filled_circle(window,ball["x"] , ball["y"], ball["radius"],teal)

  pygame.gfxdraw.box(window,(paddle["x"],paddle["y"],paddle["width"],paddle["height"]), lavender )

  textsurface= myfont.render("score: {0}/{1}".format(score,total),False,white)

  window.blit(textsurface,(10,10))

  pygame.display.update() 

pygame.quit() 
