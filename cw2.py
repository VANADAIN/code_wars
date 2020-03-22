arr1 = [1,2,3,4,1,2,3,5,5,6,7,8,7,8,6]

def find_unique(arr):
    for i in arr:
        s = arr.count(i)
        if s == 1: 
            print(i)

find_unique(arr1)