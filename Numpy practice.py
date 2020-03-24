################################
### NUMPY (NUMERICAL PYTHON) ###
################################
#numpy is a python library used for working with arrays
#also has functions for linear algebra,fourier transform and matrices

#Array object is called ndarray
#ndarrays are faster than lists - stored at one continuos place in memory unlike lists
#one locality of reference
import numpy as np

# arr = np.array([1,2,3,4,5]) #making a numpy array
# print(arr)
# print(np.__version__) #check the version of numpy im using
# print(type(arr)) #it will show as a numpy array rather than a list
#to create an ndarray we can pass a list,tuple or any array-like object into the array() method

#### DIMENSIONS ####
#a dimension in array is one level of array depth
#can have nested arrays

#0-D arrays (scalars) are the elements in each array, i.e. each value
# arr0D = np.array(43)
# print(arr0D)
#
# #1-D arrays are those that have 0-D arrays as its elements: most common and most basic arrays
# arr1D = np.array([1,2,3,4,5])
# print(arr1D)
#
# #2-D arrays have 1-D arrays as their elements: often used to represent matrices
# #numpy has a whole sub module dedicated to matrix operations 'numpy.mat'
# arr2D = np.array([[1,2,3],[4,5,6]])
# print(arr2D)
#
# #3-D arrays have 2D arrays as their elememnts:often used to represnt 3rd order tensor
# arr3D = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
# print(arr3D)
#
# #check number of dimensions:
# print(arr0D.ndim)
# print(arr1D.ndim)
# print(arr2D.ndim)
# print(arr3D.ndim)
#
# #an array can have any  number of dimensions, you can define when making the array by using then ndmin
# arrnD = np.array([1,2,3,4],ndmin=5)
# print(arrnD.ndim)
# print(arrnD.shape) #returns a tuple with each index having the number of corresponding elements

### np array indexing:
#accessing array elements
#refer to its index number

# arr=np.array([1,2,3,4,5,6,7,8])
# print(arr[1])
# arr[1]=100
# arr2=arr[1:4]
# print(arr2)
# print(arr[1]+arr[4])
#
# #accessing 2D arrays:
# arr2D = np.array([[1,2,3],[4,5,6]])
# print(arr2D[1,0])#dimension,index
# #accessing 3D arrays:
# arr3D = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
# print(arr3D[1,1,2])#dimension,dimension,index
# print(arr3D[-1,-1,-1])

###Slicing::
# #[start:end] OR [start:end:step]
# arr=np.array([1,2,3,4,5,6,7,8])
# print(arr[3::1])#from index 3 to the end step of 1
# print(arr[:4])
# print(arr[-3:-1])
# print(arr[1:6:2])
#
# #slicing 2d arrays:
# arr2D = np.array([[1,2,3],[4,5,6]])
# print(arr2D[1,0:3:2])
# print(arr2D[0:3,1:3])
# print(arr2D.dtype)

####numpy copy and view ####
#copy is a new array, view is just a view of the original
#the copy has the data of the original but changes will not affect the original
#changes to the view will change the original array

# arr=np.array([1,2,3,4,5,6,7])
# x=arr.copy()
# arr[1]=37
# print(arr)
# print(x) #no change from the original

# arr=np.array([1,2,3,4,5,6,7])
# x=arr.view()
# x[1]=37
# print(arr)
# print(x) #both depict the changes made
#
# #'base' shows whether the array owns the data
# arr=np.array([1,2,3,4,5,6,7])
# x=arr.view()
# y=arr.copy()
# print(x.base)
# print(y.base) #this has no base as the copy 'owns' the data within it

# #shape#
# arr2D = np.array([[1,2,3],[4,5,6]])
# print(arr2D.shape)#returns '(2,3)' describing that there are 2 dimensions each with 3 elements
# arr3D = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
# print(arr3D.shape)
#
# #Reshaping arrays#
# arr1D =np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# arr1Dto2D=arr1D.reshape(4,3) #i.e. reshaping the flat 1d to 2d with 4 arrays each with 3 elements
# print(arr1Dto2D)
# arr1Dto3D = arr1D.reshape(2,3,2)#to 2 arrays each with 3 arrays within them with 2 elements
# print(arr1Dto3D)
# arr1DtoUkn = arr1D.reshape(2,2,-1)#specifying 2 arrays with 2 in each, the '-1' represents an unknown so python will calculate it for us
# print(arr1DtoUkn)

# #flattening arrays:
# #converting multi dimensional arrays to 1D
# #reshape(-1)
# arr2D = np.array([[1,2,3],[4,5,6]])
# flatarr = arr2D.reshape(-1)
# print(flatarr)



########################
### ITERATING ARRAYS ###

#Can use a normal for loop
#for 1D arrays it'll go through each individual element
#for multidimensional arrays it will go just through the dimensions

# arr1D = np.array([1,2,3])
# for x in arr1D:
#     print(x)
#
# arr2D = np.array([[1,2,3],[4,5,6]])
# for x in arr2D:
#     print(x)
#
# for x in arr2D:
#     for y in x: #have to go through each element of each array
#         print(y)

#Iterating arrays using 'nditer()'
# arr3D = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
# for x in np.nditer(arr3D): #this allows you to go through each individual element of a multi-dimensional array
#     print(x)
#
# for idx, x in np.ndenumerate(arr3D):
#     print(idx,x)#provides an index for each value it iterates through

#####################
### NP ARRAY JOIN ###

#putting contents of two or more arrays into a single one
#join arrays by axes
#use the 'concatenate()' function along with the x-axis, if axis is not explicitly passed it is taken as 0

# arr1 = np.array([1,2,3])
# arr2 = np.array([4,5,6])
# joined = np.concatenate((arr1,arr2))
# print(joined)
#
# arr1 = np.array([[1,2],[3,4]])#2D
# arr2 = np.array([[5,6],[7,8]])
# joined = np.concatenate((arr1,arr2),axis=1)
# print(joined)#so this joins the first two arrays together and the second two arrays together

# #USING A STACK FUNCTION#
# #stacking is done along a new axis
# arr1 = np.array([1,2,3])
# arr2 = np.array([4,5,6])
# stacked=np.stack((arr1,arr2),axis=1)
# print(stacked) #creates a new axis
#
# #stacking along rows using 'hstack'
# arr1 = np.array([1,2,3])
# arr2 = np.array([4,5,6])
# rowstack = np.hstack((arr1,arr2))
# print(rowstack)
#
# #stacking along columns using 'vstack'
# arr1 = np.array([1,2,3])
# arr2 = np.array([4,5,6])
# colstack = np.vstack((arr1,arr2))
# print(colstack)
#
# #Stacking along height (depth) using 'dstack'
# arr1 = np.array([1,2,3])
# arr2 = np.array([4,5,6])
# heightstack = np.dstack((arr1,arr2))
# print(heightstack)

## SPLITTING NUMPY ARRAYS ##
#reverse operation of joining
#breaks one array into multiple
#'array_split()'

# arr1D = np.array([1,2,3,4,5,6])
# split = np.array_split(arr1D,4) #split it into 4 parts
# print(split)
# #the new arrays can be accessed as a normal array
# print(split[1])
#
# arr2D = np.array([[1,2,20],[3,4,21],[5,6,22],[7,8,23],[9,10,24],[11,12,25]]) #splitting 2D arrays uses the same syntax
# split2D = np.array_split(arr2D,3)
# print(split2D)# creates 3 2D arrays each with 2 arrays in them
#
# arr2D = np.array([[1,2,20],[3,4,21],[5,6,22],[7,8,23],[9,10,24],[11,12,25]])
# split2D = np.array_split(arr2D,3,axis=1) #deciding on the axis of the split, this keeps all of the first elements together
# print(split2D)


## using 'hsplit' (opposite of hstack)
# arr2D = np.array([[1,2,20],[3,4,21],[5,6,22],[7,8,23],[9,10,24],[11,12,25]])
# newarr = np.hsplit(arr2D,3)
# print(newarr)

########################
### SEARCHING ARRAYS ###

#CAN SEARCH AN ARRAY FOR A CERTAIN VALUE
#use the 'where()' method
#
# arr = np.array([1,2,3,4,5,4,4,6])
# x=np.where(arr==4)
# print(x) #shows the index of each 4 in the array
# y=np.where(arr%2 == 0)
# print(y)

#'searchsorted()' performs a binary search on an array and returns the index where the specified value would be inserted
#to maintain the search order
#
# arr = np.array([6,8,9])
# x=np.searchsorted(arr,7)
# print(x) #the number 7should be inserted at index 1, the method starts from the left and returns the first index where
# #number 7 is no longer  larger than the next value
# arr = np.array([6,8,9,8,6])
# y=np.searchsorted(arr,7,side="right") #start the search from the right
# print(y)
#
# arr = np.array([1,3,5,7])
# x=np.searchsorted(arr,[2,4,6]) #search for the positions of more than one value
# print(x)

### Sorting NUmpy arrays ###
############################
#putting elements in an ordered sequence
#numeric or alphabetical
#'sort()'

# arr = np.array([3,2,0,1])
# print(np.sort(arr))
#
# arrstr = np.array(['banana','cherry','apple'])
# print(np.sort(arrstr))
#
# arrbool = np.array([True,False,True])
# print(np.sort(arrbool))
#
# arr2D = np.array([[3,2,8],[6,9,1]])
# print(np.sort(arr2D)) #sorts each array in the dimension separately


########################
### filtering arrays ###

#getting some elements out of an existing array and making a new one
#using a boolean index list - if the value at the index is true then it is contained in the filtered array

# arr = np.array([33,76,112,168,232,85,12]) #we will filter this for all values above 100
#
# filter_arr = []
#
# for element in arr:
#     if element >100:
#         filter_arr.append(True)
#     else:
#         filter_arr.append(False)
# newarr = arr[filter_arr] #so takes all the values from arr where its index is true for the condition
# print(filter_arr)
# print(newarr)
#
# #creating a filter directly from an array:
# filter_arr = arr>100
# newarr = arr[filter_arr]
# print(filter_arr)
# print(newarr)
