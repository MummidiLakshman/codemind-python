a=input()
v='aeiooAEIOU'
c=0
for i in a:
    if i in v:
        c+=1
if(c==0):
    print('0')
else:
    print(c)