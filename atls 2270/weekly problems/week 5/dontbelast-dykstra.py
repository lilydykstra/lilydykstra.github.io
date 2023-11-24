# ## starter input output code
with open('notlast.in') as read:
	raw = {} # dictionary
	for _ in range(int(read.readline())):
		name, amt = read.readline().split()
		amt = int(amt)
		if name not in raw:
			raw[name] = 0
		raw[name] += amt
cows = [(amt, name) for name, amt in raw.items()] # nested list with all the cows names and amount of milk produced
# print(cows)

cows.sort() # sorting the lists in the list by the value of their first element

min_cow = cows[0][0] # assigning the minimum cow to the smallest value in the list 

min_count = 0  # instantiating the count for number of cows with a minumum value, so we can index the second minimum

for n in cows: # for each cow in the list of cows
    if n[0] == min_cow: # if the first value of the list its on is equal to the lowest cow
        min_count += 1 # add 1 each time there is a cow with the min value

if (min_count < len(cows)): # if the amount of cows with the minimum value is less than the lenght of the list
     # and if the cow next to our second min has a greater value (not a tie), or if the second minumum is the last cow in the lsit
    if (cows[min_count][0] < cows[min_count + 1][0]) or (min_count == len(cows)): 
        ans = cows[min_count][1] # answer is equal to the cow at minimum count value index 1
elif len(cows) == 1: # if the length of the cows list is equal to 1
    ans = cows[0][1] # our second minimum is just that one cows name, since others are considered 0
else: # if not we have a tie
    ans = "Tie"

# print(ans)

written = open('notlast.out', 'w')
written.write(ans)