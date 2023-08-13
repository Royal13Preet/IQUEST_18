'''
start=+ve and -ve
stop=+ve generally, -ve only if start point is lesser than stop point
step=+ve when start is lesser than stop
      -ve when start is greater than stop
'''

for x in range (-6,-1):
    print(x) #output comes in one by one
    
for x in range (-6,-1):
    print(x,end=" ") #end used to the number in one order

for x in range(-10,-20,-2):
    print(x) 

for x in range (1,6,2):
    print(x,end=" ")

for x in range(5,0,-1):
    print(x)

for x in range(5,0,-1):
    print("*"*x)   #inverted half pyramid
         
for x in range(5,-1,-1):
    print("*" *x)  #inverted half pyramid
      
y=6
for x in range(y):
    for x in range(y-x): 
        print('*', end=" ")
    print(' ')    #inverted half pyramid in another way
           
for i in range(1, 7):
    for j in range(6, i-1, -1):
        print(j, end=" ")
    print()  #inverted half pyramid using number
    
for x in range(1,6):
    print("*" *x) #half pyramid

y=6
for x in range(y):
    for y in range(x):
        print('*',end=" ")
    print(' ')   #half pyramid in another way
    
for i in range(6, 0, -1):
    for j in range(6, i-1, -1):
        print(j, end=" ")
    print()   #half pyramid using numbers
    
for i in range(1, 7):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()  #half pyramid

numbers = [1, 2, 3, 5, 6]
for i in range(len(numbers)):
    for j in range(i + 1):
        print(numbers[j], end=" ")
    print()   #half pyramid using list
    
for i in range(4):
    print(" " * (4 - i - 1) + "*" * (2 * i + 1)) #full pyramid

for i in range(4, 0, -1):
    print(" " * (4 - i) + "*" * (2 * i - 1))  #inverted full pyramid
