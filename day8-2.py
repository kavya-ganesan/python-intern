try:
    
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

except ZeroDivisionError:
    print("cannot divide by zero ,try again")
except AttributeError:
    print("the given attribute not found")
except NameError:
    print("invalid input")
except TypeError:
    print("enter correct input type")
except Exception:
    print("wrong operator")

"""
output
Calculator
1.Add
2.Substract
3.Multiply
4.Divide
Enter Choice(1-4): 4
Enter A:5
Enter B:0
cannot divide by zero ,try again

Calculator
1.Add
2.Substract
3.Multiply
4.Divide
Enter Choice(1-4): 1
Enter A:2
Enter B:5.5
wrong operator
""""
