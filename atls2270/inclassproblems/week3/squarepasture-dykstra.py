file = open("square.in","r")

pasture_1=[int(s) for s in file.readline().split()] # creates an array of the 6,6,8,8 sqaure pasture values
pasture_2=[int(s) for s in file.readline().split()] # creates an array of the 1,8,4,9 sqaure pasture values

highestX = max(pasture_1[0],pasture_1[2],pasture_2[0],pasture_2[2]) # checks what the highest x value is out of both corners and each pasture
lowestX = min(pasture_1[0],pasture_1[2],pasture_2[0],pasture_2[2]) # checks what the lowest x value is out of both corners and each pasture
highestY = max(pasture_1[1],pasture_1[3],pasture_2[1],pasture_2[3]) # checks what the highest y value is out of both corners and each pasture
lowestY = min(pasture_1[1],pasture_1[3],pasture_2[1],pasture_2[3]) # checks what the lowest y value is out of both corners and each pasture

side = max(abs(lowestX-highestX), (abs(lowestY-highestY))) 
# is setting side equal to the highest value between the absolute value of the lowest x value minus the highest x value or the absolute value of the lowest y value minus the highest x value

answer = side * side # is setting answer equal to side multiplied by itself since we want a square pasture

#writing to file
out = open("square.out","w")
out.write(str(answer))
out.close()