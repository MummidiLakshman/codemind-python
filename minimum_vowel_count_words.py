n=input().lower()
n=n.split()
v='aeiou'
s=[]
c=0
for i in n:
    for j in i:
        if j in v:
            c+=1
    s.append(c)
    c=0
#print(s)
m=min(s)
print(s.count(m))