## starter input output code

file_in = open('whereami.in') # opening the input file
data = file_in.read().strip().split('\n') # reads in the input, strip the spaces, splits to new lines, and makes it a list of two elements
n = int(data[0]) # take the index 0 of data (number of mailboxes) to n
mailboxes = data[1] # takes the second index of data, the string of mailbox letters

ans = 0 

# k starts at 1, i starts at 0
# k is the unique length we want

for k in range(1, n+1): # will go through and check every value between and including k
    sequence = set() # each time it runs it resets

    for i in range(n-k+1):
        # goes through the indexes of the mailboxes to check all possibilities of n length in the string
        # check from 0 -> n-k+1
        # k = 3 -> 7-3=4+1=5 so check 0,1,2,3,4

        sequence.add(mailboxes[i : i + k]) # starts adding comparisons of each k length

    if len(sequence) == (n-k+1): # if the number of windows is the same as the sequence to know everything is unique
        # n is always 7
        # k = 3 -> 7 -3 + 1 = 5

        ans = k
        # we can exit exit the loop as this will be the smallest working length
        break

print(ans, file = open('whereami.out', 'w')) # printing the answer to the out file