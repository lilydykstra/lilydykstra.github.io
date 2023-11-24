'''
Making a basic button

AUTHOR:
DATE

Goal:

1. Make a surface (suface can hold images) (buttonFace)
2. Make a box to hold the location & size info (pygame.Rect)
3. Draw button face (& text) onto window surface (blit) 
6. Functions created for drawing (show), and key interaction (key) - call in while loop

'''
import pygame
pygame.init()

# Window
w = 400
h = 400
win = pygame.display.set_mode((w, h))

magenta = (255,0,255)

# make a rectangle Surface & add to window
class Button: # attributes that describe out class button
    def __init__(self, color):
        self.color = color
        self.bw = 100 # box width
        self.bh = 50 # box height
        self.x = w/2
        self.y = h/2-self.bh/2 #makes it so that it is actually at the center
        self.box = pygame.Rect(self.x,self.y,self.bw,self.bh)  # store location info for pygame

        self.face = pygame.Surface((self.bw,self.bh)) # create surface for drawing
        self.face.fill(self.color) # pink colored face

    def show(self):
      win.blit(self.face,(self.x,self.y))

    # key interaction
    def key(self, event, left=pygame.K_LEFT, right=pygame.K_RIGHT):
        '''Controls key interaction for a surface. To be called in event for loop.
          event - pygame event (from for loop)
          surface - pygame surface to draw on (win, buttonFace, etc.)'''
        if (event.type == pygame.KEYDOWN):
            if (event.key == left):
              # left arrow box to left
                if (self.x>self.bw):
                  self.x -= 5
                print('left key press')
            if (event.key == right):
                if (self.x<w):
                  self.x += 5
                print('right key press')                  


def main():
    button = Button(magenta)
    button2 = Button((0,0,255))
    button2.y = 0


    running = True
    
    while running:
        win.fill((0,0,0))
        
        for event in pygame.event.get():
            # ========= Add events here ========= 
            button.key(event)
            button2.key(event, left=pygame.K_a, right=pygame.K_d)

            if (event.type == pygame.QUIT):
                pygame.quit()

        # ========= Add draw tasks here ========= 
        
        button.show()
        button2.show()
        
        
        pygame.display.update()

#  ========= Runs the code: ========= 
main()