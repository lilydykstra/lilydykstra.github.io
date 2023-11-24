with open("milkvisits.in") as read:
	farm_num, query_num = [int(i) for i in read.readline().split()] # number of farms, and visiters
	farms = read.readline() # H or G of farms
	neighbors = [[] for _ in range(farm_num)] # empty list
	# print('neighbors ', neighbors)

	for f in range(farm_num - 1):
		f1, f2 = [int(i) - 1 for i in read.readline().split()]
		# print("f1 f2", f1,f2)
		neighbors[f1].append(f2) # at the value of farm 1 in our empty list, append farm 2
		neighbors[f2].append(f1) # at the value of farm 2 in our empty list, append farm 1
		# print("neigbors ", neighbors)


	queries = []
	for _ in range(query_num):
		query = read.readline().split()
		# print('query', query)
		query[0], query[1] = int(query[0]) - 1, int(query[1]) - 1 # converting it to start at 0
		# print('queries', query)
		queries.append(query)

# print('queries ',queries)
# print('farms ', farms)
# print("farm num ",farm_num)
# print("query num ", query_num)
# print("farms ", farms)
# print("neighbors ", neighbors)


# Process the tree & detect the different components
component_num = 0
component = [-1 for _ in range(farm_num)] # full of -1s to track visiting
# print('component ', component)

for farm in range(farm_num): # each farm in our number of farms

	if component[farm] != -1: # if visited
		continue # skip the rest of the current iteration

	frontier = [farm] # whatever farm we are on
	# print('frontier', frontier)

	curr_type = farms[farm] # current milk we are checking

	while frontier: # while something is in frontier

		curr = frontier.pop() # set equal to current value of frontier, then pop it
		# print("curr ", curr) 

		component[curr] = component_num # visited, no longer -1
		# print('component curr ', component[curr])

		for n in neighbors[curr]: # each component in neighbors
			if farms[n] == curr_type and component[n] == -1: # if current farm has same milk type and is not visited yet
				frontier.append(n) # append current position to frontier

	component_num += 1 # add 1 to show we have exhausted the component, looking at new component 
	# print('component num ', component_num)


# print('component ', component)


with open("milkvisits.out", "w") as written:
	# 1 if the friend is happy, 0 otherwise
	for a, b, milk in queries:  # for farm 1, farm 2, type of milk in queries list
			
			# print('a,b,milk', a,b,milk)
			if component[a] == component[b]: # if components have the same value for each farm location
				print(1 if farms[a] == milk else 0, end="", file=written)
				# if the farms of that component have the same milk as they are asking for print 1, otherwise print 0
			else:
				# if they don't have the same component value
				print(1, end="", file=written) # print 1 because they'll have both types of milk
	print(file=written)
