from collections import deque

with open("shuffle.in", "r") as input_file:
	n = int(input_file.readline()) # number of cows
  
	cows_after_shuffle = [0] * n # empty list of 0s for n cows, to keep track of cows when shuffling
	a = list(map(int, input_file.readline().split())) # shuffle order
  
# print(n)
# print(cows_after_shuffle) # for case 1 [3,2,1,3]
# print(a) # [0,0,0,0]

#running the shuffle once
for i in range(n): # going through all the cows
  a[i] -= 1 # subtract one from each cow
  # print('a' , a)
  cows_after_shuffle[a[i]] += 1 # add one to wherever value of a[i] is
  # print('shuffle ',cows_after_shuffle)

# print(a)
# print(cows_after_shuffle)

ans = n # basic answer is the number of cows we have is the number of spots filled
no_cows = deque() # keeping track of where there are no cows double ended queue

#find the number of positions that don't have cows after 1 shuffle
for i in range(n):
  if cows_after_shuffle[i] == 0: # if there are no cows there
    no_cows.append(i) # append that position to no cows
    ans -= 1 # subtract 1 from answer of all cows for each empty spot
  # print('no cows', no_cows)
  # print('ans', ans)

while no_cows: # while no_cows has a value
  curr = no_cows.popleft() # current position with no cows, our 0s, and then remove it

  cows_after_shuffle[a[curr]] -= 1 # subtract 1 from cows_after_shuffle index of a[curr] to eventually show where there will always be cows

  if cows_after_shuffle[a[curr]] == 0: # if that position is equal to zero after process above
    no_cows.append(a[curr]) # append that to no_cows
    ans-=1 # and subtract 1 from answer again to show there is another position with no cows

# print(ans)
print(ans, file=open("shuffle.out", "w"))