#zerodivision error
try:
    a=10
    b=0
    c=a/b
    print(c)
except Exception:
    print("zero division error")
else:
    print("no error")

#IO error
try:
    a=open('abc.txt')
except Exception:
    print("no file")
else:
    print("file found")

#index error or runtime error
a=[1,2,3,4,5]
print(a[10])
"""
Traceback (most recent call last):
  File "K:/python inter/day8-1.py", line 22, in <module>
    print(a[10])
IndexError: list index out of range"""

#overflow error
import math
ans=math.exp(1000)
print(ans)
"""
Traceback (most recent call last):
  File "K:/python inter/day8-1.py", line 25, in <module>
    ans=math.exp(1000)
OverflowError: math range error"""

#name error
a=0
b=5
c=a/b
print(d)
"""Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print(d)
NameError: name 'd' is not defined"""

#syntax error
k=10
   print(k)
#SyntaxError: unexpected indent

#value error
a=int(input("enter value"))
enter value2.5
"""Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    a=int(input("enter value"))
ValueError: invalid literal for int() with base 10: '2.5'"""

#import error
import module_does_not_exist 

""""Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    import module_does_not_exist
ModuleNotFoundError: No module named 'module_does_not_exist'"""

#attribute error
class Attributes(object): 
	pass

object = Attributes() 
print (object.attribute) 
"""
Traceback (most recent call last):
  File "K:/python inter/day8.py", line 5, in <module>
    print (object.attribute)
AttributeError: 'Attributes' object has no attribute 'attribute'"""

#type error
arr = ('tuple', ) + 'string'
"""Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    arr = ('tuple', ) + 'string'
TypeError: can only concatenate tuple (not "str") to tuple"""

#index error
try: 
	a = [1, 2, 3] 
	print (a[3]) 
except LookupError: 
	print ("Index out of bound error.") 
else: 
	print ("Success") 

#Index out of bound error.

#key error
array = { 'a':1, 'b':2 } 
print (array['c']) 
"""Traceback (most recent call last):
  File "exceptions_KeyError.py", line 13, in 
    print array['c']
KeyError: 'c'"""

#os error
def func(): 
	print (ans) 

func() 
"""Traceback (most recent call last):
  File "442eccd7535a2704adbe372cb731fc0f.py", line 4, in 
    print i, os.ttyname(i)
OSError: [Errno 25] Inappropriate ioctl for device"""

#MemoryError
def fact(a): 
	factors = [] 
	for i in range(1, a+1): 
		if a%i == 0: 
			factors.append(i) 
	return factors 

num = 600851475143
print (fact(num)) 
"""
Traceback (most recent call last):
  File "4af5c316c749aff128df20714536b8f3.py", line 9, in 
    print fact(num)
  File "4af5c316c749aff128df20714536b8f3.py", line 3, in fact
    for i in range(1, a+1):
MemoryError"""

#ReferenceError
import gc 
import weakref 

class Foo(object): 

	def __init__(self, name): 
		self.name = name 
	
	def __del__(self): 
		print ('(Deleting %s)' % self) 

obj = Foo('obj') 
p = weakref.proxy(obj) 

print ('BEFORE:', p.name) 
obj = None
print ('AFTER:', p.name) 
"""
BEFORE: obj
(Deleting <__main__.Foo object at 0x03769F58>)
Traceback (most recent call last):
  File "K:/python inter/day8.py", line 17, in <module>
    print ('AFTER:', p.name)
ReferenceError: weakly-referenced object no longer exists"""




    
