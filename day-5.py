a=int(input("enter value a"))
b=int(input("enter value b"))
def add(a,b):
    c=a+b
    print("addition of two numbers is",c)
def sub(a,b):
    d=a-b
    print("subtraction of two numbers is",d)
def div(a,b):
    e=a/b
    print("division of two numbers is ",e)
def mul(a,b):
    f=a*b
    print("multiplication of two numbers is",f)
add(a,b)
sub(a,b)
div(a,b)
mul(a,b)
#output
#enter value a100
#enter value b50
#addition of two numbers is 150
#subtraction of two numbers is 50
#division of two numbers is  2.0
#multiplication of two numbers is 5000

def covid(name,temp=98):
    print("patient name",name)
    print("body temp",temp)
covid("ria")
covid("tia")
covid("mia","100")
covid("ram")
covid("rahul","99")
#ouput
#patient name ria
#body temp 98
#patient name tia
#body temp 98
#patient name mia
#body temp 100
#patient name ram
#body temp 98
#patient name rahul
#body temp 99
    
    
    
