#1-------------------merge two dictionaries--------------------------------
dic1 ={
    "a":1,
    "b":2,
    "c":3
}
dic2 ={
    "e":1,
    "b":2,
    "c":3,
    "f":3
}

dic3 ={} 
for x in dic1:
    if x in dic2:
        dic3[x] = dic1[x] + dic2[x]
    else:
        dic3[x] = dic1[x]

for x in dic2:
    if x not in dic1:
        dic3[x] = dic2[x]
    

print(dic3)
#---------------------------


##dic3= {"a":1, "b": 4,"c":6,"e":1, "f": 2}

'''
for x,y in dic1.items():
    for r,s in dic2.items():
        if x == r:
            y+=s
            dic3[x]=y
            #dic3[r]=s
        else:
            #dic3[x]=y
            dic3[r]=s
'''
#2---------maximum value---------------------------

dis ={
    "a":7,
    "b":9,
    "c":9,
    "d":2
}

maxV=0
list1 =[]

for x in dis.values():
    if x>maxV:   
        maxV=x

for x,y in dis.items():
    if y == maxV: 
        list1.append(x)
        
print(list1)

#3-------------remove duplicates--------
data ={
    "a":1,
    "b":2,
    "c":1,
    "d":4,
}

uniq = {}
datalist = []

for x,y in data.items():
    if y not in datalist:
        uniq[x] = y
        datalist.append(y)
print(uniq)

#4----------common-------------
li1= [23,443,34,20]
l2= [23,43,34,26]

l3= list(set(li1) & set(l2))

print(l3)


#5-----------------

daata = ["raj","car","apple","python","sql","cherry"]

group={} 


for w in daata:
    length = len(w) 
    if length not in group:
        group[length] = []
        group[length].append(w)
    else:
        group[length].append(w)

print(group)
    



    
    





