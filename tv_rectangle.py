import pygame
from random import randint

black = (0,0,0)
white = (255,255,255)
random = (randint(0,255),randint(0,255),randint(0,255))

pygame.init()
 
size = [700, 500]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("TV Rectangle")

done = False

clock = pygame.time.Clock()

rect_x = 50
rect_y = 50

rect_change_x = 5
rect_change_y = 5

while done == False:
    for event in pygame.event.get(): 
      if event.type == pygame.QUIT: 
        done = True 
    
    screen.fill(black)

    random = (randint(0,255),randint(0,255),randint(0,255))
    pygame.draw.rect(screen, white, [rect_x, rect_y, 50, 50])
    pygame.draw.rect(screen, random, [rect_x + 10, rect_y + 10, 30, 30])
 
    rect_x += rect_change_x
    rect_y += rect_change_y

    if rect_y > 450 or rect_y < 0:
        rect_change_y = rect_change_y * -1
    if rect_x > 650 or rect_x < 0:
        rect_change_x = rect_change_x * -1
    
    clock.tick(20)

    pygame.display.flip()
    pygame.display.update()

pygame.quit()

