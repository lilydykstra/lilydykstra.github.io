with open('div7.in') as read:
	cows = [int(read.readline()) for _ in range(int(read.readline()))]
# print(cows)

# prefix sum
cows_psum = [0]
for i in range(len(cows)): # for the length of the cows list
	# print(cows_psum) 
	# print(cows_psum[i] )
	cows_psum.append((cows_psum[i] + cows[i])%7) # append each prefix sum to the list and simultaneously divide by 7

# print(cows_psum)


storage_ph = [-1,-1,-1,-1,-1,-1,-1] # create a storage placeholder full of -1
max_value = 0

for v, k in enumerate(cows_psum): # the v is the index and the k is the modulo value in cows_psum
	# values = []
	if storage_ph[k] == -1: # if there is a -1 at the location of the value we are checking
		storage_ph[k] = v # then we make that value the value of the index location
	else: # if the value is already there
		max_value = max(max_value, v - storage_ph[cows_psum[v]]) # the max is the difference between the two values's index if there is multiple

# print(max_value)
print(max_value, file=open('div7.out', 'w'))