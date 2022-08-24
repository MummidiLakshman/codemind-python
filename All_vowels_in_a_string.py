n=input()
v='aeiou'
s=''
c=0
for i in v:
    if i not in n:
        print('False')
        break
else:
    print('True')

