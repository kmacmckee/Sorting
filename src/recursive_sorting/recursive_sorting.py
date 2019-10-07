# TO-DO: complete the help function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    print("elements:", elements)
    merged_arr = [0] * elements
    # TO-DO
    i = 0 #merged_arr index
    a = 0 #arrA index
    b = 0 #arrB index

    for i in range(0, elements):
        if a >= len(arrA):
            #there aren't any more elements in arrA
            merged_arr[i] = arrB[b]
            b += 1
        elif b >= len(arrB):
            #there aren't any more elemnts in arrB
            merged_arr[i] = arrA[a]
            a += 1
        elif arrA[a] < arrB[b]:
            #the next value in arrA is smaller
            merged_arr[i] = arrA[a]
            a += 1
        elif arrB[b] < arrA[a]:
            #the next value in arrB is smaller
            merged_arr[i] = arrB[b]
            b += 1
        elif arrA[a] == arrB[b]:
            #the values of arrA and arrB are equal/duplicate
            #letting arrA go first because why not
            merged_arr[i] = arrA[a]
            a += 1

    return merged_arr

print(merge([2,4,6,8,10],[1,2,3,4,5]))

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
