# Function to perform binary search on a sorted array
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = arr[mid]

        if mid_value == target:
            return mid
        elif mid_value < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Example usage:
unsorted_array = [64, 34, 25, 12, 22, 11, 90]
target = 22

sorted_array = sorted(unsorted_array)

# Step 2: Perform binary search on the sorted array
result = binary_search(sorted_array, target)

if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print("Element not found in the array.")
