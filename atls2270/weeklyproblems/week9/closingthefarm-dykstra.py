import sys

sys.stdin = open("closing.in", "r")
read = open("closing.in", "r").readline
sys.stdout = open("closing.out", "w")

n, m = map(int, read().split())
# print(n, m)

adj, order = {}, [] # in order to figure out the connections between the barns
for i in range(1, n + 1): # we are going 1 to 4 and throwing an empty list into our dictionary
	adj[i] = []
# print(adj)

visited, closed = [False] * (n+1), [False] * (n+1) # estsblishing a False to keep or change when we check if we've visited the farm
nodes = 0 # nodes is the number of nodes we visit on that iteration of dfs
# print(visited)
# print(closed)

# read in adjacency list, store the relationship between barns, edges
for i in range(m): 
	a, b = map(int, read().split()) # look through each line, and map the two numbers to a and b
	# then append those values to adj dictionary at the key values of a and b
	adj[a].append(b) 
	adj[b].append(a)
	# print(adj)

for i in range(n):
	order.append(int(read()))
	
# print(order)
# print(adj)
	
def dfs(node):
	global nodes 
	if visited[node] or closed[node]: # if this farm in visited or in closed 
		return # kick us out we are done
	
    #visit this node if it isn't closed and we haven't visited yet
	nodes += 1 # keeping track of how many we can visit
	visited[node] = True # true marks we visited it

	for u in adj[node]: # for u at the position in adj of the node
		if not visited[u]: # if its not visited
			dfs(u) # run dfs function again

#The farm is initially connected if we've visited every node before any of the farms are closed.
dfs(1)
print("YES") if nodes == n else print("NO")

# we see the falses turning to true from this loop, will have a dummy false at 1, will get up to closing the barns and checking the conditions to print YES or NO
for i in range(n-1):
	visited = [False] * (n+1) # reset all visited to False so we can go through it again
	nodes = 0 # reset nodes to 0
	closed[order[i]] = True # whatever order i we now reset to be True, saying that it is a closed barn
	dfs(order[n-1]) # we've started closing the barns, so we run dfs each time on the barn will close last


    # have we visited all unclosed barns?
	if nodes == n - i - 1: # 
		print("YES")
	else:
		print("NO")
