n=input()
n=n.lower()
s=[]
c=0
for i in n:
    if n.count(i)==1:
        s.append(i)
        c+=1
if(c==0):
    print('-1')
else:
    print(s[0])