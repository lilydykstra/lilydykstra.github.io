with open('angry.in', 'r') as infile:
	n, k = map(int, infile.readline().split()) # n is number of hay bales k is humber of cows we want
	bales = [int(infile.readline()) for _ in range(n)]
bales.sort()

left = bales[0] # left is the location of the first bale
right = bales[-1]-bales[0] # right is the location of the last bale


while left < right: # while our left position is less than our right 

	radius = (right+left)//2 # radius is the right plus left divided by two for the midpoint to start
	print("radius is " + str(radius))

	blast1 = -float("inf") # makes our blast1 -infinity to keep it from being greater than radius
	cows = 0 # initialize our cows

	for x in bales: # each number in our bales list

		if abs(x -blast1) > radius: # if the absolute value of our bale position - our blast1 is greater than our radius
			cows += 1 # add one to cows 
			blast1 = x + radius # and we make our blast1 now the bale position + out radius

	if cows > k: # if our number of cows needed is greater than our k value
		left = radius + 1 # our left is now radius + 1 to assign a new leftmost value
	else: # if our number of cows is less than k
		right = radius # our rightmost value now becomes our radius

	print("cows is " + str(cows))

print(radius)
print(n, k)
print(bales)
 
ans = left # the answer is the last left position we had

print(ans, file=open('angry.out', 'w'))