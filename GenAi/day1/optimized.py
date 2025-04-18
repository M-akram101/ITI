def optimized_quick_sort(arr, low=None, high=None):
    """
    Optimized QuickSort implementation that handles all test cases.

    Args:
        arr: Input array to be sorted
        low: Starting index of the partition
        high: Ending index of the partition

    Returns:
        Sorted array
    """
    # Initialize low and high for the first call
    if low is None:
        low = 0
    if high is None:
        high = len(arr) - 1

    def partition(low, high):
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quick_sort_internal(low, high):
        while low < high:
            pivot_index = partition(low, high)

            # Optimize tail recursion by handling smaller partition first
            if pivot_index - low < high - pivot_index:
                quick_sort_internal(low, pivot_index - 1)
                low = pivot_index + 1
            else:
                quick_sort_internal(pivot_index + 1, high)
                high = pivot_index - 1

    # Handle empty or single-element arrays
    if len(arr) <= 1:
        return arr

    if low < high:
        quick_sort_internal(low, high)
    return arr


# Optional: Add example usage if running directly
if __name__ == "__main__":
    test_array = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", test_array)
    print("Sorted array:", optimized_quick_sort(test_array.copy()))
