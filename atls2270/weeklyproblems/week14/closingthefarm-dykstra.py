#closing the farm
class DisjointSets:
  def __init__(self, size: int) -> None:
    # initialize an array for parents and sizes, both of 'size' number of -1s
    self.parents = [-1 for _ in range(size)] 
    self.sizes = [1 for _ in range(size)]
  
  # method to find the root/parent that the element of the given value 'x' belongs to
  def find(self, x:int) -> int:
    # if the parent of x is -1, then x is a root itself
    if self.parents[x] == -1:
      return x
    # otherwise, continue to recursively find the parent of x until we find the root
    self.parents[x] = self.find(self.parents[x])
    return self.parents[x]
  
  # method to check if two values 'x' and 'y' are in the same connected component
  def connected(self, x:int, y:int) -> bool:
    # returns True if the roots of x and y are the same when calling find() with our x and y and false if not
    return self.find(x) == self.find(y)

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
    self.parents[y_root] = x_root
    self.sizes[x_root] += self.sizes[y_root]

    # return True to indicate that a union operation was performed
    return True

with open('closing.in') as fin:

    n,m = map(int, fin.readline().split()) # reading in number of barns and number of bidirectional paths
    #graph is a graph representation of the barn, probably in terms of adjacency
    graph = [[] for _ in range(n)] # however many ns we have we get an empty list for each barn in graph list

    # each barn list will have the number of each barn it is connected to
    for _ in range(m): # for each connection in our number of edges
      f,t = map(lambda i: int(i) -1, fin.readline().split()) # 0 indexes them
      graph[f].append(t) # append value of t at position of f
      graph[t].append(f) # append value of f at position of t
    remove_order = [int(fin.readline()) -1 for _ in range(n)] # 0 index and read in the order of our closing the barns 


# we're going to "close" the barn in reverse... so we start with no nodes

open_barns = set() #keeping track of if we've opened a barn
components = 0 # keeping track of how many componentds are connected at a given time
fully_connected = [] # is out farm fully connected or not

dsu = DisjointSets(n) # instantiate the class

# going through our remove order in reverse and check connected components
for node in remove_order[::-1]: # going to go backwords through our list by 1
    components += 1
    for adj in graph[node]: # for adjacent values in our lists
        if adj in open_barns: # if the barn that is adjacent to the barn we are checking is open, check if they are in the same connected component
            if dsu.union(adj,node): # if running dsu.union changes the graph
                components -= 1 
        
    open_barns.add(node) # add this value to open_barns since we have gone through it
    fully_connected.append("YES" if components == 1 else "NO") # YES we are fully connected if we are fully connected, components ==1, and if components is anything else we are not fully connected

# for n in fully_connected[::-1]: # for each yes or no in fully_connected, print each one
#   print(n)

print(*fully_connected[::-1],sep="\n",file=open('closing.out','w')) # goes through the list backwards and adding a line break