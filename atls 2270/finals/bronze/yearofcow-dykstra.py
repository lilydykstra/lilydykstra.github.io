from typing import NamedTuple

# instantiate the zodiacs to reference 
ZODIAC = [
	"OX",
	"TIGER",
	"RABBIT",
	"DRAGON",
	"SNAKE",
	"HORSE",
	"GOAT",
	"MONKEY",
	"ROOSTER",
	"DOG",
	"PIG",
	"RAT",
]

# assigns the aspects of the sentence the types of varibale it needs to be in order to work laterwork
class Relation(NamedTuple):
	name: str # assigns string data type to name
	dir: bool  # assigning boolean data type to dir to check direction, made later to assign PREVIOUS as true for the location in the sentence
	year: int # assigning integer data type to our year
	relative: str # assigning string data type to our relative variable 


relations = [] # empty list to append to
# reading in out sentences
# for each n
for _ in range(int(input())):
	# converts all our input to uppercase and splits the words into their own strings
	relation = input().upper().split()
	# append value of our sentence to relations list based on the values we created in our Relation class:
	# assign relation[0] to name to be a string, if relation[3] is equal to PREVIOUS its a True boolean, find the value index in ZODIAC of our zodiac year and assign that to year, and assign our comparing cow's name to relative
	relations.append(Relation(relation[0],relation[3] == "PREVIOUS", ZODIAC.index(relation[4]),relation[7],))

# instantiate bessie's birth year
birth_years = {"BESSIE": 0}

# for each item in relations
for r in relations:
	# change represents the amount the current (relative) cow's birth year needs to be adjusted to find the birth year of name cow
	# change variable is -1 if our current direction is true/previous, otherwise change=1
	change = -1 if r.dir else 1
	# this_year represents the birth year of the cow whose relation is being currently processed, found through set to the birth year of cow we are comparing to + change
	this_year = birth_years[r.relative] + change
	
	# checks if this_year matches zodiac year of our relation
	# while this_year moduloed by the length of the ZODIAC calender is not equal to our corresponding year our sentence uses
	while this_year % len(ZODIAC) != r.year:
		# if it is a different year, add change to this_year
		this_year += change
		#ends when correct year is found
	# once the correct year is found, the name and corresponding value are stored in birth_years
	birth_years[r.name] = this_year

# after we've gone through and found all cows and their year, find the difference between bessie and elsie
dist = abs(birth_years["BESSIE"] - birth_years["ELSIE"])
print(dist)