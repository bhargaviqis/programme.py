x,y=map(int,input().split())
l=[]
for num in range(x,y+1):
    if num>1:
      for i in range (2,num):
        if(num % i)==0:
          break
      else:
        l.append(num)
for p in range(0,len(l)):
  if(p==len(l)-1):
    print(l[p],end=(""))
  else:
    print(l[p],end=(" "))
