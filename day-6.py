l=[1,5,4,8,9,6]
print(l)
print("the new list is")
for i in l:
    print(i+2)
#output
#[1, 5, 4, 8, 9, 6]
#the new list is
#3
#7
#6
#10
#11
#8

i=0
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end='')
    print()
"""54321
4321
321
21
1
"""

n=int(input("no of terms"))
n1, n2 = 0, 1
count = 0
if n <=0:
    print("enter positive integer")
elif n==1:
    print("fibonacci sequence upto",n)
    print(n1)
else:
    print("fibonacci sequence")
    while count < n:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count +=1
"""no of terms5
fibonacci sequence
0
1
1
2
3"""

num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
"""Enter a number: 153
153 is an Armstrong number"""

num = 9
for i in range(1, 13):
   print(num, 'x', i, '=', num*i)
"""9 x 1 = 9
9 x 2 = 18
9 x 3 = 27
9 x 4 = 36
9 x 5 = 45
9 x 6 = 54
9 x 7 = 63
9 x 8 = 72
9 x 9 = 81
9 x 10 = 90
9 x 11 = 99
9 x 12 = 108"""

num1=int(input("enter value"))
if(num1<0):
    print("negative number")
else:
    print("positive number")
"""enter value-1
negative number
enter value5
positive number"""

days= int(input("enter days"))
years= days / 365.
print("Number of years is: ");
print(years);
"""enter days565
Number of years is: 
1.547945205479452
enter days730
Number of years is: 
2.0"""

import math
x = int(input("enter number"))
print("math.cos(",x,"): ", math.cos(x));
print("math.sin(",x,"): ", math.sin(x));
print("math.tan(",x,"): ", math.tan(x));
"""enter number8
math.cos( 8 ):  -0.14550003380861354
math.sin( 8 ):  0.9893582466233818
math.tan( 8 ):  -6.799711455220379"""

print("Calculator")
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Divide")
n=int(input("Enter Choice(1-4): "))

if n==1:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a+b
    print ("sum of numbers ")
    print("Sum = ",c)
elif n==2:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a-b
    print ("difference of numbers ")
    print("Difference = ",c)
elif  n==3:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a*b
    print ("product of numbers ")
    print("Product = ",c)
elif n==4:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a/b
    print ("quotient of numbers ")
    print("Quotient = ",c)
else:
    print("Invalid Choice")
"""Calculator
1.Add
2.Substract
3.Multiply
4.Divide
Enter Choice(1-4): 3
Enter A:5
Enter B:80
product of numbers 
Product =  400
Calculator
1.Add
2.Substract
3.Multiply
4.Divide
Enter Choice(1-4): 5
Invalid Choice"""
    
