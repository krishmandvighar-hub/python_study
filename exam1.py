#-------- Max value find-----------------------
list1 = [23,434,45,400]
list1.sort()                 
print(list1[-1])

list2 = [23,434,45,400]


maxVal = 0
for n in list2:
    
    if n>maxVal: 
        maxVal = n
        
print(maxVal)


#---------- Reverse list-----------------------

data = [1,2,3,4,5]
revList = []

for x in range(len(data)-1, -1, -1):
    revList.append(data[x])

print("rev:", revList)

data1= [1,2,3,4,5]
revList1 = [data1[x] for x in range(len(data)-1, -1, -1)]
print("rev:", revList1)





#----------even and odd-------------
 

l = [2,3,4,5,6,7,8,9] 
even=[]
odd=[]
for x in l:
    if x%2==0:
        even.append(x)
    else:
        odd.append(x)
print(even)        
print(odd)

'''
list=[1,2,3,4,5]
list2=[x for x in list]
print(list2)
'''
#----------find a in list -------------
 


name = ["raj","sagar","john","kris","krishna"] 
name2 =[x for x in name if "a" in x]
print(name2)
#----------sum of the num in the list -------------

list1 =[1,2,3,5,4]
sum = 0
for x in range(len(list1)):
    sum +=list1[x]              
print("sum of N number:", sum)

    
list1 =[5,4,3,2,1]
sum = 0
for x in range(len(list1)):
    sum -=list1[x]              
print("sum of N number:", sum)

















