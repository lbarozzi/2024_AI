import numpy as np

def showArray(arr):
    print(arr)
    print(type(arr))
    print(f"----{arr.ndim}: {arr.dtype}-----")

arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9,])
showArray(arr1)

arr2 = np.array(42)
showArray(arr2)

arr3= np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9], [2,4,6,8,10,12,14,16,19]])
showArray(arr3)
print(arr3[0,1])

arr4 = np.array([ [ [1,2,3], [4,5,6] ],[ [1,2,3], [4,5,6] ] ])
showArray(arr4)
print(arr4[0,1,2])

arr5 = np.array([1, 2, 3, 4,5 ], ndmin=5)
showArray(arr5)

'''
# -----------------------
print(arr1[3:])
print(arr1[-3:-1])
print(arr1[::2])
#'''
# ------------------
showArray(arr3)
print(arr3[0:3,2:4])

arr6 = np.array(['cane', 'gatto', 'ippopotamo', 'stegosauro', ])
showArray(arr6)

arr7 = np.array([1, 2, 3, 4, ], dtype='S')
showArray(arr7)

arr8 = np.array(["01", 2, 3, 4, 5, ],dtype="i")

arr9 = np.array([1.2, 2.3, 3.3, 4.5])
showArray(arr9)
arr10 = arr9.astype('i')
showArray(arr10)

# ---------------
arr11 = arr10.view()
arr12 = arr10.copy()
arr11[2]=9
print("--------  - -- - -")
showArray(arr10)
showArray(arr11)
showArray(arr12)

arr13= np.array([1, 2, 3, 4, 5, 6 ,7 ,8 ,9 ,10, 11, 12, 13, 14, 15, 16 ,17, 18 ])
print(arr13.shape)
print(arr4.shape)

arr14 = arr13.reshape(3,3, -1) #3d
arr13[8]=99
print(arr13.shape)
print(arr14.shape)
showArray(arr13)
showArray(arr14)
arr15 = arr14.reshape(-1)
showArray(arr15)
# -----------------------
'''
for x in arr14:
    print("--------------")
    print(x)
    for y in x:
        for z in y:
            print(z)
    print("--------------")
#'''
for x in np.nditer(arr14[:,::2]):
    print(x)

arr20 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
arr21 = np.array([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, ])
arr22 = np.concatenate( (arr20,arr21) )
showArray(arr22)

arr23 = np.array([ [1, 2], [3, 4] ])
arr24 = np.array([ [5, 6], [7, 8] ])

arr25 = np.concatenate((arr23,arr24))
arr26 = np.concatenate((arr23,arr24),axis=1)
showArray(arr25)
showArray(arr26)

# ----
arr30 = np.array([1, 2, 3, ])
arr31 = np.array([4, 5, 6, ])

arr32= np.stack((arr30,arr31))
arr33= np.stack((arr30,arr31),axis=1)
showArray(arr32)
showArray(arr33)

arr34 = np.hstack( (arr30,arr31))
showArray(arr34)

arr35 = np.vstack( (arr30,arr31))
showArray(arr35)
# --------------
arr40 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, ])
arr41 = np.split(arr40,3)
for a in arr41:
    showArray(a)
# ----------
arr50 = np.array([2, 4, 8 ,4 ,2 ,8, 9, ])
x= np.where(arr50==4)
print(x)
x= np.where(arr50%2==0)
print(x)
x= np.where(arr50>5)
print(x)

# -----
arr60 = np.array( [  1, 2 ,3 ,4, 5, 6, 7, 8, 9 ,])
arr61 = np.array([True, False, False,False,True,True,False,True,False])
arr62 = arr60[arr61]
showArray(arr62)

arr65= np.arange(1,100,dtype="f")
print(arr65)

arr66= []
for t in arr65:
    if t%3 ==0:
        arr66.append(True)
    else:
        arr66.append(False)

# in genere si scrive così
arr67 = arr65%3==0
arr68 = arr65*10.2

showArray(arr65[arr66] )
showArray(arr65[arr67] )

showArray(arr67)
showArray(arr68)

#
print(np.zeros(5, dtype="i" ) )
print(np.ones(5, dtype="i" ) )