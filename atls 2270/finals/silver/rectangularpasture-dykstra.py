import sys

# Read in the number of cows 
num_cows = int(sys.stdin.readline().strip())

# instantiate a set to use for later as previously seen x and y coordinates
seen_x, seen_y = set(), set()

# read in the cows x and y coordinates
cows = []
for _ in range(num_cows):
    x, y = map(int, sys.stdin.readline().strip().split())

    # make sure we haven't the x and y of the iteration in out sets before
    assert (x not in seen_x and y not in seen_y)

    # tracking all our x-values and y-values to make sure we havent seen them in previous iterations
    seen_y.add(y) 
    seen_x.add(x) 
    # if we haven't seen them we can add those coordinates to our cows list
    cows.append((x, y)) 

# sort the cows, it goes by x value
cows.sort()
# print('cows',cows)

# compresses the x-coordiantes by creating a dictionary of the key is a x values and the value is the index of that value
reduced_x = {x: i for i, (x, y) in enumerate(cows)}
# print('reduced_x',reduced_x)

# sort the cows by y value
cows.sort(key=lambda c: c[1])
# print(cows)
# compresses the y-coordinates by creating a dictionary of the key is a y values and the value is the index of that value
reduced_y = {y: i for i, (x, y) in enumerate(cows)}
# print('reduced_y',reduced_y)

# print('cows',cows)
# replace the original cow coordinates with the compressed coordinates (reduced_x,reduced_y)
for i, (x, y) in enumerate(cows): # for each index and coordinate in cows
    # the value at the index of current iteration in cows is replaced by the x/y value at reduced_x/y of the curretn x/y coordinate of cows
    cows[i] = (reduced_x[x], reduced_y[y]) 
# Sort the cows by x-coordinate again after adjustment
cows.sort()
# print('cows after sort',cows)
# print('cows',cows)




# making empty lists with number of cows+1 amount of sublists to store the prefix sums of y lines of cows later
less_than_y = [[0] * (num_cows + 1) for _ in range(num_cows)]
greater_than_y = [[0] * (num_cows + 1) for _ in range(num_cows)]
# print('less_than_y',less_than_y)
# print('greater_than_y',greater_than_y)

for cow in range(num_cows): # for each cow we have
    # assign our current y_value for an iteration as the y value of a each cow as we go through
    curr_y = cows[cow][1]
    for x in range(1, num_cows + 1): # for each x from 1 to out number of cows+1
        # find the prefix sum of the number of cows that are less than the current y-coordinate and make that value the value of that postion in less_than_y
        less_than_y[curr_y][x] = less_than_y[curr_y][x - 1] + (cows[x - 1][1] < curr_y)
        # print(less_than_y)
        # find the prefix sum of the number of cows that are greater than the current y-coordinate and make that value the value of that postion in greater_than_y
        greater_than_y[curr_y][x] = greater_than_y[curr_y][x - 1] + (cows[x - 1][1] > curr_y)
        # print(greater_than_y)

total = 0 # start our total at 0

# count the number of aligned rectangles, rectangles between the coordinates we are given
for cow1 in range(num_cows): # for the first cow we are comparing 
    for cow2 in range(cow1 + 1, num_cows): # for the second cow we are comparing (the cow to the right of cow1)
        # our bottom is the minimum between the y positions of the two cows
        bottom = min(cows[cow1][1], cows[cow2][1])
        # print(bottom)
        # top is the maximum between the y positions of two cows
        top = max(cows[cow1][1], cows[cow2][1])
        # find the total number of cows in the bottom region, which is 1 + our prefix sum at cow2+1 position of bottom index - the prefix sum at the cow1 position of bottom
        bottom_total = 1 + less_than_y[bottom][cow2 + 1] - less_than_y[bottom][cow1]
        # find the total number of cows in the top region, which is 1 + prefix sum of cow2+1 - cow1 each at the index of top in greater_than_y
        top_total = 1 + greater_than_y[top][cow2 + 1] - greater_than_y[top][cow1]
        # multiply the two totals to get the number of rectangles that align with cow1 and cow2 and add that to a running total
        total += bottom_total * top_total

# total is current total plus our number of cows+1
total += num_cows + 1

print(total) # print answer
