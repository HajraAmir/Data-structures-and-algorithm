def merge(gArray, low, mid1, mid2, high, destArray):
    i = low
    j = mid1
    k = mid2
    l = low
 
    # Choose smaller of the smallest in the three ranges
    while ((i < mid1) and (j < mid2) and (k < high)):
        if(gArray[i] < gArray[j]):
            if(gArray[i] < gArray[k]):
                destArray[l] = gArray[i]
                l += 1
                i += 1
            else:
                destArray[l] = gArray[k]
                l += 1
                k += 1
        else:
            if(gArray[j] < gArray[k]):
                destArray[l] = gArray[j]
                l += 1
                j += 1
            else:
                destArray[l] = gArray[k]
                l += 1
                k += 1
 
    # Case where first and second ranges have remaining values
    while ((i < mid1) and (j < mid2)):
        if(gArray[i] < gArray[j]):
            destArray[l] = gArray[i]
            l += 1
            i += 1
        else:
            destArray[l] = gArray[j]
            l += 1
            j += 1
 
    # Case where second and third ranges have remaining values
    while ((j < mid2) and (k < high)):
        if(gArray[j] < gArray[k]):
            destArray[l] = gArray[j]
            l += 1
            j += 1
        else:
            destArray[l] = gArray[k]
            l += 1
            k += 1
 
    # Case where first and third ranges have remaining values
    while ((i < mid1) and (k < high)):
        if(gArray[i] < gArray[k]):
            destArray[l] = gArray[i]
            l += 1
            i += 1
        else:
            destArray[l] = gArray[k]
            l += 1
            k += 1
 
    # Copy remaining values from the first range
    while (i < mid1):
        destArray[l] = gArray[i]
        l += 1
        i += 1
 
    # Copy remaining values from the second range
    while (j < mid2):
        destArray[l] = gArray[j]
        l += 1
        j += 1
 
    # Copy remaining values from the third range
    while (k < high):
        destArray[l] = gArray[k]
        l += 1
        k += 1
 
 
""" Performing the merge sort algorithm on the 
given array of values in the rangeof indices 
[low, high). low is minimum index, high is 
maximum index (exclusive) """
 
 
def mergeSort3WayRec(gArray, low, high, destArray):
    # If array size is 1 then do nothing
    if (high - low < 2):
        return
 
    # Splitting array into 3 parts
    mid1 = low + ((high - low) // 3)
    mid2 = low + 2 * ((high - low) // 3) + 1
 
    # Sorting 3 arrays recursively
    mergeSort3WayRec(destArray, low, mid1, gArray)
    mergeSort3WayRec(destArray, mid1, mid2, gArray)
    mergeSort3WayRec(destArray, mid2, high, gArray)
 
    # Merging the sorted arrays
    merge(destArray, low, mid1, mid2, high, gArray)
 
 
def mergeSort3Way(gArray, n):
    # if array size is zero return null
    if (n == 0):
        return
 
    # creating duplicate of given array
    fArray = []
 
    # copying elements of given array into
    # duplicate array
    fArray = gArray.copy()
 
    # sort function
    mergeSort3WayRec(fArray, 0, n, gArray)
 
    # copy back elements of duplicate array
    # to given array
    for i in range(n):
        gArray[i] = fArray[i]
 
    # return the sorted array
    return gArray
 
 
data = [45, -2, -45, 78, 30, -42, 10, 19, 73, 93]
data = mergeSort3Way(data, 10)
print("After 3 way merge sort: ", end="")
for i in range(10):
    print(f"{data[i]} ", end="")
"""iteration merge sorted"""
def merge(left, right):
    if not len(left) or not len(right):
        return left or right
 
    result = []
    i, j = 0, 0
    while (len(result) < len(left) + len(right)):
        if left[i] < right[j]:
            result.append(left[i])
            i+= 1
        else:
            result.append(right[j])
            j+= 1
        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            break
 
    return result
 
def mergesort(list):
    if len(list) < 2:
        return list
 
    middle = int(len(list)/2)
    left = mergesort(list[:middle])
    right = mergesort(list[middle:])
 
    return merge(left, right)
     
seq = [12, 11, 13, 5, 6, 7]
print("Given array is")
print(seq); 
print("\n")
print("Sorted array is")
print(mergesort(seq))
def merge(arr, start, mid, end):
    start2 = mid + 1
 
    # If the direct merge is already sorted
    if (arr[mid] <= arr[start2]):
        return
 
    # Two pointers to maintain start
    # of both arrays to merge
    while (start <= mid and start2 <= end):
 
        # If element 1 is in right place
        if (arr[start] <= arr[start2]):
            start += 1
        else:
            value = arr[start2]
            index = start2
 
            # Shift all the elements between element 1
            # element 2, right by 1.
            while (index != start):
                arr[index] = arr[index - 1]
                index -= 1
 
            arr[start] = value
 
            # Update all the pointers
            start += 1
            mid += 1
            start2 += 1
 
 
'''
* l is for left index and r is right index of
the sub-array of arr to be sorted
'''
 
 
def mergeSort(arr, l, r):
    if (l < r):
 
        # Same as (l + r) / 2, but avoids overflow
        # for large l and r
        m = l + (r - l) // 2
 
        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
 
        merge(arr, l, m, r)
 
 
''' UTILITY FUNCTIONS '''
''' Function to print an array '''
 
 
def printArray(A, size):
 
    for i in range(size):
        print(A[i], end=" ")
    print()
 
 
''' Driver program to test above functions '''
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    arr_size = len(arr)
 
    mergeSort(arr, 0, arr_size - 1)
    printArray(arr, arr_size)    