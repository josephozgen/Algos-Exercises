# Reordering the array so that the elements less than the pivot appear first,
# followed by the elements equal to the pivot, followed by the elements greater
# than the pivot. This is known as Dutch national flag partitioning, because the
# Dutch national flag consists of three horizontal bands, each in a diffrent color.

def dutch_flag_partition(pivot_index, arr):
    pivot = arr[pivot_index]
    # First pass: group elements smaller than pivot
    for i in range(len(arr)):
        # look for a smaller element
        for j in range(i+1, len(arr)):
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                break
    # Second pass: group elements larger than pivot.
    for i in reversed(range(len(arr))):
        # look for a larger element. Stop when we reach an element less than
        # pivot, since first pass has moved them to the start of arr.
        if arr[j] > pivot:
            arr[i], arr[j] = arr[j], arr[i]
            break
    return arr
    
A = ["BLACK", "GRAY", "BLACK", "BLACK","WHITE","WHITE","GRAY","GRAY","WHITE"]
B = [1,3,1,1,2,2,3,3,2]
print(dutch_flag_partition(6, B))