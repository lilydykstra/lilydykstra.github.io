
# usaco setup
file = open("blocks.in", "r")

s = int(file.readline()) # will read the 3 at the top of the input
cards = [] # making the empty array
for i in range(s): # repeats reading below for the 3 cards
    card = file.readline().split() # reading the cards from usaco
    cards.append(card) # adding each individual card arrays to array 

def newCounts(): # creates a function of a 26 character long array
  return [0]*26 # returns the array of 0s to assign values to later

def countLetters(word): # creates a function for counting the letters in each word
  counts = newCounts() # sets the count equal to the newCounts function
  for letter in word: # for each letter in the input word
    idx = ord(letter) - 97 #is assigning the value of the ord code of the letter minus 97 to the idx variable so that the letter is assigned to an index in the array
    counts[idx] = counts[idx] + 1 # is making the value at the index of idx's value equal to the current value plus 1
  return counts # returns the counts with the new values in it


def max(letterCounts1, letterCounts2): # inputing the values of the amount of letters in each of the sides of the card
  counts = newCounts() # sets the count equal to the newCounts function
  for letter in 'abcdefghijklmnopqrstuvwxyz': # for each letter in the alphabet
    idx = ord(letter) - 97 # is assigning the value of the ord code of the letter minus 97 to the idx variable so that the letter is assigned to an index in the array
    if letterCounts1[idx] > letterCounts2[idx]: # if the value for the amount of letters in the first word at the index of the idx value is greater than the same of the second word
        # the value is the number of that certain letter in that word
      counts[idx] = letterCounts1[idx] # then the value at that index is now assigned the value of lettercounts1
    else: # if the value is not greater at the index of idx for the word word
      counts[idx] = letterCounts2[idx] # then the value at that index is assigned the value of lettercounts2 
  return counts # returns the counts with the new values in it
 # are we returning counts because it is set equal to newCounts in the function so when it is run this value will be assigned to newCounts too?

ans = newCounts() #the answer is the values stored in newCounts

for card in cards: #for each card array in the cards array
  letterCounts = max(countLetters(card[0]), countLetters(card[1])) # it is equal to the larger value of either the first or second item and its number of a letter in the array
  for letter in 'abcdefghijklmnopqrstuvwxyz': # for each letter in the alphabet
    idx = ord(letter) - 97 # idx is equal to the ord code of the letter minus 97
    ans[idx] = ans[idx] + letterCounts[idx] #the answer at the certain index is equal to the answer at the index plus the amount of letters at the index

for count in ans: # for each item in count array in  ans
  print(count) # print the count, so that they are on different lines?

# file writing for USACO
out = open("blocks.out", "w")
for count in ans: # for each letter in the alphabet
  out.write(str(count) + '\n') # giving each value in the count array and printing on a new line
out.close()

