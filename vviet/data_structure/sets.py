'''SETS'''

#set define using {}
a={4,5,6,7,87}
print(a)

#set define the built-in function 'set'
b=set(range(9))
print(b)

#set is heterogeneous
e={5,6,6.7,5,'abc'}
print(e)

#set cannot accessing through the index
#print(b[2])

#Set not act as a SLICING OPERATOR
#print(b[::-1])

#Set cannot be Modify
#b[2]=900
#print(b)

#Set not act as a SLICING OPERATOR
#print(b[1:3:5])