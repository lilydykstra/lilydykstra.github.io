with open('maxcross.in') as read:
	n, k, b = map(int, read.readline().split())
	seen = [0] * (n + 1) # creating an array of 0s
	left, right = 1, k # assigning 1 to left and k to right
	value = 0
	for _ in range(b):
		seen[int(read.readline())] = 1 # putting 1's where there are broken stoplights

print(n, k, b)
print(seen)

# find the very first prefix sum 
for i in range(left,right+1): # from first value 1 to k
	value += seen[i] # add whatever value we see to the value variable since if it is working it is 0

print(value)
values = [value] # creating a list to append all the future values to

while n > right: # when the rightmost of k is less then the n
	left, right = left + 1, right + 1 # in order to increment the k length check and eventually kick us out
	num = seen[right] - (seen[left-1]) # creating a value with the prefix sum of the new incremented k list
	# print(num)
	value += num # add this value to previous prefix sum value 
	values.append(value) # add this value to the list of our values
	# print(values)

answer = min(values) # find the minimum prefix sum from our list 


print(answer, file=open('maxcross.out', 'w'))