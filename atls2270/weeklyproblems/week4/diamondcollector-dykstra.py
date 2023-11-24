## starter input/output code

with open('diamond.in') as fin:
	n, k = map(int, fin.readline().split()) # number of diamonds and number it can differ by but not be above
	diamonds = [int(fin.readline()) for _ in range(n)] # list of the sizes of the diamonds
diamonds.sort() # sorts the diamonds in order

globalcounter = 0 # sets the global to zero to instantiate it before we assign a new value later

for s in range(n): # for the s in the range of the number of diamonds (hoarding this value through the rest)
	diamondcounter = 0 # so we have something to increment on later
	for i in range(n): # comparing diamond 0 to all other 0s (comparing these values we are circling through to the value we have from s)
		if (diamonds[s] <= diamonds[i] <= (diamonds[s] + k)): # seeing if the constant is between s value and s+k
			diamondcounter += 1 # if it within that range it is within the right size and we add that to the amount of diamonds bessie can display
	if diamondcounter > globalcounter: # if the diamond counter is greater than our stored global counter
		globalcounter = diamondcounter # then our global counter takes the value of the diamondcounter
		# print(globalcounter)

# #outvar should be the final output the problem expects
print(globalcounter, file=open('diamond.out', 'w'))
