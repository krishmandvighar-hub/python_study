#******* Pattern making
row = int(input("enter the any num: "))
for x in range(row,0,-1):
    for y in range(x):
        print("* ",end="")
    print()

    
row = int(input("enter the any num: "))
for x in range(0,row+1,1):
    for y in range(x):
        print("* ",end="")
    print()

    
#prime number
    
a =int(input("enter the any num : "))
isprime = True

if a<=1:
    isprime = False
for x in range(2,a):
    if a%x==0:
        isprime = False
        break
    
if isprime == True:
    print("prime number")
else:
    print("is not prime number")
#list convert
    
a=list(("a","b","c","c","l","h","h"))
print("list: ",a)
























    
    
