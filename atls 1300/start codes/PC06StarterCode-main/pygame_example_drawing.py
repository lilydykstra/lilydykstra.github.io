"""
Examples of how to use drawing functions in pygame. Borrowed code from
this script will not count toward your 20% limit. Citation not required.
"""

import pygame
import math
pygame.init() # initialize pygame managers

# create a display window
w = 600
h = 600
win = pygame.display.set_mode((w,h)) # create window

print(win.get_at((0, 0))) # get color at pixel location (x,y)
# returns (r, g, b, a) alpha = transparency

# while loop setup
clock = pygame.time.Clock() # for animation speed
running = True # for animation loop

# color values
black = (0,0,0)
white = (255,255,255)
blue = (0,0,255)

# position & sizing info in 2 WAYS
rect = [0,0,200,300] # [x, y, w, h]

size = (200,300)
rectSurf =  pygame.Surface(size) # makes a rect with same info

while running:
    # draw lines. http://www.pygame.org/docs/ref/draw.html#pygame.draw.line
    # arguments: (surface, color,  startxy, stopxy, linewidth)
    pygame.draw.line(win, white, (0,0), (w,h), 14)
    
    # draw arcs http://www.pygame.org/docs/ref/draw.html#pygame.draw.arc 
    # arguments: (surface, color, rect, start_radian, stop_radian, linewidth)
    pygame.draw.arc(win, white, rect, 0, math.pi/2, 4)
    pygame.draw.arc(win, white, [50,75,200,300], math.pi/2, math.pi, 4)

    # NOTE: holes in line are a result of pygame's drawing algorithm. cannot be changed.

    # draw circle http://www.pygame.org/docs/ref/draw.html#pygame.draw.circle
    # arguments: circle(surface, color, center, radius)
    pygame.draw.circle(win, white, (w/2,h/2), 50) # empty
    pygame.draw.circle(win, blue, (w/2,h/2), 20, 0) # filled

    # drawing parametric pattern (at once, no animation)
    # 1 of 2: solve for all x and y points
    points = [] # empty list
    rad = 100
    centerX = 100
    centerY = 150
    for angles in range(360):
        t = math.radians(angles) # convert to radians
        
        # replace these 2 lines with parametric equation
        x = rad * math.sin(t) + centerX 
        y = rad * math.cos(t) + centerY
    
        points.append((x,y)) # add (x,y) tuple to list

    # 2 of 2: draw using list of points
    # arguments: (surface, color, connect points?, points, linewidth)
    pygame.draw.lines(win, blue, True, points,4)
    
    # animation controls
    clock.tick(60) # 60 fps
    pygame.display.update()
