from typing import NamedTuple

class DisjointSets:
  def __init__(self, size: int) -> None:
    # initialize an array for parents and sizes, both of 'size' number of 1s and 'i's
    self.sizes = [1 for _ in range(size)]
    self.parents = [i for i in range(size)] 

  # method to find the root/parent that the element of the given value 'x' belongs to
  def find(self, x:int) -> int:
    # if the parent of x is x, then x is a root itself
    if self.parents[x] == x:
      return x
    # otherwise, continue to recursively find the parent of x until we find the root
    self.parents[x] = self.find(self.parents[x])
    return self.parents[x]
  

  # method to unite two values 'x' and 'y' by drawing an edge between them
  def union(self, x:int, y:int) -> bool:
    # find the roots of x and y
    x_root = self.find(x)
    y_root = self.find(y)

    # if the roots of x and y are already the same, then no need to unite them
    if x_root == y_root:
      return False
    
    # merge the smaller component into the larger component
    if self.sizes[x_root] < self.sizes[y_root]:
      x_root, y_root = y_root, x_root 
    
    # set the parent of y's root to be x's root, and update the size of x's component
    self.sizes[x_root] += self.sizes[y_root]
    self.parents[y_root] = x_root

    # return True to indicate that a union operation was performed
    return True


class Edge(NamedTuple):
    # defines our input below as integers
    # represents the indexs of the points we are checking
	a: int
	b: int
    # represents the distance between the points
	dist: int


with open("moocast.in") as read:
	n = int(read.readline()) # number of cows
    # making empty lists for our x and y coordinates to
	x = []
	y = []
    
    # reading in our coordinates of each cow 
	for i in range(n):
		x_i, y_i = [int(i) for i in read.readline().split()]
        # appending our x and y coordinates as we read them in to our lists 
		x.append(x_i) 
		y.append(y_i)
# making an empty list to track our edges
edges = []
# print('x',x)
# print('y',y)

# for each cow
for i in range(n):
    # for j in the range of out current cow+1 to our total number of cows
	for j in range(i + 1, n):
        # calculating the distacne between the coordinates of cow i and cow j
		dx = x[i] - x[j]  
		dy = y[i] - y[j]
        # append to our list tracking Edge objects, where an Edge object is the connection between two points
		edges.append(Edge(i, j, dx**2 + dy**2)) # i and j are the index of the points it connects, and then the distance between is calculated
# print(edges)
edges.sort(key=lambda e: e.dist) # sorts our edges by distance value
# print(edges) 

last_dist = 0 # will track last distance value we use to union two points
component_num = n # initially setting our number of connected components to our number of cows 
dsu = DisjointSets(n) # instantiating the class with number of cows for out input

# for each edge from 0/first edge to the last edge in our list
for e in edges:
    # if our two points can create a new union
	if dsu.union(e.a, e.b):
        # then our last distance is set to the distance of the edge we are on 
		last_dist = e.dist
        # subtract 1 from out counter for conected c0mponents 
		component_num -= 1
        # when we get to 1 we know they are all connected
		if component_num == 1:
			break
# our last_dist from the last edge we checked is our answer becaus it is when we know everyone is connected by the current minimum distance as we started from the lowest distance and went up
print(last_dist, file=open("moocast.out", "w"))