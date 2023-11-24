
'''
ATLS 1300
Author: Dr. Z
Spirograph example

READ FIRST! 

How to borrow code

    1. You MUST create a comment that says what the code you're borrowing does
    and where you got it from (ATLS1300 example code). 
    2. You MAY NOT copy this code or use this code as start code. 
    Only take what you need.
    3. Copy the sections between the ======= lines (lines 32-45, and/or, 
                                                    lines 51-70)
    And paste it in your code! 
    
    Do not take what you do not understand!
'''

import math
from turtle import * #import the library of commands that you'd like to use
colormode(255)

Screen().bgcolor('black') # set the background color to black.
PURPLE = (80,80,200)
color(PURPLE) # set the turtle color using RGB values inside of a tuple
width(3)
speed(10) # draw at the fastest speed
up()

#===============================
#Circle spirograph (EASY!)
    
inc = 60 # angle increment between shapes in pattern
numIt = int(360/inc) # the number of iterations to make a complete circle. 
innerCirc = 2 # radius of inner circle
radius = 50 # radius of circles drawn in pattern

# goto(150,150) # center of the pattern

for iteration in range(numIt):
    down()
    circle(radius)
    forward(innerCirc)
    right(inc)    
#=============================== 
# This section allows for clean execution of the code! (Ignore it)
up()    
 
#===============================
#Polygon spirograph (HARD!)

# #set the size, number of sides, and internal angle of your shape that will make your spirograph
# size = 50
# sides = 4 # chage this to change the shape!
# angle = 360/sides

# inc = 10 # angle increment between shapes in pattern
# numIt = int(360/inc) # the number of iterations to make a complete circle. 
# innerCirc = 20 # radius of inner circle

# goto(-100,-50) # center of the pattern

# for iteration2 in range(numIt):
#     down()
#     for iteration1 in range(sides):
#         forward(size)
#         right(angle)
#     up()
#     forward(innerCirc)
#     right(inc)