a=input()
v='aeiouAEIOU'
b=''
c=0
for i in a:
    if i not in b:
        b+=i
for i in b:
    if i in v:
        c=1
        print(i,end=' ')
if(c==0):
    print('-1')