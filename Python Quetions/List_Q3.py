#
sales=[200,450,300,150,500,700,100]
sum=0
for x in range(len(sales)):
    sum+=sales[x]
print("sum of sales: ",sum)

#
maxVal = max(sales)
##for n in sales:
##    
##    if n>maxVal: 
##        maxVal = n
##    
print("maximum value: ",maxVal)

#
minVal = min(sales)
##for n in sales:
##    
##    if n<minVal: 
##        minVal = n
    
print("minimum value: ",minVal)

#
good_sale=[]
count=0
for x in sales:
    if x >300:
        count+=1
        good_sale.append(x)
print("count: ",count)        
print("good sale: ",good_sale)

#
marks=[45,78,90,56,89,67]
highest = 0
for n in marks:
    
    if n>highest: 
        highest= n
        
print("highest marks: ",highest)

#
sum1=0
for x in range(len(marks)):
    sum1+=marks[x]
ave=sum1/6
print("average marks: ",ave)

#
scores=[23,55,67,12,89,34]
for x in scores:
    if x <50:
        scores.remove(x)
        
print("good scores: ",scores)
#
sales=[200,450,300,150,500,700,100]
sales.reverse()
print(sales)

reverse1=[]
for x in range(len(sales)-1,-1):

    print(reverse1)
print(sales[::])







