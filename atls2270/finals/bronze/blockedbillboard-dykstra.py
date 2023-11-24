file = open("billboard.in","r")

lm=[int(s) for s in file.readline().split()] # creates an array of the coordinates of the lawnmover sign
cf=[int(s) for s in file.readline().split()] # creates an array of the coordinates of the cow feed sign

lm_x0 = lm[0] # assigns the first value in the lawnmower array as lm_x0
lm_y0 = lm[1] # assigns the second value in the lawnmower array as lm_y0
lm_x1 = lm[2] # assigns the third value in the lawnmower array as lm_x1
lm_y1 = lm[3] # assigns the fourth value in the lawnmower array as lm_y1

cf_x0 = cf[0] # assigns the first value in the cow feed array as cf_x0
cf_y0 = cf[1] # assigns the second value in the cow feed array as cf_y0
cf_x1 = cf[2] # assigns the third value in the cow feed array as cf_x1
cf_y1 = cf[3] # assigns the fourth value in the cow feed array as cf_y1

width = lm_x1-lm_x0 # assigns the  value of right side of the lawnmower - left side to the width
length = lm_y1-lm_y0 # assigns the value of top of the lawnmower - the bottom to the length


# accounts for when the length of the lawnmower is covered by the cow feed in different scenarios
if cf_x0 <= lm_x0 and lm_x0 <= cf_x1 and cf_x0 <= lm_x1 and lm_x1 <= cf_x1:
    ''' 
    the first two sets of inequalities test whether the left side of the lawnmower is between the left and right sides
    of the cow feed sign, and the second two sets inequalities test whether the right side of the lawnmower is also 
    between the left and right sides of the lawnmower. All testing whether the lawnmower's width is encapsulated by 
    the cow feed sign in some way.
    '''
    if cf_y0 > lm_y1 or lm_y0 > cf_y1: # seeing if the lawn mower sign is completely above or below the cow feed 
        pass # if it is completely above or below, pass the condition to then do the length*width of the lawnmower sign below
    elif lm_y0 < cf_y0 and cf_y1 < lm_y1: # seeing if the cow feed is directly sandwiched in the middle of the lawnmower sign
        pass # if it in in the middle, pass so that we do the whole area of the lawnmower sign below
    elif lm_y1 > cf_y1 and cf_y1 > lm_y0: # seeing if the cow feed sign is covering the bottom of the lawnmower sign
        length = lm_y1 - cf_y1 # if the bottom is covered then the length becomes the lawnmower y1 vlaue minus the cow feed y1 value
    elif lm_y1 > cf_y0 and cf_y0 > lm_y0: # seeing if the cow feed sign is covering the top of the lawnmower sign
        length = cf_y0 - lm_y0 # if the top is covered the length becomes the cow feed y0 value minues lawnmower y0 value
    else: # if it is none of those conditions, then it probably means the cowfeed completely covers the lawnmower and we don't need a tarp
        width = 0 # we don't need a tarp so length and width are 0
        length = 0

elif cf_y0 <= lm_y0 and lm_y0 <= cf_y1 and cf_y0 <= lm_y1 and lm_y1 <= cf_y1:
    '''
    the first two sets of inequalites test whether the bottom side  of the lawnmower is between the top and bottom sides 
    of the cowfeed sign, and the second two sets of inequalities test whether the top side of the lawnmower is between the
    top and bottom sides of the cow feed sign. This all tests whether the lawn mower height is encapsulated by the cow feed
    sign in some way.
    '''
    if cf_x0 > lm_x1 or lm_x0 > cf_x1: # seeing if the lawnmover is completely to the right or left of the cow feed sign
        pass # pass since we don't need to change the length or width
    elif lm_x0 < cf_x0 and cf_x1 < lm_x1: # seeing if the lawnmower is sandwiches between the height of the lawnmower sign
        pass # passing since we will still have to cover the whole thing with the two ends poking out
    elif lm_x1 > cf_x1 and cf_x1 > lm_x0: # testing whether the cowfeed covers the left side of the lawnmower sign
        width = lm_x1 - cf_x1 # if the left is covered, the width is changed to the lawnmowers x1 value minus the cowfeed x1 value
    elif lm_x1 > cf_x0 and cf_x0 > lm_x0: # testing if the right side of the lawnmower sign is covered by the cowfeed sign
        width = cf_x0 - lm_x0 # if the right side is covered then the width becomes the cowfeed x0 minus the lawnmower x0
    else: # if it none of those coniditons the lawnmower is completely covered by the cow feed and we dont need a tarp
        width = 0 # since we don't need a tarp the length and width are 0
        length = 0

else:
    pass # for when there is only one corner covered, do the whole area of the lawnmower sign

lm_area = width*length # calculating the area needed for covering the lawnmower sign based on coniditons or changes made to length and width in the if statements


#so usaco can run it
out = open("billboard.out","w")
out.write(str(lm_area))
out.close()