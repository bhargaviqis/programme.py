S = int(input())
factorial = 1
if S < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif S == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,S + 1):
       factorial = factorial*i
   print("The factorial of",S,"is",factorial)
