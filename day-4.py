l=list(range(10))
print(l)
l.insert(5,100)
print(l)
l.remove(8)
print(l)
maximum=max(l)
print("maximum num is ",maximum)
minimum=min(l)
print("minimum num is ",minimum)
#output
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#[0, 1, 2, 3, 4, 100, 5, 6, 7, 8, 9]
#[0, 1, 2, 3, 4, 100, 5, 6, 7, 9]
#maximum num is  100
#minimum num is  0

t=(1,2,3,4,5)
t1=reversed(t)
print("reversed tuple is ",tuple(t1))
#ouput
#reversed tuple is  (5, 4, 3, 2, 1)

T=('hi','hello',1,500,254,'welcome')
L=list(T)
print(L)
#output
#['hi', 'hello', 1, 500, 254, 'welcome']
