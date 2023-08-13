'''LIST'''
#LIST define using[]
a=[1,2,3,4,5]
print(a)

#LIST define built-in 'list'
c=list(range(6))
print(c)

#List define empty
b=[]
print(b)

#LIST accessing through the index
print(a[0])

#LIST act as a SLICING OPERATOR
print(a[0:3:2])

#LIST can be Reversing
print(a[::-1]) 

#LIST accepts the duplicate values
d=[7,5,4,5,6,2,1]
print(d)

#LIST is a Heterogeneous data
e=[1.5,5,3,4,8.9]
print(e)

#LIST can Modify
f=[5,6,7,8,9,10]
f[2]=45  #mutable
print(f)
print(len(f))

'''ITERATING OVER LIST'''

#adding number to the list
g=[1,2,3]
g.append(10)
print(g)

#adding the entire list as single element
h=[5,6,7,8]
i=[1,0,3,4]
h.append(i)
print(h) 
 
print(h[4]) #the append of i list consider a set of 1 set
#print(h[4.1]) #Type error

#insert through index
i.insert(3,17)
print(i)

#copying 
j=[3,4,5,6,8,6,2,1,9]
k=j.copy()
print(k)

#delete the index of 4th
j.pop(4)
print(j)

#It remove 6 in the list, if 2 times appeared only first element of 6 is removed
j.remove(6)
print(j)

#by defaultly taking the last element to remove
j.pop() 
print(j)

#Sorting in the Ascending order
j.sort()
print(j)

#it reverse the entire list
j.reverse()
print(j)

#extending to the single set
m=[4,5,6,7,65]
l=[1,2,9]
l.extend(m)
print(l)

#LIST COMPREHENSION
p=[1,2,3,4,5,6,7]
q=[x for x in p if x %2==0]  
print("list comprehension",b)

#By orderly Taken the even and odd numbers
numbers=[0,1,2,3,4,5,6,7]
r=[]
s=[]
for n in numbers:
    if n % 2==0:
        print("even number")
        r.append(n)
        print(r)
    else:
        print("odd number")
        s.append(n)
        print(s)

#By orderly taking the set as multiplication of 2
a=[8,43,32,45,6,2,4,6,6,9,1]
b=[]

for x in a:
    if x % 2==0:
        b.append(x)
    print(b)