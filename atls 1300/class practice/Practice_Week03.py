import turtle

win = turtle.Screen() #we ran the origianl without this. does this jsut specify the height and width?
w = 700
h = 700
win.setup(width=w,height=h)


turtle.Turtle()
# move the turtle forward 50 pixels

turtle.forward(340) #pixels, moves near the edge of the screen
turtle.right(90) #degrees of the turn
turtle.forward(340)

turtle.up() #picks up pen
turtle.goto(-150, -150) #move to lower left quadrant
turtle.stamp()
turtle.goto(-150,150) #move to upper left quardant 
turtle.left(40)

turtle.done()