#-------------Multiplication or any table --------------
n = int(input("Enter any number: "))

for x in range(1,11):
    print(x*n)

#-------------------------SUM-------------------

N = int(input("Enter any number: "))

sum = 0
for x in range(1,N+1):
    sum += x              
print("sum of N number:", sum)

#------------------PRINT 1 TO 20---------------

for x in range(1,21):
    print(x)
    
# ------------------------------TABLE---------------

n = int(input("enter any number: "))
for x in range(1,11):
    print(x*n)
    
#------------------- FACTORS------------------

X = int(input("Enter any number: "))
factors = 1
for x in range(1,X+1):
    factors*= x              
print("factors of N number", factors)

#------------------even num--------------------------------

k=int(input("enter the any num: "))
for x in range (1,k+1):
    if x%2==0:
        print(x)
        
#--------------------------even num-------------------
        
g=int(input("enter the sny num: "))
for x in range (1,g+1,2):
    print(x)
    
#---------------------count------------------------------
    
count = 0
for c in "Krisjhati":
    if c=='a' or c=='e' or c=='i':
        count+=1
print("vowels count:", count)

#-----------------while loop count-------------------------
t = 5
a = 1
while a<=10:
    print(a*t)
    a+=1
#-------------------------    
count=0
txt = "manish javel munoiEs"
for c in txt:
    if c=='a' or c=='e' or c=='i' or c=='o' or c=="u" or c=="A" or c=="E" or c=="O" or c=="I" or c=="U":
        count+=1
print("vowels count:", count)
#----------------------------
p =int(input("enter any num: "))
m = 1
while m<=10:
    print(m*p)
    m+=1

#--------------------------Table-----------------------
num = 8
i = 1
while i<=10:
    print(num,"X", i,"=",num*i)
    i+=1

##---------------------prime num-------------------------

n=int(input("enter the num: "))
isprime= True
if n<=1:
    isprime= False
else:
    for x in range(2,n):
        if n%x==0:
            isprime=False
            break
if isprime == True:
    print("prime number")
else:
    print("not a prime number")

#----------------------pattern--------------------------
print("patterns")

rows = int(input("enter the number: "))
for x in range(rows+1):
    for y in range(x):
        print("* ",end="")
        
    print()

rows1 = int(input("enter the number: "))
for m in range(rows1,0,-1):
    for n in range(m):
        print("* ",end="")
        
    print()


for x in range(10,0,-1):
    print(x)
       





    
