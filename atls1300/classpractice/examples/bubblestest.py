'''
Making a clickacle bubble game

AUTHOR: Sophie Luu, Lily Dykstra, Kacey Chen
DATE: November 17th, 2022

Summary: 
 

How to Play Instructions:


'''
import pygame, random
pygame.init()

# Window
w = 400
h = 400
win = pygame.display.set_mode((w, h))


class Bubble:
    
    def __init__(self, color, x, y):
        self.color = color # color of bubble
        self.radius = 20 # radius/size of bubble
        self.x, self.y = x,y # coordinates of bubble
        self.cordinate = (self.x,self.y)
        self.draw = True # boolean for show below. will be made false when we do click interaction

    def checkClick(self,event):
        # method for clicking the bubble and having the individual one pop
        if event.type == pygame.MOUSEBUTTONDOWN: # if the mouse is pressed down
            mx, my = pygame.mouse.get_pos()
            if pygame.mouse.get_pressed()[0]:
                # check for left mouse button
                if self.circle.collidepoint(mx, my):
                    # check if click is inside the bubble & hide bubble
                    self.draw = False
        
    def show(self):
        # Store location info for pygame
        if(self.draw):
            self.circle = pygame.draw.circle(win, self.color ,(self.x,self.y) , self.radius)

# need to instantiate later in the code
# class smallBubble(Bubble):
#     def __init__(self, color,x,y):
#         super().__init__(color,x,y)
#         self.radius = 10


# haven't called yet or edited. it is from repository
class Timer:
    def __init__(self,countDir=True,time=60,text='0'):
        self.totalTime = time
        self.countDir = countDir # if False, then clock counts up
        self.setToZero(time) # resets clock based on self.countDown

      # text settings
        self.fontSize=30
        self.font = pygame.font.SysFont('Consolas', self.fontSize)
        self.text = text # string to print
            
    def countUp(self):
        seconds=(pygame.time.get_ticks()-self.start_ticks)/1000
        self.currTime = int(seconds)
        return self.currTime  

    def countDown(self):
      self.currTime = self.totalTime-self.countUp()
      return self.currTime      

    def setToZero(self,time=60): 
        self.start_ticks=pygame.time.get_ticks()
        self.currTime = time
class Manager:
    def __init__(self):
        # Colors in the random choice palette
        blue = (63, 136, 197)
        yellow = (227, 181, 5)
        purple = (252, 221, 242)
        green = (129, 228, 218)
        red = (255, 27, 28)
        self.palette = blue, yellow, purple, green, red 
    
        self.circleList = [] #objects
        positions = [] #positions

        self.radius = 20 # radius of the bubbles

        # won't show multiple bubbles
        for i in range(20):
            x = random.randint(0,w)
            y = random.randint(0,h)
            
            positions.append((x,y)) # generate list of 10 positions
            self.circleList.append(Bubble(random.choice(self.palette),x,y)) # adds a bubble object of random colors at lower y positions each time to the list each loop
    
    # doesn't move
    def move(self):
        dx = random.randint(-20,20)
        dy = random.randint(-20,20)
        self.x += dx # updating the x position
        self.y += dy # updating the y position
        
        
        Bubble.x += dx
        Bubble.y += dy
        

        if Bubble.top <= 0 or Bubble.bottom >= h:
            Bubble.y *= -1
        if Bubble.left <= 0 or Bubble.right >= w:
            Bubble.y *= -1

    def gameOver(self):       
        """ check for end conditions all balls in the list are invisible (self.draw == False for all balls)"""
        for b in self.circleList:
            if (Bubble.draw):
                # all ball.draw == False
                return False # stops the method and returns to the main block of code
            return True

   
    def main(self):
        running = True
        
        while running:
            win.fill((0,0,0))

            # end conditional
            for event in pygame.event.get():
                for b in self.circleList: # calls each bubble in the circleList 
                    b.checkClick(event) # goes to check the method and see if there was a mousepress
                # ========= Add events here ========= 
                if (event.type == pygame.QUIT):
                    pygame.quit()

    # ========= Add draw tasks here ========= 


            for b in self.circleList: # draws each bubble object from the circleList list loop
                
                b.show()

            pygame.display.update()

#  ========= Runs the code: ========= 
Manager().main()
