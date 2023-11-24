read = open("pairup.in", "r").readline

n = int(read()) # the number of sets 
cows = [list(map(int, read().split())) for _ in range(n)] # x cows with y output of milk
cows.sort(key=lambda x: x[1]) # sort the pairs within the list

i = 0 # left side
j = n-1 # right side

ans = 0

while i <= j:
    min_cows = min(cows[i][0],cows[j][0]) # the minimum between the left and right values

    if i == j:
        min_cows = min_cows / 2 # divide by two so that we dont end up with -2 at the bottom if i and j are 0 and they both subtract
        
    cows[i][0] = cows[i][0] - min_cows # make the 0 value of the index we are at from the left the value of the left index minus the min cow value
    cows[j][0] = cows[j][0] - min_cows # make the 0 value of the index we are at from the right the value of the right index minus the min cow value
    
    if (cows[i][0] == 0): # if the cows i index are equal to zero after we subtract above we increment by one right
        i += 1
    if (cows[j][0] == 0): # if the cows j index are equal to zero after we subtract above we increment by one left
        j -= 1

    ans = max(ans,cows[i][1]+cows[j][1]) # comparing to previous answers to see the max for rel answer
    

# print(ans)

print(ans, file=open('pairup.out', 'w'))