# USACO setup
with open('pails.in') as fin:
	buck_x, buck_y, milk_order = map(int, fin.readline().split())  # buck_x = bucket X, buck_y = bucket Y

outvar = 0

# find the max amount of x's to use, go through all of bucket 1
for first in range(milk_order + 1): # first is where we are in the range function (the iterator variable), the +1 makes sure it goes to 77 since it starts at 0
    x_current = (buck_x * first) # our current best answer is value of bucket x multiplied by what iteration we are on
    if x_current > milk_order: # if the current best answer is greater than we need for the order, break out of the if conditional
        break # we want to stop these comparisons fully once it gets larger than the order
    
    for second in range(milk_order+1): # second is where we are in the range function (the iterator variable), the +1 makes sure it goes to 77 since it starts at 0
        y_current = x_current + (buck_y * second) # first will remain consistent as second checks all Y values
        if y_current > milk_order: # makes sure it doesn't keep going and going until it is greater than what we need
            break # once our combination of x and y gets greater than the order, we go back up and increment X by one
# at this point we have all the combinations of X and Y that are less than or equal to M
        outvar = max(outvar, y_current) # keeps track of the max value we find with these combinations


#outvar should be the final value output
print(outvar, file=open('pails.out', 'w'))
