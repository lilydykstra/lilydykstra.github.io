'Bubbles list example'

import pygame, sys, random
from pygame.locals import QUIT

w = 600
h = 600

DISPLAYSURF = pygame.display.set_mode((w, h))


def setup():
    pygame.init()
    # DISPLAYSURF = pygame.display.set_mode((400, 300))
    pygame.display.set_caption('Hello World!')


class Bubble:

    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.click = False

    def clicked(self, mx, my):
        distance = ((self.x - mx)**2 + (self.y - my)**2)**0.5
        #print(distance)
        if (distance <= 10):
            print("click2")
            self.click = True

    def update(self):
        self.y -= 0.1
        #self.x += random.uniform(-1.5, 1.5)
        self.boundary()

    def display(self):
        if (not self.click):
            pygame.draw.circle(DISPLAYSURF, (255, 255, 255), (self.x, self.y),
                               self.size)
    def boundary(self):
        if(self.y< 0):
           self.y= h
        if(self.x< 0):
           self.x= w
        if(self.x> w):
           self.x= 0


listBubbles = []

for i in range(30):
    listBubbles.append(
        Bubble(random.randrange(w), random.randrange(h), random.randrange(10,20)))


def loop():
    while True:
        DISPLAYSURF.fill((255, 0, 0))

        for b in listBubbles:
            b.display()
            b.update()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                mx, my = pygame.mouse.get_pos()
                for b in listBubbles:
                    b.display()
                    b.clicked(mx, my)
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


def main():
    setup()
    loop()


main()