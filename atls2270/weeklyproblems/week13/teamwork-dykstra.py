fin = open('teamwork.in')
# read in the number of cows and number of cows can be on a team
n,k = fin.readline().split()

# convert to integers
n = int(n)
k = int(k)

# read in the cows skill levels based on position
cows = []
for i in range(n):
    cows.append(int(fin.readline()))

# print(n,k)
# print(cows)

# we want to iterate through cows, and keep track of the best sum at that point
# then use that information to determine optimal groupings

dp = [-1] * n
# print(dp)
# makes dp's value at 1 the value that cows is at 1
dp[0] = cows[0]
# print(dp)

# for each cow we have
for i in range(n):
    # if we don't join the cow we are on to a team, then its value remains that of cow[i]
    maximum = cows[i]
    # check the cows around it to see if there is a more optimal cow nearby
    for j in range(i,-1,-1): # start at i, increment by -1, end at -1 ( counts down )

        cr = i - j +1 # cr is the number of cows in the team being considered in an iteration 
        if cr > k: # if we have have more than k cows on the current team 
            break # it is not possible
        maximum = max(maximum,cows[j]) # what cow has the highest skill level in our cr consideration

        # making sure we don't go out of bounds,
        if j == 0: # we got to far left of cows
            dp[i] = max(dp[i], maximum * cr) # at that point in the array, what is the maximum sum we've seen

        else: # if not we compare to (dp[j - 1] + (maximum * cr))
            dp[i] = max(dp[i], dp[j - 1] + (maximum * cr))


with open('teamwork.out','w') as f:
    f.write(str(dp[n - 1])+ '\n') # answer is the index of dp at n-1