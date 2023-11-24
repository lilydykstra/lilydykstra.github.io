with open('moocast.in') as read:
	cow_num = int(read.readline())
	x = [0 for _ in range(cow_num)] # x coordinate of the cows
	y = [0 for _ in range(cow_num)] # y coordinate of the cows
	p = [0 for _ in range(cow_num)] # power of the cows walkies
  
  # assigning the values of each for the iterations
	for c in range(cow_num):
		x[c], y[c], p[c] = [int(i) for i in read.readline().split()]

# print(cow_num)
# print(x)
# print(y)
# print(p)

cows_connected = [[False for _ in range(cow_num)] for _ in range(cow_num)] # makes all falses to have something to edit later
# print(cows_connected)

# finding if the cow is within the powers of the main cows reach, and if it is make that value true, otherwise it stays false
for i in range(cow_num):
  for j in range(cow_num):
    cows_connected[i][j] = ((x[i]-x[j])**2 + (y[i]-y[j])**2) <= (p[i]**2) # hypotenuse between the cows <= power

# print(cows_connected)

# recursive function looking at each layers layer to see how many are connected to cow c through thr power
def reachable_cows(c): # goes through each cow and their nested cows
  global visited
  visited[c] = True # visited shows what we have and have not checked, so saying it is true we have visited cow c
  reached = 1 
  for nc in range(cow_num): # for the cow within a cows list
    if not visited[nc] and cows_connected[c][nc]: # if we have not visited the cow within the cow we are on, meaning its False
      visited[nc] = True # visited is now true for that cow
      reached += reachable_cows(nc) # add that cow to the reached variable 
  return reached 


max_cows=0

for c in range(cow_num): # for each cow within the cow we are on
	visited = [False for _ in range(cow_num)] # visited will be false for each cow to reset for the next cow go through
	max_cows = max(max_cows, reachable_cows(c)) # our max cow will be the maximum value between our reachable cow and current max

# print(max_cows)
print(max_cows, file=open('moocast.out', 'w'))