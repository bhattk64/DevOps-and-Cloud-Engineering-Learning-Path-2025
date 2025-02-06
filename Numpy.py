import numpy as np
arr=np.array([1,2,3,4,5])
Arr=np.array(['apple','cat'])
print(arr)
print(type(arr))
#for checking numpy version
print(np.__version__)
#checking the data type
print(arr.dtype)
print(Arr.dtype)
#diff between copy and view=copy is a new array and view is just a view of the original array
x=arr.copy()
arr[0]=43
print(arr)
print(x)
x=arr.view()
print(arr)
print(x)
x=arr.copy()
y=arr.view()
print(x.base)
print(y.base)
#array iterating
for x in arr:
    print(x)
#join in python
print(''.join(['a','b','c']))
#split in python
print('abc'.split('b'))
#reshape in python
print(np.arange(0,10).reshape(2,5))
print(np.arange(0,10).reshape(5,2))


