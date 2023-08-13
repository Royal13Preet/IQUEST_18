'''TUPLES'''

#Tuples define using()
c=(2,7,8,9,5,45,0)
print(c)

#Tuples define built-in 'tuple'
a=tuple(range(6))
print(a)

#Tuples define empty
a=()
print(a)

#Tuples accessing through the index
print(c[2])

#Tuples can be Reversing
print(c[::-1])

#Tuples act as a SLICING OPERATOR
print(c[2:8:5])

#Tuples is a Heterogeneous data
d=('abc',3,4,5,0.7,9)
print(d)

#Tuples cannot Modify
b=(5,6,7,3,2,2,5,6)
b[2]=900
print(d)

#Tuples can duplicate
e=(6,7,543,3,7,5,6)
print(e)

#TUPLE Comprehension
g=(5,7,87,5,10)
f=[x for x in g if x %2==0] 
print("tuple comprehension",f)

#Tuples can add the set
h=(7,4,5,2,4)
i=(3,56,2,5,7)
print(h+i)

#tuples can double
print(h*2)

#Tuple cannot concatenate with int. it only tuple to tuple
print(h+2)
print(h-2)

#Tuples can tell the true or false conditions
print(6 not in h)
