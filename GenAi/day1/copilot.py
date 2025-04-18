def quick_sort(arr):
    # Base case: if array has 1 or fewer elements, it's already sorted
    if len(arr) <= 1:
        return arr

    # Choose the pivot (here we're using the last element)
    pivot = arr[-1]

    # Partition elements into three groups
    left = []  # Elements smaller than pivot
    middle = []  # Elements equal to pivot
    right = []  # Elements larger than pivot

    # Partition the array
    for x in arr:
        if x < pivot:
            left.append(x)
        elif x == pivot:
            middle.append(x)
        else:
            right.append(x)

    # Recursively sort left and right partitions
    return quick_sort(left) + middle + quick_sort(right)


# Example usage
if __name__ == "__main__":
    # Test the quick sort implementation
    test_array = [64, 34, 25, 12, 22, 11, 90]
    sorted_array = quick_sort(test_array)
    print("Original array:", test_array)
    print("Sorted array:", sorted_array)

"""
# QuickSort Algorithm Explanation

## Overview
QuickSort is a highly efficient, comparison-based sorting algorithm that uses a divide-and-conquer strategy. It's known for its average-case time complexity of O(n log n).

## Key Components

### 1. Pivot Selection
- In our implementation, we use the last element as the pivot
- Other common pivot selection strategies include:
  - First element
  - Random element
  - Median of three elements

### 2. Partitioning
In our code, partitioning is done by:
```python
left = []    # Elements smaller than pivot
middle = []  # Elements equal to pivot
right = []   # Elements larger than pivot

for x in arr:
    if x < pivot:
        left.append(x)
    elif x == pivot:
        middle.append(x)
    else:
        right.append(x)
```

### 3. Recursion
The algorithm recursively sorts the sub-arrays:
```python
return quick_sort(left) + middle + quick_sort(right)
```

## How It Works

1. **Base Case**: If array has 1 or fewer elements, return it (already sorted)
2. **Pivot Selection**: Choose a pivot element
3. **Partitioning**: Divide array into three parts:
   - Elements less than pivot
   - Elements equal to pivot
   - Elements greater than pivot
4. **Recursive Sorting**: Apply QuickSort to left and right partitions
5. **Combining**: Merge the sorted partitions with pivot in the middle

## Time Complexity
- Best Case: O(n log n)
- Average Case: O(n log n)
- Worst Case: O(n²) - occurs with already sorted arrays or arrays with many duplicates

## Space Complexity
- O(log n) - for the recursive call stack
- Our implementation uses additional space for the partition arrays

## Advantages
- Efficient for large datasets
- In-place sorting possible (though our implementation creates new arrays)
- Works well with virtual memory systems

## Disadvantages
- Not stable (equal elements may change relative order)
- Worst case performance is poor
- Our implementation uses extra space for partitioning
"""
