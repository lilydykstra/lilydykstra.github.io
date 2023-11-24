'''
Author: Elle Kartchner, Lily Dykstra
Date: 10/14/22

Description:
create a circle of circles that follow will follow a continuous gradient for PC06- akin to a loading screen.

'''
import pygame, math
pygame.init()

# create a window
w = 600
h = 600
win = pygame.display.set_mode((w,h)) # set window to size (w x h)

# set up clock for animation
clock = pygame.time.Clock() # animation control


# x = 200
# y = 200
running = True

def circle():
    rad = 20
    scale = 6.5
    k = 0
    for t in range(360):
        angle = math.radians(t) #convert to radians
        X = (rad * math.sin(angle)) * scale
        Y = (rad * math.cos(angle)) * scale
        if(t == k):
            k += 30
            pygame.draw.circle(win,(255,255,255),(X+w/2,Y+h/2),rad,0) # drawing white filled circle at (0, h/2)
        pygame.display.update() # draws everything to window
        clock.tick(30)
    return k
    
k = print(circle())

while running:
    circle()
    if k > 720: #have to figure out how to get k defined outside of the function variable
        running = False