from collections import deque

with open("perimeter.in") as r:
	t = r.readline
	n = int(t()) # the grid layout 
	ice = [] # the figuration of the blobs
	visited = [[False] * n for _ in range(n)] # false values telling us we havent visited the coordinate yet

	for _ in range(n):
		ice.append(list(t()))

max_area = 0
min_peri = float("inf") # infinity

# possible directions
DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# creating the boundaries to test if it is out of grid
def boundaries(a, b, l):
	if a < 0 or b < 0 or a >= l or b >= l:# if the position is above, below, right, or left of our edges
		return True
	return False

# a, p = 0,0

# finding the area and perimeter function
def area_perimeter(x, y):
	area, perimeter = 1, 0

    # making q, adding our x,y values to it, and making those x,y as visited
	q = deque()
	q.append((x, y)) 
	visited[x][y] = True 

    # while q is true it runs through all our stuff, so when the x,y location is true for out iteration
	while q:
		x, y = q.pop() # remove these values from q

		for dx, dy in DIRECTIONS:
			x2, y2 = x + dx, y + dy # in order to check to the right, left, above, below
			if boundaries(x2, y2, n) or ice[x2][y2] == ".": # if these coordinates are out of bounds, add 1 to perimeter
				perimeter += 1
			else: 
				# if they are in bounds and we havent visited, add 1 to the area, add the values to the beginning of q list, and mark it as visited
				if not visited[x2][y2]:
					area += 1
					q.appendleft((x2, y2)) 
					visited[x2][y2] = True 
					
					# original depth first search code
					# a,p = area_perimeter(x2,y2)
					# area += a
					# perimeter += p
					# print(area)
					# print(perimeter)
	return area, perimeter


for i in range(n):
	for j in range(n):
		if ice[i][j] == "#" and not visited[i][j]:
			# print("new run for i,j")
			area, perimeter = area_perimeter(i, j) # running it each iteration of for loop to go through all coordinates
			if area > max_area: # sets the new area as the max area if greater
				max_area, min_peri = area, perimeter
			elif area == max_area: # if they are currently equal, make the max area the area,
				if min_peri > perimeter:
					max_area, min_peri = area, perimeter  # and make sure we have the lowest perimeter for the max area

print(max_area, min_peri, file=open("perimeter.out", "w"))