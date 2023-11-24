file = open("speeding.in", "r")

s =  file.readline() # reading the 3,3 number of segments
s = s.split() # turning the string into array, array of two strings
r_segments, b_segments = map(int,s) # turning 3,3 into intergers
r_segment = [0 for i in range(r_segments)] # mapping the number of segments in the road, r_segments = 3
b_segment = [0 for i in range(b_segments)] # mapping the number of segmnets in bessies journey, b_segments = 3

for x in range(r_segments):  # goes through it 3 times through each line of road segment and their speed limit
    r = file.readline() # reading the road segments and their speed limits
    r_segment[x] = [int(s) for s in r.split()] # turning them into integers in an array

for y in range(b_segments): # goes through it 3 times through each line of bessie's segment and their speed
    b = file.readline() # reading the road segments and bessie's speeds
    b_segment[y] = [int(s) for s in b.split()] # turning them into integers in an array

speed_limit = [] # empty array to be appended in the for loop

for r in range(r_segments): # going through each road segment 
    for i in range(r_segment[r][0]): # going to r segment in the array, going to the first item in that individual array and that becomes the range for how many times it loops 
        speed_limit.append(r_segment[r][1]) # adding the speed limit to the array the amount of times of r's first item

b_speed = []

for b in range(b_segments): # going through each of bessie's segments
    for i in range(b_segment[b][0]): # going to item j in the segments, going to the first item in that individual array and that becomes the range for how many times it loops 
        b_speed.append(b_segment[b][1]) # adding the speed limit to the array the amount of times of b's first item

max_difference = 0 
for i in range(100): # runs through a range of 100
    difference = b_speed[i] - speed_limit[i] # subtracts the speed limit from bessies speed to see if it is postive at any value
    if difference > max_difference: 
        # if the new difference we find above is greater than out current max difference then that is now our new max difference
        max_difference = difference

# file writing for USACO
out = open("speeding.out", "w")
out.write(str(max_difference))
out.close()