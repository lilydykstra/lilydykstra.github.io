with open('perimeter.in') as r:
	t = r.readline 
	n = int(t()) # the grid layout, n x n
	ice = [] # the figuration of the blobs
	visited = [[False] * n for _ in range(n)] # false values telling us we haven't visited the coordinate yet
	
	for _ in range(n):
		ice.append(list(t()))

max_area = 0
min_peri = float('inf') # infinity


# creating the boundaries
def boundaries(a,b,l):
	if a < 0 or b < 0 or a >= l or b >= l: # if the position is above, below, right, or left of our edges
		return True
	return False			


directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

a, p = 0,0

# find area and perimeter:
def area_perimeter(x,y):
	# print("new area_perimeter calculation. X,Y ", x, y)
	global directions, a, p
	area , perimeter = 1,0
	# going through all the coordinates
	# print("x,y: " , x,y)
	visited[x][y] = True # marking this coorinate as we have checked it
	for dx,dy in directions:
		x2, y2 = x + dx, y + dy # checking to the right, left, above, below
		# print(x2,y2)
		# print(boundaries(x2,y2,n))
		if boundaries(x2,y2,n) or ice[x2][y2] == '.': # if these coordinates are out of bounds, add to perimeter
			perimeter += 1 
		else:
			if not visited[x2][y2]: # if they are in bounds and we havent visited, add 1 to the area
				visited[x2][y2] = True
				a,p = area_perimeter(x2,y2)
				area += a
				perimeter += p
				# print(area)
				# print(perimeter)
	return area, perimeter 


for i in range(n):
	for j in range(n):
		if ice[i][j] == '#' and not visited[i][j]:
			# print("new run for i,j")
			area, perimeter = area_perimeter(i, j) # dont know whwere exactly to call since its different than
			# print("area: ", area, "perimeter: ", perimeter)
			if area > max_area: # sets the new area as the max area if greater
				max_area = area
				min_peri = perimeter
			elif area == max_area: # if they are currently equal, make the max area the area,
				if min_peri > perimeter:
					max_area = area
					min_peri = perimeter  # and make sure we have the lowest perimeter for the area

print(max_area, min_peri, file=open('perimeter.out', 'w'))