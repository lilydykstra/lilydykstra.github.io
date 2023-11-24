with open("berries.in") as read:
	# reading in number of berry trees (n) and number of baskets (k)
	n, k = map(int, read.readline().split())
	# reading in the number of berries each tree has 
	berries = [*map(int, read.readline().split())]

print('n',n)
print('k',k)
print('berries',berries)

# initialize our answer of max berries bessie can get as 0
max_berries = 0

# going through i in range 1 to the max amount of berries any of the trees have +1 (add one so we don't divide y zero)
for i in range(1, max(berries) + 1):

	mod = i # mod is whatever out iterator is on (number of berries bessie will get per basket)
	full_baskets = 0  # number of full baskets
	leftover = 0 # the number of berries leftover after baskets are full

	# for each tree in all the berry trees
	for tree in range(n):
		# how many full baskets can be made from our current tree, which is the berries of the tree floor divided by i/mod
		full_baskets += berries[tree] // mod

	# if full_baskets value is less than half the total baskets, then if so we can't fill all the baskets and we stop the iteration
	if full_baskets < k / 2:
		break

	# if full_baskets is greater than or equal to k (number of baskets), we have enough berries to fill all the baskets
	if full_baskets >= k:
		# max_berries equals the maximum amount of berries that bessie can have
		max_berries = max(max_berries, (k // 2) * i)
		continue
	
	bessie_baskets = full_baskets - k // 2 # number of full baskets bessie gets (half remainin baskets after filling elsie's baskets)
	bessie_idx = bessie_baskets * i # number of full baskets Bessie gets multiplied by the size of each basket(i)

	# sorts berries list by mod so Bessie can get the maximum amount of leftovers
	berries.sort(key=lambda x: (x % mod), reverse=True)

	# calculates maximum amount of leftovers Bessie can take
	# while leftover is less than whatever total baskets-full baskets is 
	while leftover < (k - full_baskets):
		# if leftover is less than the amount of trees we have 
		if leftover < len(berries):
			# bessies index will get the remainder of the berry at leftover index moduloed by mod and increment leftover
			bessie_idx += berries[leftover] % mod
			leftover += 1
		# if none of those things happen break out of the iteration
		else:
			break

	# answer is the max between previous answer and the value for bessies index
	max_berries = max(max_berries, bessie_idx)

print(max_berries, file=open("berries.out", "w"))