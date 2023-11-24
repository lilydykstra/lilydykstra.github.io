'''
Turtle starter code
ATLS 1300/5650
Author: Dr. Z

Author: Lily Dykstra
DATE 9/6/2022

This is a description of what this code does. You should edit this line to get full credit on assignments.
The code will CONTINUE TO RUN (meaning you cannot run it again) when you close the window!
'''

import turtle # import the library of commands that you'd like to use
turtle.colormode(255) # so you can use standar RGB values, 0-255

#Create a panel to draw on. 
win = turtle.Screen()
w = 700 # width of panel
h = 700 # height of panel
win.setup(width=w, height=h) #700 x 700 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

#====================================================== Your code ======================================================

circle = turtle.Turtle()
circle.shape("circle")
circle.forward(100)
circle.circle(200)

#second circle
circle.up()
circle.goto(-100,-100)
circle.down()
circle.color("black",(254, 32, 54)) #pen color is black (outline) and a blue fill
circle.begin_fill()
circle.circle(150)
circle.end_fill()


stripe = turtle.Turtle()
stripe.pensize(10)
stripe.forward(200)

#======= Clean up, required to run properly ======
turtle.done() # nothing should come after this line of code!
