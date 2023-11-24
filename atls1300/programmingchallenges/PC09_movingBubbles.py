'''
Making a clickable bubble game

AUTHOR: Sophie Luu, Lily Dykstra, Kacey Chen
DATE: November 20th, 2022

Summary and How to play:
There are moving bubbles of different sizes and colors. Each time the game runs they show up
at different positons on the screen in different colors. The goal is pop all of them.
To pop them you put your cursor over the bubble and click. Once you have clicked all the bubbles
the game will close and you will be shown "You popped all the bubbles!" in the terminal.

'''
import pygame, random
pygame.init()

# Window
w = 400
h = 400
win = pygame.display.set_mode((w, h))


class Bubble:
    
    def __init__(self, color, x, y):
        # attributes of the bubbles
        self.color = color # color of bubble
        self.radius = 25 # radius/size of bubble
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
        # Store location info for pygame to know where to show the circle
        if(self.draw):
            self.circle = pygame.draw.circle(win, self.color ,(self.x,self.y) , self.radius)

    def move(self):
        # moves the circle around the screeen
        dx = random.randint(-1,1)
        dy = random.randint(-1,1)
        self.x += dx # updating the x position
        self.y += dy # updating the y position
        


# subclass of the Bubble class
class smallBubble(Bubble):
    def __init__(self, color,x,y):
        super().__init__(color,x,y)
        # attribute of the smallBubble class
        self.radius = 15


class Manager:
    def __init__(self):
        # Colors in the random choice palette
        blue = (63, 136, 197)
        yellow = (227, 181, 5)
        purple = (252, 221, 242)
        green = (129, 228, 218)
        red = (255, 27, 28)
        self.palette = blue, yellow, purple, green, red 
    

    # end conditional class. When all the bubbles are no longer showing then the screen closes
    def gameOver(self,circleList,miniList):       
        """ check for end conditions all balls in the list are invisible (self.draw == False for all balls)"""
        for b in circleList:
            if (b.draw):
                return False
        for b in miniList:
            if (b.draw):
                # all ball.draw == False
                return False # stops the method and returns to the main block of code
        return True

   
    def main(self):
        running = True
        self.circleList = [] #objects
        self.miniList = []
        positions = [] #positions

        # makes the lists of bubble objects
        for i in range(10):
            # ranges for the random bubble positions
            x = random.randint(50,w-50)
            y = random.randint(50,h-50)
            x2 = random.randint(50,w-50)
            y2 = random.randint(50,h-50)

            positions.append((x,y)) # generate list of 10 positions
            self.circleList.append(Bubble(random.choice(self.palette),x,y)) # adds a bubble object of random colors at lower y positions each time to the list each loop
            self.miniList.append(smallBubble(random.choice(self.palette),x2,y2)) # adds a bubble object of random colors at lower y positions each time to the list each loop

        while running:
            win.fill((0,0,0))

            # makes the bubbles move
            for b in self.circleList:
                b.move()
            for b in self.miniList:
                b.move()

           # end conditional
            if (self.gameOver(self.circleList,self.miniList)):
                print( "You popped all the bubbles!")
                running = False

            # checks if the bubbles have been clicked
            for event in pygame.event.get():
                for b in self.circleList: # calls each bubble in the circleList 
                    b.checkClick(event) # goes to check the method and see if there was a mousepress

                for b in self.miniList:
                    b.checkClick(event)

                if (event.type == pygame.QUIT):
                    pygame.quit()

    # ========= Add draw tasks here ========= 

        # draws each bubble object from the circleList list and miniList
            for b in self.circleList:
                b.show()
            
            for b in self.miniList: 
                b.show()

            pygame.display.update()

#  ========= Runs the code: ========= 
Manager().main()
