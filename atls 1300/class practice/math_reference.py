import turtle
import math  # import the library of commands that you'd like to use
turtle.colormode(255) # so you can use standar RGB values, 0-255

#Create a panel to draw on. 
win = turtle.Screen()
w = 700 # width of panel
h = 700 # height of panel
win.setup(width=w, height=h) #700 x 700 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

#====================================================== Your code ======================================================

test = turtle.Turtle()

#In the below chunk of code we get a wave which moves very slow. How to make it faster ?

amp = 200   #Amplitude
for i in range(300):
     i = math.radians(i)
     y = amp * math.cos(i+5)
     test.goto(i*5,y)

#It can be made faster by increasing the radians value --> I will be replacing math.cos(i+5) with math.cos(i*10)

amp = 200   #Amplitude
for i in range(300):
     i = math.radians(i)
     y = amp * math.cos(i*10)
     test.goto(i*5,y)

# Now it's faster but we have waves very close to each other. How do we increase the width?
#It could be done by changing the 'x' coordinate value in this code --> replacing test.goto(i*5,y) with test.goto(i*50,y)

amp = 200   #Amplitude
for i in range(300):
     i = math.radians(i)
     y = amp * math.cos(i*10)
     test.goto(i*50,y)

# 3. If we want to make the size/amplitude of the waves bigger or smaller we have to increase or decrease the amp value respectively. Let's make the amplitude smaller. Replacing amp = 200 with amp = 100.

amp = 100   #Amplitude
for i in range(300):
     i = math.radians(i)
     y = amp * math.cos(i*10)
     test.goto(i*50,y)

#======= Clean up, required to run properly ======
turtle.done() # nothing should come after this line of code!
