m=input()
m=m.lower()
n=input()
n=n.lower()
c=0
for i in m:
    if i not in n:
        c+=1
for i in n:
    if i not in m:
        c+=1
if(c==0):
    print('True')
else:
    print('False')