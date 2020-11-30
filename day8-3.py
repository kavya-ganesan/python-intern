try:
    print(x)
except NameError:
    print("varaible x is not defined")
except:
    print("something else went wrong")
    
"""
output
varaible x is not defined
"""

#4
#when try and except scenario is not required?
"""
it is usually used everywhere in all cases
for all program there is chance of getting error
so try-except method is used in all cases
incase of small program where we known that program is correct,
where there is not possibility of exceptions then try-except
condition are not required.
"""
