import pygame, math
pygame.init()

# create a window
w = 600
h = 600
win = pygame.display.set_mode((w,h))
pygame.display.set_caption("ooOOooOOoo")

clock = pygame.time.Clock() # create a clock object that controls frame rate

# DEFINE FUNCTIONS

# function definition STORES task, but doesn't execute
def sinePulse(angle):
    # calculates values between -100 and 100
    return 100 * math.sin(math.radians(angle)) 

def pulse(size, step):
    # oscillate between values of 5 and 100
    if size >= 100 or size <= 5:
        # size hits upper limit (100)
        step *= -1 # changes sign
    else:
        size += step # increment size
    return step


# ANIMATION LOOP SETUP
Step = 5 # increment size for circle growth
size = 80 # start size of circle
x = w/2 # horiz center of screen
y = h/2 # vertical center of screen
t = 0 # start value for circle size
running = True

while running:
    win.fill((0,0,0)) # clears screen of prior drawings
    
    # draw a pulsing circle
    # size = sinePulse(t)
    pygame.draw.circle(win, (255, 0, 0), (x,y), size)
    # t += 5
    size += Step
    Step = pulse(size, Step)

    pygame.display.update() # draw all our images onto surface
    clock.tick(30) # 30 fps
