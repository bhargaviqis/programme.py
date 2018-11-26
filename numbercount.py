#no of digits
import sys
f = int(input(' '))
sum = 0
d = f
while d > 0 :
    sum += 1
    d //= 10
print(sum)
