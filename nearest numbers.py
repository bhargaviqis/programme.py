m,s=map(int,input().split())
arr=input().split()
l=[]
for i in arr:
    l.append(int(i))
l.sort()
for i in range(0,len(l)):
    if(s==l[i]):
        if(i==0):
            print(l[i+1],l[i+2],l[i+3],sep=' ')
        if(i==len(l)-1):
            print(l[i-1],l[i-2],l[i-3],sep=' ')
        if(i>1 and i<len(l)-2):
            print(l[i-1],l[i+1],l[i-2],sep=' ')
        if(i==1):
            print(l[i-1],l[i+1],l[i+2],sep=' ')
