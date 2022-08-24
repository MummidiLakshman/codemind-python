n=input()
n=n.lower()
v='aeiou'
s=''
c=0
for i in v:
    if i not in n:
        print(i,end=' ')
        c+=1
if(c==0):
    print('0')

