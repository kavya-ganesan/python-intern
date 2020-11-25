def merge(dic1,dic2):
	return(dic2.update(dic1))
dic1 = {'a': "apple" ,'b': "ball"}
dic2 = {'c': "cat" ,'d' :"dog"}
print(merge(dic1,dic2))
print(dic2)
#output
#None
#{'c': 'cat', 'd': 'dog', 'a': 'apple', 'b': 'ball'}

dic3 = {"hello":25,"all":20,"good" :40,"morning" : 40}
key_to_be_removed = 'good'
res= dic3.pop(key_to_be_removed,None)
print("removed item=",res)
print("updated dictionary=",dic3)
#output
#removed item= 40
#updated dictionary= {'hello': 25, 'all': 20, 'morning': 40}


values=['orange','apple','grape','banana']
keys=['o','a','g','b']
dic4=dict(zip(keys,values))
print(dic4)
#output
#{'o': 'orange', 'a': 'apple', 'g': 'grape', 'b': 'banana'}

set1=set([1,5,2,7,17,20,30,52,41,0,25,84,12])
print(len(set1))
#output
#13

sn1 = set([1,2,3,4,5,6])
sn2 = set([2,4,6,8,10])
print("original sets")
print(sn1)
print(sn2)
print("remove intersection of 2nd set from 1st set")
print(sn1-sn2)
#output
#original sets
#{1, 2, 3, 4, 5, 6}
#{2, 4, 6, 8, 10}
#remove intersection of 2nd set from 1st set
#{1, 3, 5}
