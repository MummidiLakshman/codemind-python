n=input()
n=n.split()
s=[]
for i in n:
    s.append(i)
s.sort()
print(*s)