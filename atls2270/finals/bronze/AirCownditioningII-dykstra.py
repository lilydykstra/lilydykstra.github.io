# read num. cows and ACs
n, m = (int(x) for x in input().split())

# read info about cows (Si Ti Ci)
cowInfo = []
for _ in range(n):
  cowInfo.append([int(x) for x in input().split()])

# read info about ACs (Ai Bi Pi Mi)
acs = []
for _ in range(m):
  acs.append([int(x) for x in input().split()])

"""
Enumerating all possible configurations:
  each bit corresponds to an AC
  0 means that it's not used
  1 means that it's used.

config #0: 000
config #1: 001
config #2: 010
config #3: 011
config #4: 100
config #5: 101
config #6: 110
config #7: 111

ACs are powers of 2:
  ac #0 is 2^0 = 001
  ac #1 is 2^1 = 010
  ac #2 is 2^2 = 100

so:

is ac #0 used in configuration #6 (110)?
  (001) & (110) = 000 => no, ac #1 is not used (because it's 0)

is as #1 used in config #6 (110)?
  (010) & (110) = 010 => ac #2 is used! (because it's not 0)


And now, the algorithm:

initially, min cost = infinity
for every possible combination of ACs:
  (a) calculate total cost of configuration
  (b) calculate temp. decrease in each stall
  (c) figure out if cows' reqs are met
  (d) if so,
    - if cost is less than min cost, new cost is min cost
print min cost

"""
minCostSoFar = sum([ac[3] for ac in acs]) # min cost so far is cost to operate all ACs (worst possible case)
for used in range(2**m): # used goes from 0 to 2^m-1 (gives us all configurations of ACs)
  # the first loop does (a) and (b)
  cool = [0] * 101  # 101 stall positions to keep track of how much each stall is cooled
  cost = 0
  for ac in range(m): # i goes from 0 to m-1
    if used & (2 ** ac): # is this AC used in this configuration?
      cost += acs[ac][3] # add this AC's cost to total cost (a)
      for s in range(acs[ac][0], acs[ac][1] + 1):
        cool[s] += acs[ac][2] # stall s is cooled by AC (b)

  # figure out if configuration is valid (i.e., each cow's temperature requirements are met)
  valid = True
  for cow in range(n):
    # simplifying the variables for later 

    coolingNeeds = cowInfo[cow][2]
    startStall = cowInfo[cow][0]
    endStall = cowInfo[cow][1]
    stalls = range(startStall, endStall + 1)
    cowIsHappy = all([cool[s] >= coolingNeeds for s in stalls]) # happy is only happy if all of its stalls are cooled sufficiently
    if not cowIsHappy: # if cowIsHappy is not True, valid is False and we run through it again
      valid = False

  if valid: # if valid is True we get our min value
    minCostSoFar = min(minCostSoFar, cost)

print(minCostSoFar)