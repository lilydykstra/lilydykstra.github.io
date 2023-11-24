"""
Pygame Startere Code
ATLS 1300/5650

Author: YOUR NAME(S)
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
WHITE = (255,255,255) # some handy RGB values
BLACK = (0,0,0)



#================================ Animation loop ===================================================
# start values defined here
running = True
clock = pygame.time.Clock() # for framerate timing

while running:
    # clear window (comment out to have trace behind animation)
    win.fill(BLACK)
    
    # This loop allows windows when exit is clicked.
    # Do not change, remove or augment this loop...yet.
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False # stops animation
                
    #================== Your animation tasks ================
    # call functions, increment values
    
    # stop conditional would go here too
    
    
    #================== Animation control ===================
    pygame.display.update()
    clock.tick(30) # framerate in fps (30-60 is typical)

# pygame.display.quit() # uncomment to automatically close window at end of animation    