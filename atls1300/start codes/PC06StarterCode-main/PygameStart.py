"""
Pygame Startere Code
ATLS 1300/5650

Author: Lily Dykstra
DATE

NOTE: the animation loop is inifinite. You will have to add a conditional
to break the loop, if desired. Infinite looping animation can be used intentionally!

This is a description of what this code does. You should edit this line to get 
full credit on assignments. The code will CONTINUE TO RUN 
(meaning you cannot run it again) until you close the window!
'''"""

import pygame
pygame.init() # initialize pygame managers

# create a window
w = 600
h = 600
win = pygame.display.set_mode((w,h)) # define window variable
# pygame.display.set_caption("Read carefully.") # uncomment & edit to caption the window

#======================== Variables & functions ===================================================
clock = pygame.time.Clock() # for framerate timing

COLOR = (255,255,255) # some handy RGB values
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)

def circle(x,w):
    if x > w:
        x = 0 #redo animation
    # return x

#================================ Animation loop ===================================================
# start values defined here
x = 0 
y= h/2

step = 10

running = True
                
#================== Your animation tasks ================
# call functions, increment values

while running:
    win.fill(BLACK)

    pygame.draw.circle(win, COLOR, (x, y), 50, 0)
    x += step

    circle(x,w)
    # if x > w:
    #     x = 0 #redo animation
    
    pygame.display.update()


    # stop conditional would go here too

    # This loop allows windows when exit is clicked. Do not change, remove or augment this loop...yet.
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False # stops animation
            if event.type == pygame.KEYDOWN:
        # handles key press event (see docs for other types of key events)
                if event.key == pygame.K_b:
                    COLOR = BLUE
                if event.key == pygame.K_r:
                    COLOR = RED
                if event.key == pygame.K_g:
                    COLOR = GREEN
                if event.key == pygame.K_SPACE:
                    COLOR = BLACK
                
    
    #================== Animation control ===================
    pygame.display.update()
    clock.tick(30) # framerate in fps (30-60 is typical)

# pygame.display.quit() # uncomment to automatically close window at end of animation    