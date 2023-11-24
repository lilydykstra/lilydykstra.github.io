# what we wil be moduloing by
MOD = 10 ** 9 + 7

# doing the math for a^b^c mod 10^9+7
def math(a,b,c):
    # using pow to go quicker
	ans = pow(a,pow(b,c),MOD)
	return ans

# reading in the number of calculations we will 
n = int(input())

for _ in range(n):
    # reads in our a,b,c
    a, b, c = map(int, input().split())
    # ans is the solution from function calculations
    ans = math(a,b,c) 
    print(ans)