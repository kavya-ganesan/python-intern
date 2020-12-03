lst1=[19542209, 4887871, 1420491, 626299, 1805832, 39865590]
lst2=["New York", "Alabama", "Hawaii", "Vermont", "West Virginia",  "California"]
lst3 = list(zip(lst1, lst2))
print(lst3)
"""
output
[(19542209, 'New York'), (4887871, 'Alabama'), (1420491, 'Hawaii'), (626299, 'Vermont'), (1805832, 'West Virginia'), (39865590, 'California')]
""""

lst1=["Energy", "Agriculture", "Industry", "Technology", "Finance", "Forestry", "Transport"]
lst=list(zip(range(8), lst1))
print(lst)
"""
output
[(0, 'Energy'), (1, 'Agriculture'), (2, 'Industry'), (3, 'Technology'), (4, 'Finance'), (5, 'Forestry'), (6, 'Transport')]
"""

a = ["h", "b", "a", "c", "f", "d", "e", "g"]
x = sorted(a)
print(x)
"""
output
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
"""


numbers = [1, 2, 4, 5, 7, 8, 10, 11]
def filterOddNum(in_num):

    if(in_num % 2) != 0:
        return True
    else:
        return False
out_filter = filter(filterOddNum, numbers)
print("Filtered list with odd nos: ", list(out_filter))
"""
output
Filtered list with odd nos:  [1, 5, 7, 11]
"""
