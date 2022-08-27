n=input()
n=n.lower()
v='aeiou'
k=''
c=0
for i in n:
    if i in v:
        k+=i
for i in v:
    if i not in k:
        print(i,end=' ')
        c+=1
if(c==0):
    print('0')