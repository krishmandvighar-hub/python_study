####----------------unordered in set---------------
setj={"banana","apple","cherry"}


####---------------NO dublicates allowed in set--------
set={"kris","delroy","kris","labda","delro","kar","ks","kar"}
print(set)

####------------unchangeable but we can add and remove------------

##-----------------ADD--------------------
set1={"banana","apple","cherry"}
set1.add("mango")
print(set1)
#--------S-------------
set1.update({"orange"})
print(set1)

#---------sigular Letter will comes------------
set1.update("pineapple")
print(set1)

##-----TWO LIST ADD ###  BY UPDATE SYNTAX------
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

##---------------REMOVE---------------
thisset1 = {"apple", "banana", "cherry"}
thisset1.remove("banana")
print(thisset1)

##-------------DISCARD (error never occur)---------------
thisset2 = {"apple", "banana", "cherry"}
thisset2.discard("banana")
print(thisset2)

##------------CLEAR AND POP----------
thisset3 = {"apple", "banana", "cherry"}
x = thisset3.pop()
print(x)
print(thisset3)

#------------clear---------------------
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

#---------how to access in set-------------
set2={"banana","apple","cherry"}
print("banana" in set2)






