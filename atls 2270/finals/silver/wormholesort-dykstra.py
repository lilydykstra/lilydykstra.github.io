# Open file for reading
with open("wormsort.in", "r") as file:
    # Read the number of cows and number of wormholes
    num_cows, num_wormholes = map(int, file.readline().split())

    # Read the cows' initial positions
    cow_positions = list(map(int, file.readline().split()))
    cow_positions = [pos - 1 for pos in cow_positions]  # Make the cows 0-indexed
    # print(cow_positions)

    max_width = 0 

    cow_neighbors = [[] for _ in range(num_cows)] # empty list to append to
    # print(cow_neighbors)

    for _ in range(num_wormholes):
        cow1, cow2, width = map(int, file.readline().split())
        # print(cow1,cow2,width)
        cow1 -= 1  # Make the cows 0-indexed
        cow2 -= 1
        # at that cows's position in cow_neightbors, append the cow it connects with and the width of the wormhole
        cow_neighbors[cow1].append((cow2, width))
        cow_neighbors[cow2].append((cow1, width))
        # the running max width is the max of the width's we go through above
        max_width = max(max_width, width)
        # print(width)
        # print(max_width)

    # print(cow_neighbors)
    # print(max_width)

    # Binary search to find the largest minimum wormhole width that allows the cows to be sorted
    min_width = 0 # minimum width of a wormhole
    max_valid_width = max_width + 1 # maximum width that allows us to sort cows, add 1 so we can account for the all values including the max_width
    valid_width = -1 # largest minumum width that allows the cows to be sorted, gets updated in the binary search, if still -1 later there is not wormhole big enough
    
    # while our minimum width of the wormhole is less than or equal to our maximum valid width
    while min_width <= max_valid_width:
        # set mid_width equal to itself + our min_valid width floor divided by 2 to find the middle value to test on
        # we test mid_width at the start of each iteration so we can filter out wormholes with width's less than our mid_width
        mid_width = (min_width + max_valid_width) // 2

        # Find the connected components of the cow graph using only wormholes with width >= mid_width
        cow_components = [-1] * num_cows # makes then all zero to adjust later
        # print(cow_components)
        curr_comp = 0 # our tracker for current connected components
        for cow in range(num_cows): # for each how in out number of cows 
            if cow_components[cow] != -1: # if the cow_component of our current cow is not -1, that means it has been connected
                continue # skip the rest of the code

            # use breadth first search to find connected component 
            frontier = [cow] # setting frontier equal to a list that contains the cow we are on
            # print('frontier', frontier)

            while frontier: # while frontier has a value in it
                curr = frontier.pop() # set curr equal to the value in frontier, then pop that value so frontier is empty
                cow_components[curr] = curr_comp # updating cow_components list to mark it as connected to the current component, making the value at curr index the value of curr_comp
                # print("cow_components", cow_components)
                # print('curr_comp', curr_comp)

                for neighbor, neighbor_width in cow_neighbors[curr]: # for each neighbor and neighbors width in cow_neighbors at index of curr
                    # print('neighbor',neighbor)
                    # print('neighbor_width', neighbor_width)

                    # if the index at neighbors of cow_components is equal to -1 and also neighbor_width is greater or equal to our middle value of width 
                    if cow_components[neighbor] == -1 and neighbor_width >= mid_width: 
                        # then we append the neighbor value to frontier for the next go through
                        frontier.append(neighbor)
            curr_comp += 1 # increment our current connected components tracker by 1

        # Check if all cows in the same initial position belong to the same connected component
        # is_sortable is True if cow_component at index cow is equal to the value of cow_components indexed by the value of cow positons indexed at our cow for each cow in our list of cows
        is_sortable = all(cow_components[cow] == cow_components[cow_positions[cow]] for cow in range(num_cows))
        # print(is_sortable)
        # Update the valid_width and adjust the search range accordingly
        if is_sortable: # if it is sortable, is_sortable = True
            # then our variable for mid_width we make our valid_width and make our new min_width our mid_width +1
            valid_width = mid_width 
            min_width = mid_width + 1
        else: # if it is not sortbale
            # our max_valid_width is now our middle width + 1
            max_valid_width = mid_width - 1

# Open file for writing and output the largest minimum wormhole width that allows the cows to be sorted
with open("wormsort.out", "w") as file:
    file.write(str(-1 if valid_width == max_width + 1 else valid_width) + "\n")