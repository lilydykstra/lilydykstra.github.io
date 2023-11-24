fin = open('highcard.in')
n = int(fin.readline()) # the number of cards
elsie_has = set() # makes sure it is sorted
for i in range(n): 
    elsie_has.add(int(fin.readline())) # adding in each of the cards the elsie has

print(elsie_has)

elsie, bessie = [],[]

for i in range(1,n*2+1):
    # print(i)
    if i not in elsie_has: # if our iterator variable is not in elsie's list then we add that value to bessies value
        bessie.append(i)
    else: # if it is in elsies list then we add it to another elsie list to keep track of it
        elsie.append(i)
    # print(elsie)
    # print(bessie)

ans = 0
bessie_index, elsie_index = 0,0

while(bessie_index < n) and (elsie_index < n): # while the index we are at of bessies list and elsies list is less than n 
    # when bessie or elsies list is greater than n, we've hit the end of their cards and we have no more cards to compare
    if bessie[bessie_index] >  elsie[elsie_index]: # if the value of bessies card is greater than elsies card at the index
        ans += 1 # add one to our counter of bessie winning
        bessie_index += 1 # increment them both to the next card
        elsie_index += 1
    else:
        bessie_index += 1 # move up only bessies index to bessies current index to the next card in elsies deck

print(ans)   

with open('highcard.out', 'w') as f:
    f.write(str(ans) + '\n')