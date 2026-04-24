#-----------------python list questions---------------------
#-----------------1.find the sum of element-----------------
sum1=0
list=[1,2,3,4,5]
for x in range(len(list)):
    sum1+=list[x]
print("sum of the element: "sum1)

#-----------------2.find the max value----------------------

list1 =[875,5665,559,65965]
list1.sort()
print("max value: ",list1[-1])

#-----------------3.extract even no into list--------------

list2=[2,3,4,5,6,7,8,9,10]
newlist=[]
for x in list2:
    if x%2==0:
        newlist.append(x)
print("extract even: ",newlist)

#----------------4.count odd num in the list--------------

list3=[1,2,3,4,5,6,7,8,9]
count =len([x for x in list3 if x%2 !=0])
print("count odd num : " ,count)

#------------------5.reverse list---------------------
list4=[1,2,3,4,5]
list4.sort(reverse = True)
print("reverse list : ",list4)

#----------------6.find duplicates element------------

my_list = [1, 5, 2, 1, 3, 4, 5]
find_dupli = []
for x in range(len(my_list)):
    for y in range(x+1,len(my_list)):
        if my_list[x]==my_list[y] and my_list[x] not in find_dupli:
            find_dupli.append(my_list[x])
            break
        
print("Find Duplicates: ",find_dupli)

#---------------------------7. removes dublicates--------------

my_list1 = [1, 2, 2, 3, 4, 4, 5]
re=[]
for x in my_list1:
    if x not in re:
        re.append(x)
print("remove deplicate: ", re)

#----------------8.count frequency of the element----------

li = [1,2,3,3,4,3,4]  
freq = {}        
for x in li:
    if x in freq:
        freq[x]+=1
    else:
        freq[x]=1
print("count frequency",freq)

#-----------------9.check if it palindrome--------------

li1 = [1,2,3,1]
if li1 == li1[::-1]:
    print("this is a palindrome")
else:
     print("not palindrome")
     
#-------------------10.find common element in two list
     
list10=[1,2,4,6,10]
list11=[1,2,4,3,6,9,8,7]
common=[]
for x in list10:
    for y in list11:
        if x == y:
            common.append(x)
print("Common Elements:", common)

#-------------------11. rotate list left-------------------

myData = [2,3,6,78,56]
rtL = []
for n in range(1,len(myData)):
    rtL.append(myData[n])
rtL.append(myData[0])
print("Rotate Left: ", rtL)

#-------------------12.find the prime num-------------------

list12=[1,2,3,4,5,6,7,8,9]
prime=[]

for x in list12: 
    isprime= True
    if x<=1:        
        isprime= False
    else:
        for num in range(2,x):    
            if x%num==0:
                isprime= False
                break
        if isprime:
            prime.append(x)

print("Prime : ", prime)

#--------------------13.convert list into str-------------------

list13=['K','r','i','s']
str1= ""
for ch in list13:
    str1 += ch
print("String: ", str1)

#---------------14.find average of list-----------------------

list14=[12,23,58,66,47,88,58,94,25,55,54]
sum3=0
for x in list14 :
    sum3+=x
print(sum3)
ave1=sum3/len(list14)
print("average: ",ave1)

#------------------15. remove zero----------------

list6=[0,1,2,3,0,0,5,0,6]
zeroremove=[]
for x in list6:
    if x!=0:
        zeroremove.append(x)
print("remove zero: ",zeroremove)

#----------------16. multiply all element------------------------

mul=1
n=[1,2,3,5,4,6,8]
for x in n:
    mul*=x
print("multiply: ",mul)

#------------------17.student result------------------------

#----------------------for loop method-----------------------

mark1=[78,45,90,34,88,76,35]
sum2 =0
#1
for x in mark1:
    sum2+=x
print("sum: ",sum2)
#2
ave2=sum2/7
print("average: ",ave2)
pass1 =[]
fail  =[]
#3&4
for x in mark1:
    if x >40:
        pass1.append(x)
    else:
        fail.append(x)        
print("passed: ",pass1)     
print("failed: ",fail)
#5
mark1.sort()
print("highest: ",mark1[-1])

#-----------------18.shoping cart-----------------

#-------------for loop----------------------

price=[129,340,450,220,150]
total1=0
max1=price[0]
min1=price[0]
count=[]
#1
for x in price:
    total1+=x
print("total : " ,total1)
#2
for x in price:
    if x>max1:
        max1=x
print("expensive ",max1)
#3
for x in price:
    if x<min1:
      min1=x
print("cheapest",min1)
#4 
for x in price:
    if x >200:
        count.append(x)
print(len(count))        
