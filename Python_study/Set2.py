#--------------------union set  and (|)----------------------
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
s3 =set1.union(set2)
print("union: ",set3)
print("union: ",s)
print("union: ",set1.union(set2))

#-----------------------update-------------------------------
set4 = {"a", "b", "c"}
set5 = {1, 2, 3}
set4.update(set5)
print("update: ",set4)

#---------------------intersection and (&)--------------------
set7 = {1, 2, 3}
set8 = {2, 3}
set9 = set7.intersection(set8)
print("intersection: ",set9)

s1 = {"apple", "banana", "cherry"}
s2 = {"google", "microsoft", "apple"}

s3 = s1 & (s2)
print("intersection: ",s3)

#--------------------intersection_update-----------------------
se1 = {"apple", "banana", "cherry"}
se2 = {"google", "microsoft", "apple"}

se1.intersection_update(se2)

print("intersection_update: ",se1)


#------------------------difference and (-)------------------

st1 = {"apple", "banana", "cherry"}
st2 = {"google", "microsoft", "apple"}

st3 = st1.difference(st2)
st4 =st1 - st2
print("difference: ",st3)
print("difference ",st4)

#difference_update(),("update can change in given first or second set ")
set11 = {"apple", "banana", "cherry"}
set12 = {"google", "microsoft", "apple"}

set11.difference_update(set12)

print("difference_update: ",set11)

#--------------symmetric_difference and (^)----------------------

set13 = {"apple", "banana", "cherry"}
set14 = {"google", "microsoft", "apple"}

set15 = set13.symmetric_difference(set14)
set16 = set13 ^ set14
print("symmetric_difference: ",set15)
print("symmetric_difference: ",set16)

#-------------symmetric_difference_update()----------------------

set17 = {"apple", "banana", "cherry"}
set18 = {"google", "microsoft", "apple"}

set17.symmetric_difference_update(set18)

print("symmetric_difference_update: ",set17)

#-----------frozen set(you cannot add and remove in it)------------
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))


#-----------------frozen set support opertaion--------------
#---------copy.()------------

y = frozenset({"apple", "banana", "cherry"})
z = y.copy()
print(z)

#-------------we can do following syntsx difference(-) , in(&) , sym(^) , uni(|)

a = frozenset({1, 2, 3, 4})
b = frozenset({3, 4, 5})
print("difference: ",a.difference(b))
print("difference: ",a - b)#{1,2}

#------------isdisjoint(two sets with different number)---------
m = frozenset({1, 2})
n = frozenset({3, 4})
o = frozenset({2, 3})
print("isdisjoint: ",m.isdisjoint(n))#true
print("isdisjoint: ",m.isdisjoint(o))#false

#----------issubset()-------------

r = frozenset({1, 2, 6, 5})
s = frozenset({1, 2, 3})
print("issubset: ",r.issubset(s))
print("issubset: ",r <= s)
print("issubset: ",r < s)

#----------issuperset()-----------

j = frozenset({1, 2, 3})
k = frozenset({1, 2})
print("issuperset: ",j.issuperset(k))
print("issuperset: ",j >= k)
print("issuperset: ",j > k)
