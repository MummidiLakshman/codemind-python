p,r,t=map(int,input().split())
res=p*(pow((1+r/100),t))
print("%.2f"%res)