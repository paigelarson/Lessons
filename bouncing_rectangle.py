import pygame
from random import randint

# Define some colors
black = (0,0,0)
white = (255,255,255)
green = (0,255,0)
random = (randint(0,255),randint(0,255),randint(0,255))

pygame.init()
 
# Set the height and width of the screen
size = [700, 500]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("TV Rectangle")

#Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Starting position of the rectangle
rect_x = 50
rect_y = 50

# Speed and direction of rectangle
rect_change_x = 5
rect_change_y = 5

#game loop
while done == False:
    for event in pygame.event.get(): 
      if event.type == pygame.QUIT: # If user clicked close
        done = True # Flag that we are done so we exit this loop
    
    # Set the screen background
    screen.fill(black)
    # Draw the rectangle

    random = (randint(0,255),randint(0,255),randint(0,255))
    pygame.draw.rect(screen, white, [rect_x, rect_y, 50, 50])
    pygame.draw.rect(screen, random, [rect_x + 10, rect_y + 10, 30, 30])
 
    # Move the rectangle starting point        
    rect_x += rect_change_x
    rect_y += rect_change_y

    # Bounce the ball if needed
    if rect_y > 450 or rect_y < 0:
        rect_change_y = rect_change_y * -1
    if rect_x > 650 or rect_x < 0:
        rect_change_x = rect_change_x * -1
    
    # Limit to 20 frames per second
    clock.tick(20)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    pygame.display.update()
    
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()

