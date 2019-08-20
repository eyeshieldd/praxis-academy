def bubblesort(arr):
    for passnum in range(len(arr)-1,3,-1):
        for i in range(passnum):
            if arr[i] < arr[i+1]: #membandingkan angka pertama dan kedua 
                temp = arr[i]   #karna angka pertama lebih besar maka pindah ke sebelah kanan
                arr[i] = arr[i+1] 
                arr[i+1] = temp 
    
    return arr


def selection_sort(arr):        
    for i in range(len(arr)):
        minimum = i
        
        for j in range(i + 1, len(arr)):
            # Select the smallest value
            if arr[j] < arr[minimum]:
                minimum = j

        # Place it at the front of the 
        # sorted end of the array
        arr[minimum], arr[i] = arr[i], arr[minimum]
            
    return arr

def insertion_sort(arr):
        
    for i in range(len(arr)):
        cursor = arr[i]
        pos = i
        
        while pos > 0 and arr[pos - 1] > cursor:
            # Swap the number down the list
            arr[pos] = arr[pos - 1]
            pos = pos - 1
        # Break and do the final swap
        arr[pos] = cursor

    return arr


