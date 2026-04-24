#1.---------- remove duplicates in list using set.------------

list1=[23,45,67,78,45,67,23,89,9,12,56,9]
list2=set((list1))
print("remove duplicates: ",list2)

#2.---------------- find common elements from two sets.------
set1 ={1,2,3,4,5,6}
set2 ={1,2,6}
set3 =set1.intersection(set2)
print("common element: ",set3)

#3.----------- find different elements from two sets.------------

set4 ={1,2,3,4,5}
set5 ={1,2,6}
set6 =set4.symmetric_difference(set5)
print("different elements: ",set6)

#4.-------------- remove 20 and 40 element in set-------

set7 = {10,20,30,40,50,60}
set7.remove(20)
set7.remove(40)
print(set7)

#---------------for loop------------------
set8 ={10,20,30,40,50,60}
a = 20
b = 40

if a in set8 :
    set8.remove(a)
if b in set8:
    set8.remove(b)
print(set8)

#5.--------------- convert set into string.------------

set = {'k','r','i','s'}
str = ""
for x in set:
    str+=x
print("string: ",str)    

#6.--------------- join four difference sets .---------------

set11 ={"kris","ajay","delroy","royan"}
set12 ={2,4,6,8,10}
set13 ={True,False}
set14 ={"apple","banana","cherry"}
set15 =set11 | set12 | set13 | set14 
print("join four difference sets: ",set15)
