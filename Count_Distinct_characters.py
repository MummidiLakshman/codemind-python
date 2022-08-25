n=input()
n=n.lower()
s=[]
for i in n:
    if(i==' '):
        continue
    if i not in s:
        s.append(i)
print(len(s))