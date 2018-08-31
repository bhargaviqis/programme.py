a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))
if (a>=b) and(a>=c):
  largest=a
  print("a")
elif (b>=a) and (b>=c):
  largest=b
  print("b")
else:
  largest=c
  print("c")
