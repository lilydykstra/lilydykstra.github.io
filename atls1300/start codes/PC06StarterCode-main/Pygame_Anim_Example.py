"""
Animates a circle (that wraps around the screen), draws a
square (2 ways shown), and includes 
"""

import pygame, math
pygame.init() # initialize pygame managers

# create a window
w = 600
h = 600
win = pygame.display.set_mode((w,h)) # create window

# colors
white = (255,255,255)

# do the task
win.fill((0,0,0)) # set background to black 

def square():
    """draws a square 100 pixels wide"""
    X = w/2
    Y = h/2
    size = 100
    # version 1
    # pygame.draw.line(win, white, (X,Y),(X+size,Y),4)
    # pygame.draw.line(win, white, (X+size,Y),(X+size,Y+size),4)
    # pygame.draw.line(win, white, (X+size,Y+size),(X,Y+size),4)
    # pygame.draw.line(win, white, (X,Y+size),(X,Y),4)
    
    # version 2
    pygame.draw.rect(win, white, (X,Y,size, size),4)

def checkEdge(x,w):
    """loops x pposition if x is greatre than 
    the window width + shape width"""
    if x > w + 50:
        return 0
    else:
        return x

def main():
    # start coordinates & conditions
    running = True
    x = -w/2 # start coordinates
    y = h/2
    step = 5
    angle = 0
    clock = pygame.time.Clock()

    while running:
        win.fill((0,0,0)) #fill background
        pygame.draw.circle(win, (255,255,255),(x, y), 100)
        square()
        x += step # increment x poosition
        x = checkEdge(x,w)

        clock.tick(60) # pauses execution (ms)
        pygame.display.update() # update window

main()
pygame.display.quit()

