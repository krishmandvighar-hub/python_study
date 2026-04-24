import numpy as np

arr = np.array([[[1,2],[3,4]],[[5,6],[7,8]],[[9,10],[11,12]]])

print("Original",arr)
print("dimension",arr.ndim)
print("indexing",arr[1,1,0])
print("slicing",arr[2,0:1])
print("filter",arr[arr>4])
print("search",np.where(arr==4))
print("sorting",arr)
for x in np.nditer(arr):
    print(x)

arr1=[[1,2],[3,4]]
arr2=[4,5,6,7]
print("joining",(arr1,arr2))

print("split",np.array_split(arr1,2))
print("split",np.array_split(arr1,2,axis=1))
print("shape",arr.shape)
print("reshape",arr.reshape(-1))



    
    








