arr1 = [1,2,3]
arr2 = map (lambda x:x*2, arr1)
print(list(arr2))

arr1 = [1,2,3]
arr2 = []
for x in range(0, len(arr1)):
    arr2 = arr1[x] * 2
    print(arr2)