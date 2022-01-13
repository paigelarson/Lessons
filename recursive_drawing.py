import pygame

black    = (   0,   0,   0)
white    = ( 255, 255, 255)
green    = (   0, 255,   0)
red      = ( 255,   0,   0)

def recursive_draw(x, y, width, height, count):

    pygame.draw.line(screen,
                     black,
                     [x + width*.25,height//2+y],
                     [x + width*.75,height//2+y],
                     3)
    pygame.draw.line(screen,
                     black,
                     [x+width*.25,(height*.5)//2+y],
                     [x+width*.25,(height*1.5)//2+y],
                     3)
    pygame.draw.line(screen,
                     black,
                     [x + width*.75,(height*.5)//2+y],
                     [x + width*.75,(height*1.5)//2+y],
                     3)

    if count > 0:
        count -= 1
        recursive_draw(x, y, width // 2, height // 2, count)
        recursive_draw(x + width // 2, y, width // 2, height // 2, count)
        recursive_draw(x, y + width // 2, width // 2, height // 2, count)
        recursive_draw(x + width // 2, y + width // 2, width // 2, height // 2, count)


pygame.init()
size = [700, 700]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Recursive Drawing")

done = False

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True 

    screen.fill(white)

    fractal_level = 3
    recursive_draw(0, 0, 700, 700, fractal_level)

    pygame.display.flip()

    clock.tick(20)

pygame.quit()
