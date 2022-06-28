n=input()
d=len(str(n))
s=''
c=0
for i in n:
    if i not in s:
        s+=i
        c+=1
if(c==d):
    print('Unique Number')
else:
    print('Not Unique Number')
