file = open("teleport.in", "r")
file = file.read()
#"a b x y"
#[a,b,x,y]
a,b,x,y = map(int, file.split())

# answer = my answer

teleport1 = abs(a-x)+abs(b-y)

teleport2 = abs(b-a)

teleport3 = abs(a-y)+abs(b-x)

myanswer = min(teleport1,teleport2,teleport3)

print(myanswer)

out = open("teleport.out","w")
out.write(str(myanswer))
out.close()
