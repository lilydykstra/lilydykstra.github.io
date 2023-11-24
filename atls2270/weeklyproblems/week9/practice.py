from collections import deque

x = 3
y = 2

q = deque() # verison of the list quicker to work
print(q)

q.append((x, y))
print(q)

x,y = q.pop()
print(q)