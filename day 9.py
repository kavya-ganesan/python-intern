#1
n=lambda x,y:x*y
print(n(8,2))
#output 16

#2
from functools import reduce
 
fib_series = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]],
                                range(n-2), [0, 1])
 
print("Fibonacci series upto 2:")
print(fib_series(2))
print("\nFibonacci series upto 5:")
print(fib_series(5))
print("\nFibonacci series upto 6:")
print(fib_series(6))
print("\nFibonacci series upto 9:")
print(fib_series(9))
"""
output
Fibonacci series upto 2:
[0, 1]
Fibonacci series upto 5:
[0, 1, 1, 2, 3]
Fibonacci series upto 6:
[0, 1, 1, 2, 3, 5]
Fibonacci series upto 9:
[0, 1, 1, 2, 3, 5, 8, 13, 21]"""

#3
nums = [2, 4, 6, 9 , 11]
n = int(input("enter number"))
print("Original list: ", nums)
print("Given number: ", n)
filtered_numbers=list(map(lambda number:number*n,nums))
print("Result:")
print(' '.join(map(str,filtered_numbers)))
"""
ouput
enter number5
Original list:  [2, 4, 6, 9, 11]
Given number:  5
Result:
10 20 30 45 55"""

#4
list1 = [45, 55, 60, 27, 100, 108, 220]
result = list(filter(lambda x: (x % 9 == 0), list1))
print("Numbers divisible by 9 are",result)
"""
ouput
Numbers divisible by 9 are [45, 27, 108]
"""

#5
list2=[1,2,3,7,66,54,78,32,99,87,100,250,400,5]
print("original list is",list2)
even_count=len(list(filter(lambda x:(x%2==0),list2)))
print("number of even numbers in given list is",even_count)
"""
output
original list is [1, 2, 3, 7, 66, 54, 78, 32, 99, 87, 100, 250, 400, 5]
number of even numbers in given list is 8
"""

