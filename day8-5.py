try:
    num = int(input("Enter a number: "))
    assert num % 2 == 0
except:
    print("Not an even number!")
else:
    reciprocal = 1/num
    print(reciprocal)

"""
output
Enter a number: 1
Not an even number!
Enter a number: 8
0.125
"""
