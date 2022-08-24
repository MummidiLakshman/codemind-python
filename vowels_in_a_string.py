n=input()
p=input()
v='aeiou'
s=''
c=0
for i in n:
    if i in p:
        s=n.index(p)
        print('True')
        print(s)
        break
else:
    print('False')

