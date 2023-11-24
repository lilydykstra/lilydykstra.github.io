'''
Turtle starter code
ATLS 1300
Author: Dr. Z

Author: Lily Dykstra
DATE: 

DESCRIPTION:
By choosing this start code, you are choosing to use a Ada Lovelace as your background 
for drawing. 

You must make sure all images you reference in the code is in the same folder as this script!
'''

import turtle #import the library of commands that you'd like to use

turtle.colormode(255)

# Create a panel to draw on. 
win = turtle.Screen()
w = 750 # width of panel
h = 750 # height of panel
win.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Ada's image to it
win.bgcolor("#89909f") #EC 2. Used a HEX value to set a color
bgImg = "FullAda_Glam.gif"
stampImg = "JustAda_Glam.gif"
win.addshape(stampImg) # Now you can use Ada's image as a stamp. USE THE DOCS.

win.bgpic(bgImg) # sets the background to the selected image.
#Comment out the line above to remove the image from background

#=======Add your code here======



#=======Clean up code (do not change)======
# this code ensures that your script runs correctly each time.
turtle.done()
