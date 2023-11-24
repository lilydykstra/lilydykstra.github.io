fin = open('feast.in')
t,a,b = fin.readline().split()

t = int(t)
a = int(a)
b = int(b)

# makes lists to track fullness when bessie drinks water and when she doesn't
seen = [[0]*(t+1)]*2

# print(seen)
seen[0][0] = 1 # adjusting the originial position for possibility of doing nothing 

# loop across rows
for i in range(2):
    # loops across columns
    for j in range(t):
        # if the value we are looking at is not 0, we eat a lemon, eat an orange, drink water
        if seen[i][j] != 0: # if it is a valid starting point/possible solution, we can
            if j+b <= t:
               seen[i][j+b] = 1 # adjusting the position so mark a possible full for eating a lemon
            if j+a <= t:
                seen[i][j+a] = 1 # adjusting the position so mark a possible full for eating a orange
            
            
            if i == 0: # if we are in our first row, we drink water at our possible solutions and append that to our second row
                seen[i+1][j//2] = 1 # divide the location of our current possible solution to get the possible solution when drinking water
# print(seen)

# find rightmost 1 for greatest place we marked a full possibility
iterator = t # set our iterator equal to the length our our rows
while seen[1][iterator] == 0: # while our row including water possibilities at rightmost position is 0, so no possibilities
        iterator -= 1 # we decrement by 1 to find the rightmost position with a 1 there

ans= iterator # our answer is our iterator because that is where we have our rightmost 1

with open('feast.out','w') as f:
    f.write(str(ans))
