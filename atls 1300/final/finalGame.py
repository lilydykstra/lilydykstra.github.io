'''
GALACTIC EXPEDITION 

AUTHOR: Daniel Guerrero, Lily Dykstra, Kacey Chen, Will Schweikert
DATE: December 9th, 2022

What is the game?:
You are an astronaut traversing through the galaxy trying to collect as
much stardust from shooting stars to complte your journey. Avoid getting
hit by astroids or your journey will end.

Game Play Instructions:
Your goal is to collect all the stars in order to win the game while avoiding
getting hit by asteroids. The game will end with a win screen if you collect all 
the stars and it will end with a lose screen if you collide with an asteroid.

Intended Users and How it Supports Them:
AGE: All ages, but specifically targeted towards younger kids with an interest 
in space and astronomy and students our age that are bored during class and want 
to play a game without their prof noticing.
GENDER: All
ABILITY: Any - since the game is controlled with arrow keys, it is also great for 
those with limited motor control or for those who want to be inconspicuous.
SUPPORT: We coded the game with arrow keys intead of the trackpad so that more users
can have access to the game. All the icons are made with color blind friendly colors 
so that they can still navigate the screen and play the game.

Summary:
You start the game on the begin screen. It will have a description of the game 
and how to start:
You will see flying stars and asteroid. Collect the stars and avoid the asteroids.
Press the space bar to start. Once you get to the next screen use the arrow
keys to control the astronaut.
On the next screen you will see an astronaut that you control with your keys as 
instructed by the previous page. You will move your astronaut to each of the stars
to collect them. 
If you collect all of them you will be directed to the win screenthat tells you:
"Congrats! You collected enough star dust to continue you journey!"
If you collide with an asteroid before you collect all the stars you will be directed 
to a screen that says:
"Oh no! You collided with an asteroid. Sadly, your journey has ended."


'''
import pygame, random
import pygame.mixer as mixer

pygame.init()

# FOR BACKGROUND MUSIC 
# Load music using file name (.mp3 or .wav are usable)
soundfile = "spacemusic.wav" 
mixer.music.load(soundfile)


# Window
w = 600
h = 600
win = pygame.display.set_mode((w, h))
background_image = pygame.image.load("START_SCREEN.png").convert_alpha() #loads the image into the code
background_image = pygame.transform.scale(background_image,(w,h)) # makes the image the same size as the window

win.blit(background_image, (0,0)) # blits the background image to the screen so that we can see it


class Star:
    
    def __init__(self, x, y):
        # attributes of the stars
        self.x, self.y = x,y # coordinates of star
        self.stardraw = True # boolean for show below so we can see the stars
        self.starImg = pygame.image.load("star.png").convert_alpha() # loads the star image into the code with a transparent background
        self.starRect = self.starImg.get_rect() # makes the image a rect
        self.starRect.center = (self.x,self.y) # assigned the center of the star to the (x,y) coordinates determined in main()


    def starShow(self):
        # Store location info for pygame to know where to show the circle
        if(self.stardraw):
            win.blit(self.starImg, self.starRect) # blits the star image onto the screen if draw = True
    
    def starCollide(self,astronautRect):
        # turn off drawing if the star rect collides with the astronaut rect
        if (self.starRect.colliderect(astronautRect)): 
            self.stardraw = False 
    

    def starMove(self):
        # moves the stars around the screeen by -1 or 1 or 0
        dx = random.randint(-1,1) 
        dy = random.randint(-1,1)
        self.starRect.x += dx # updating the x position by dx 
        self.starRect.y += dy # updating the y position by dy
        self.starShow() # calling the show method when the move method is called 


class Asteroid:
    
    def __init__(self, x, y):
        # attributes of the asteroid
        self.x, self.y = x,y # coordinates of asteroid
        self.asteroiddraw = True # boolean for show below so we can see the asteroids
        self.asteroidImg = pygame.image.load("asteroid.png").convert_alpha() # loads the asteroid image into the code with a transparent background
        self.asteroidRect = self.asteroidImg.get_rect() # makes the asteroid image a rect 
        self.asteroidRect.center = (self.x,self.y) # assigned the center of the asteroid to the (x,y) coordinates determined in main()


    def asteroidShow(self):
        # Store location info for pygame to know where to show the circle
        if(self.asteroiddraw):
            win.blit(self.asteroidImg,self.asteroidRect) # blits the asteroid image onto the screen so we can see it if draw = True

    def asteroidCollide(self,astronautRect):
        # turns of drawing for the asteroid when the asteroid rect collides with the astronaut rect
        if (self.asteroidRect.colliderect(astronautRect)): 
            self.asteroiddraw = False 

    def asteroidMove(self):
        # moves the asteroid around the screeen by values from -5 to 5
        dx = random.randint(-5,5)
        dy = random.randint(-5,5)
        self.asteroidRect.x += dx # updating the x position by dx
        self.asteroidRect.y += dy # updating the y position by dy
        self.asteroidShow() # calling the show method when the move method is called 


class Astronaut:

    def __init__(self, x, y):
        # attributes of the asteroid
        self.x, self.y = x,y # coordinates of astronaut
        self.astronautdraw = True # boolean for show below so we can see the astronaut
        self.astronautImg = pygame.image.load("astronaut.png") # loads the astronaut image into the code with a transparent background
        self.astronautRect = self.astronautImg.get_rect() # makes the astronaut image a rect
        self.astronautRect.center = (self.x,self.y) # assigned the center of the astronaut to the (x,y) coordinates determined in main()


    def astronautShow(self): 
        # Store location info for pygame to know where to show the circle
        if(self.astronautdraw):
            win.blit(self.astronautImg,self.astronautRect) #blits astronaut to screen so it is visible if draw = True
  

    # key interaction
    def key(self, event, left=pygame.K_LEFT, right=pygame.K_RIGHT, up=pygame.K_UP, down=pygame.K_DOWN):
        '''Controls key interaction for a surface. To be called in event for loop.
          event - pygame event (from for loop)'''
        if (event.type == pygame.KEYDOWN):
            if (event.key == left) or (event.key==pygame.K_a) and (self.x>10): #moves astronaut left if left arrow key or a is pressed
                self.astronautRect.x -= 5
            if (event.key == right) or (event.key == pygame.K_d) and (self.x<w-self.bw-10): #moves astronaut right if right arrow key or d is pressed
                self.astronautRect.x += 5
            if (event.key == up) or (event.key == pygame.K_w) and (self.y>10): #moves astronaut up if up arrow key or w is pressed
                self.astronautRect.y -= 5
            if (event.key == down) or (event.key == pygame.K_s) and (self.y<w-self.bh-10): #moves astronaut down is down arrow key or s is pressed
                self.astronautRect.y += 5
                
class Manager:

    def starEnd(self,starList,):       
        """ check for end conditions all stars in the list are invisible (self.draw == False for all balls)"""
        for b in starList:
            if (b.stardraw):
                #show the winning screen if all stardust is collected
                return False
        return True

    def main(self):
        # Plays the song at startup
        mixer.music.play()

        running = True
        clock = pygame.time.Clock() 

        # creates an empty lists to be used in the for loops for all the star and asteroid objects and pp
        self.starList = [] 
        self.asteroidList = [] 
        starPositions = [] 
        asteroidPositions = [] 

        # makes the lists of star objects
        for s in range(12):
            # ranges for the random star positions
            x = random.randint(50,w-50)
            y = random.randint(50,h-50)
            starPositions.append((x,y)) # generate list of 10 positions
            self.starList.append(Star(x,y)) # adds a star object lower y positions to the list each loop
            
        # makes the list of asteroid objects
        for a in range(5):
            # ranges for the random asteroid positions
            x = random.randint(50,w-50)
            y = random.randint(50,h-50)
            asteroidPositions.append((x,y)) # generate list of 10 positions
            self.asteroidList.append(Asteroid(x,y)) # adds an asteroid object at lower y positions to the list each loop

 
        man = Astronaut(w/2,h/2) # astronaut start position
        level=0  # sets the level equal to zero for the start 


        # loads the bavkground images for the lose screen, game-play background, and start screen and transforms them to the size of the window
        asteroidEnd = pygame.image.load("asteroidEnd.png").convert()
        asteroidEnd = pygame.transform.scale(asteroidEnd,(w,h)) 

        galaxy = pygame.image.load("galaxy.png").convert() 
        galaxy = pygame.transform.scale(galaxy,(w,h)) 

        starEnd = pygame.image.load("starEnd.png").convert() 
        starEnd = pygame.transform.scale(starEnd,(w,h)) 

        while running:

            # checks if the icons have been clicked
            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN: #space bar initializes game
                    if event.key == pygame.K_SPACE:
                        level += 1 # adds one to level when space bar is clicked

                if (event.type == pygame.QUIT): 
                    pygame.quit()
            
            man.key(event)   # allows the astronaut to move with the keys

            for s in self.starList: # calls each star objects in the starList 
                s.starCollide(man.astronautRect) # goes to check the method and see if there was a collision between the star rect and the astronaut rect

            for a in self.asteroidList: # calls the asteroid objects in the asteroidList
                a.asteroidCollide(man.astronautRect) # checks if the asteroid rects have collided with the astronaut rect
                # may not need method above
                if not a.asteroiddraw: # if asteroiddraw = False then the level equal zero and the end screen is shown
                    level = 0 
                    win.blit(asteroidEnd,(0,0))
                    pygame.display.update()


            if(level==1): # if level is equal to 1 then the galaxy background is shown on the screen

                win.blit(galaxy,(0,0))

                for s in self.starList: # when the level is equal to 1 each star object in the list will have thier move method called
                    s.starMove()
                for a in self.asteroidList:
                    a.asteroidMove() # when the level is equal to 1 each asteroid object in the list will have thier move method called
                man.astronautShow()  # when the level is equal to 1 the astronaut will be shown

            if (self.starEnd(self.starList)): # if the conditions in the starEnd method are met then the win screen will show up
                win.blit(starEnd,(0,0)) 
            
 
    # ========= Add draw tasks here ========= 

        # draws each bubble object from the circleList list and miniList

            pygame.display.update()
            clock.tick(30)

#  ========= Runs the code: ========= 
Manager().main()
