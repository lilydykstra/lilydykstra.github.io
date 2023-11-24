file = open("promote.in", "r")

bronze_in, bronze_out = map(int, file.readline().split())
silver_in, silver_out = map(int, file.readline().split())
gold_in, gold_out = map(int, file.readline().split())
platinum_in, platinum_out = map(int, file.readline().split())

val1 = (silver_out+gold_out+platinum_out)- (silver_in+gold_in+platinum_in)

val2 = (gold_out+platinum_out)- (gold_in+platinum_in)

val3 = (platinum_out-platinum_in)

myanswer = str(val1) + '\n' + str(val2) + '\n' + str(val3)

out = open("promote.out","w")
out.write(myanswer)
out.close()
