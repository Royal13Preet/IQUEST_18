#factorial
f=int(input("enter a number:"))
factorial=1
if n<0:
    print("factorial do not exists for negative number")
elif n==0:
    print("the factorial of 0 is 1")
else:
    for i in range(1,n+1):
        factorial=factorial*i
    print("the factorial of ", n, "is" , factorial)

#fibonacci series
fu = [0, 1]
n=int(input("enter a number:"))
if n<0:
    print("factorial do not exists for negative number")
elif n==0:
    print("the factorial of 0 is 1")
else:
    for i in range(2, n):
        next_number = fs[i-1] + fs[i-2]
        fs.append(next_number)
    for number in fs:
        print(number,end=' ')
print()
print('------------')

for x in range(8):
    print(x)
    if x==4:
        print("x is 4")
        continue
print("execution")


#even numbers multiplied 2 and odd numbers
numbers=[1,2,3,4,5]
for n in numbers:
    if n % 2==0:
        product=n
        print(product,"even number")
        product=product*2
    else:
        print("odd number")




