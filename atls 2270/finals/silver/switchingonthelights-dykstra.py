import sys

sys.setrecursionlimit(100000)  # Raise recursion limit as the default will error

filein = open("lightson.in", "r")
# reading in the number of cows and light switch toggles
# N = number of cows
# m = number of light switch toggles
N, m = map(int, filein.readline().split())
print(N,m)

lit_rooms = 1 # keeps track of the lit rooms, starting with the initial already lit room

# makes lists of Falses for every N to mark cells as visited and illuminated to keep track of lit rooms
visited = [[False for i in range(N)] for j in range(N)]
# print('visited',visited)

illuminated = [[False for i in range(N)] for j in range(N)]
# print('illuminated',illuminated)

# makes an empty list of lists to add the switches to later to keep track of the connected switch's rooms
switches = [[[] for i in range(N)] for j in range(N)]
# print('switches',switches)

# Read in light switches input, so at the switch position, append the cell it can light up
for i in range(m):
	x, y, a, b = map(int, filein.readline().split())
	switches[x - 1][y - 1].append((a - 1, b - 1))  # at position x,y append a,b (subtracting 1 since indexing starts at 0)
# print('switches',switches)


# Checks if a room is connected to the main component/initially lit room
def check_connected(x, y):
	# all the directions we can go from the cell we are in
	dir_x = [-1, 0, 1, 0]
	dir_y = [0, -1, 0, 1]
			
	# for each direction we can go (all the neighbors)
	for i in range(4):
		# our new x and y are now one of the neighbors 
		new_x = x + dir_x[i]
		new_y = y + dir_y[i]

		# if the new neighbor we go to is off the grid, go to next iteration
		if new_x < 0 or new_y < 0 or new_x > N - 1 or new_y > N - 1:
			continue

		# if a neighbor we are on is visited, return true (we mark it as visited in floodfill)
		if visited[new_x][new_y]:
			return True

	# if no neighbors have been visited, return false 
	return False


# floodfill method with source room (x, y) checking all the rooms that can be lit by the switches
def floodfill(x, y):
	global lit_rooms # lit_rooms = 1

	# ignore room if its out of bounds, already visited, or not lit
	if (x < 0 or y < 0 or x > N - 1	or y > N - 1 or visited[x][y] or not illuminated[x][y]):
		return # nothing gets returned


	# if we got false from check_connected (not connected to bessie) for these coordinates and it is not our starting point
	if not check_connected(x, y) and not (x == 0 and y == 0):
		return

	# Set current room to visited
	visited[x][y] = True

	# all the directions we can go from the cell we are in
	dir_x = [-1, 0, 1, 0]
	dir_y = [0, -1, 0, 1]

	# for each direction we can go (all the neighbors) floodfill (recursion) through the neighbors 
	for i in range(4):
		floodfill(x + dir_x[i], y + dir_y[i])


	# for each switch connected to x,y (current room) turn on the lights 
	for i in range(len(switches[x][y])):
		# print('x,y',x,y)
		
		# goes to the switches[x][y] room and assigns the 'i'th connected switch's (x,y) to room_x and room_y
		room_x = switches[x][y][i][0] 
		room_y = switches[x][y][i][1]

		# print('room x,room_y', room_x,room_y)

		# if that connected swtich's corresponding room is false (hasn't been lit yet) add it to count of lit rooms
		if not illuminated[room_x][room_y]:
			lit_rooms += 1

		# set the corresponing room to lit/set that location in illuminated to True
		illuminated[room_x][room_y] = True

		# floodfill (recursion) the new room that is lit to test all rooms this one can reach
		floodfill(room_x, room_y)


# set initial room to lit
illuminated[0][0] = True

# do floodfill function to our initial room
floodfill(0, 0)

print(lit_rooms, file=open("lightson.out", "w"))