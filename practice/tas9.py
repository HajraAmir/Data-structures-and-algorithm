def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Example usage:
my_list = [12, 11, 13, 5, 6]
insertion_sort(my_list)
print("Sorted array:", my_list)
def bubble_sort(arr, n):
    # Base case: If there is only one element or the array is empty, it's already sorted
    if n == 1:
        return
    
    # Traverse through all array elements
    for i in range(n - 1):
        # If the current element is greater than the next element, swap them
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    
    # After one pass of bubble sort, the largest element is moved to the end
    # Recursively call bubble_sort on the reduced array (excluding the last element)
    bubble_sort(arr, n - 1)

# Example usage:
my_list = [64, 34, 25, 12, 22, 11, 90]
n = len(my_list)
bubble_sort(my_list, n)
print("Sorted array:", my_list)
def insertion_sort_recursive(arr, n):
    # Base case: If array has only one element, it's already sorted
    if n <= 1:
        return
    
    # Sort first n-1 elements
    insertion_sort_recursive(arr, n - 1)
    
    # Insert last element into sorted part
    key = arr[n - 1]
    j = n - 2
    
    # Move elements of arr[0..n-2], that are greater than key, to one position ahead of their current position
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1
    
    arr[j + 1] = key

# Example usage:
my_list = [12, 11, 13, 5, 6]
insertion_sort_recursive(my_list, len(my_list))
print("Sorted array:", my_list)
def bubble_sort(arr):
    n = len(arr)
    # Traverse through all elements in the list
    for i in range(n):
        # Last i elements are already in place, so no need to check them
        for j in range(0, n - i - 1):
            # Traverse the list from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Example usage:
my_list = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(my_list)
print("Sorted array:", my_list)
def selection_sort(arr):
    n = len(arr)
    # Traverse through all elements in the list
    for i in range(n):
        # Find the minimum element in the unsorted part
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Example usage:
my_list = [64, 34, 25, 12, 22, 11, 90]
selection_sort(my_list)
print("Sorted array:", my_list)
def selection_sort_recursive(arr, n):
    # Base case: If there's only one element left or the array is empty, it's already sorted
    if n <= 1:
        return

    # Find the minimum element in the unsorted part
    min_index = 0
    for i in range(1, n):
        if arr[i] < arr[min_index]:
            min_index = i

    # Swap the minimum element with the first element
    arr[0], arr[min_index] = arr[min_index], arr[0]

    # Recursively call selection_sort_recursive on the remaining part of the array
    selection_sort_recursive(arr[1:], n - 1)

# Example usage:
my_list = [64, 34, 25, 12, 22, 11, 90]
selection_sort_recursive(my_list, len(my_list))
print("Sorted array:", my_list)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Split the list into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort each half
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    left_index, right_index = 0, 0

    # Compare elements from left and right sublists and merge them into a single sorted list
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Append remaining elements from left or right sublist
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged

# Example usage:
my_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = merge_sort(my_list)
print("Sorted array:", sorted_list)
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursive calls to divide the array into halves
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the sorted halves
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


# Example usage:
arr = [12, 11, 13, 5, 6, 7]
merge_sort(arr)
print("Sorted array:", arr)