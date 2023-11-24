
with open('10.in', 'r') as fin:
    # read the number of dishes
    n = int(fin.readline().strip())

    lines = fin.readlines() # read in all the dishes in bessies stack in order from the top 
    # make sure there are enough dishes in the input file
    if len(lines) < n: # if the length of our stack is less than our number of cows
        exit() # stop this code

    # if we have enough dishes, officially read in the dishes for order list
    order = [int(x) for x in lines[:n]]

# returns True if dishes with indices [0, end_index) can be washed
def prefix_washable(order, end_index):
    not_washed = []  # dishes that have not been washed yet will be added to this list to track later on
    # print('not_washed1', not_washed)
    for i in range(end_index): # for i in range 0 to value of end_index we chose when calling the fucntion
        not_washed.append(order[i]) # append the value of our current dish from the iteration to not_washed
    not_washed.sort() # sort not_washed to be in order

    # print('not_washed2',not_washed)

    # Each list represents a separate soapy stack
    soapy_stacks = []# making the list to append to later

    # for each i in range 0 to whatever we put in for out end_index when calling the function
    for i in range(end_index):
        # print('order', order)
        plate = order[i] # make variable plate as the value of whatever plate we are on inside order
        # print("plate",plate)
        # print(soapy_stacks)
        # binary search for the first stack it can be placed
        left, right = -1, len(soapy_stacks) # left is -1 and right is the current length of our soapy_stacks list, two-pointers for elsies and bessies stacks 
        
        # while our right value -1 is greater than our left value
        while left < right - 1:
            mid = (left + right) // 2 # we create a mid variable that is left+right all floor divided by 2 
            # then if our index of mid value then indexed again at the last value of our mid value list is all greater than our plate value
            if soapy_stacks[mid][-1] > plate:
                right = mid # our right value is now equal to mid's value
            else: # if the above condition is not true and plate is greater
                left = mid # then left is now equal to mid's value

        # not able to be placed in any existing stack
        # if our right value is equal to the length of our current soapy_stacks list
        if right == len(soapy_stacks):
            # create new stack
            soapy_stacks.append([plate]) # append our current plate value inside a list onto soapy_stacks
        else: # if it is not equal
            soapy_stacks[right].append(plate) # appends the value of plate to index of right in soapy_stacks

        # while the plate has not been washed, wash it
        while soapy_stacks and soapy_stacks[0][-1] == not_washed[0]: # while soapy_stacks has a value in it, and the last value soapy_stacks first list is equal to the first value in not_washes
            soapy_stacks[0].pop() # remove that value from its respective list inside soapy_stacks since it is being cleaned
            not_washed.pop(0) # remove that value from not_washed since we are washing it now

            # if first stack is empty
            if not soapy_stacks[0]: 
                soapy_stacks.pop(0) # remove that stack from soapy_stacks

    # returns True if not_washed is empty, meaning every plate is washed
    return not_washed == []

# binary search for the longest possible prefix
left, right = 0, n+1 # left is 0 and right is length of stack+1 for each end of the list
# while our left is less than our right-1
while left < right - 1:
    mid = (left + right) // 2 # we find out middle value is left+right floor divided by 2 to test out

    # if our function returns true with its order and the middle as its end_index testing plates 0 to mid
    if prefix_washable(order, mid):
        left = mid # then our left pointer becomes out mid because everything before mid can be washed 
    else: # if our function returns false, for 0-mid, then those values cannot be washed, so we change our right end to mid 
        right = mid

print(str(left) + '\n')
# loop goes until left and right are 1 value apart
# then left is the answer because right is the smallest number where not all dishes are washed and left represents when all dishes 0-left value are washed
with open('dishes.out', 'w') as fout:
    fout.write(str(left) + '\n')