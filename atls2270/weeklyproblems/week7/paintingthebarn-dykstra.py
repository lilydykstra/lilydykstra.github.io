WIDTH = 1000

barn = [[0 for _ in range(WIDTH + 1)] for _ in range(WIDTH + 1)] # make a list of lists where it is filed with width amount of 0s
with open('paintbarn.in') as read:
	rect_num, paint_req = [int(i) for i in read.readline().split()] # number of rectangles and optimal coats is read in to these values
	for _ in range(rect_num):  # going 0,1,2 for the optimal coats
		start_x, start_y, end_x, end_y = [int(i) for i in read.readline().split()] # for each rectange we give it, read in the coordiantes of lower left and upper right
		# Set up the prefix sums array with all the corners of the given rectangle
		barn[start_x][start_y] += 1 
		barn[start_x][end_y] -= 1 
		barn[end_x][start_y] -= 1
		barn[end_x][end_y] += 1

# print(rect_num,paint_req)
# # print(barn)
valid_area = 0

for x in range(WIDTH +1): # each row(x) we go through each cell(y)
	for y in range(WIDTH + 1): # going through each cell comparing to the x values/row
		# calculates the preix sum by row
		if x > 0:
			barn[x][y] +=  barn[x-1][y]# whatever cell we are at is greater than 0, add the value of the previous x cell
		if y > 0:
			barn[x][y] += barn[x][y-1] # whatever cell we are at is greater than 0, add the value of the previous y cell
		if x > 0 and y > 0:
			barn[x][y]-= barn[x-1][y-1] # if both are equal to zero, subtract the previous value of both x and y cell
		valid_area += barn[x][y] == paint_req # if the value at the end of the loop of barn[x][y] is equal to the paint_req, then add that value to the valid_area

# print(barn)
# print(valid_area)

print(valid_area, file=open('paintbarn.out', 'w'))