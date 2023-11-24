# First, choose a positive integer z satisfying all of the conditions below:
	# z can be represented as z=pe, where p is a prime number and e is a positive integer;
	# z divides N;
	# z is different from all integers chosen in previous operations.
	# Then, replace N with N/z.

def answer(n):
		ans = 0
    
    # z is different from all integers chosen in previous operations
	# for p in range 2 to sqrt(n) so we have a smaller factor range to look at
		for p in range(2,int(n**0.5)): 
	    # z can be represented as z=p^e, where p is a prime number and e is a positive integer 
			e = 0 # represents the exponent of p. anything to power of zero is 1
	    
	    # z divides N / while p goes into n evenly
			while n % p == 0: 	
			#then replace n with n/p and increment e
				n /= p 
				e += 1
			i = 1
			
			# doing each exponent until e < 1
			# while e is greater or equal to i, we decrement e by 1, add 1 to answer, and 1 to i
			while e >= i:
				e -= i
				ans += 1
				i += 1

	# if n > 1, its a prime factor so it won't go through the while loops so we get our answer here
	# if its a prime solution the answer is 1 since it doesn't go through the while loops
		ans += n > 1
    
		return ans



# in order to get all out input answers
print(answer(24)) # answer should be 3
print(answer(1))  # answer should be 0
print(answer(64)) # answer should be 3
print(answer(1000000007))  # answer should be 1
print(answer(997764507000))  # answer should be 7