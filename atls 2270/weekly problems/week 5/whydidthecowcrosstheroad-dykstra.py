## starter input output code

with open('cowqueue.in') as fin:
  n = fin.readline() # n is number of cows
  cows = [] # creates an empty list of cows
  for line in fin.readlines(): # for each line of times
    # maps the time they arrive to the time they wait and append the times to the list of cows and splits it to different values in the list
    cows.append(list(map(int, line.split()))) 

cows.sort() # sort the times 
# print(n)
# print(cows)

cur_time = 0

for n in cows: # for each number of cows
    if n[0] > cur_time: # if the time it arrived is greater than the current time 
        cur_time = n[0]+n[1] # the current time is now equal to the time it arrived + the time it took for questions
    else: # if the time the next cow arrived is less than the current time
        cur_time = cur_time + n[1] # the current time is equal to the current time + the time the next cow took for questioning


#cur_time should be the final output the problem expects
# print(cur_time)
print(cur_time, file=open('cowqueue.out', 'w'))