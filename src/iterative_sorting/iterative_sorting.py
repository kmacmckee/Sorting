# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(i + 1, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j

        # Swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr

print(selection_sort([23, 43, 59, 43, 11, 39]))


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    n = len(arr)

    #loop through all elements in the array
    for i in range(n):
        #Last i elements are already in place
        for j in range(0, n - i - 1):
            #loop through the array from 0 to n - i - 1
            #Compare each element with its neighbor
            if arr[j] > arr[j + 1]:
                #Swap if true
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

print(bubble_sort([23, 43, 59, 43, 11, 39]))


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr