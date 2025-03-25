
# Problem Statement

"""
Implement the Counting Sort algorithm. The goal is to sort an array of integers,
including negative numbers, efficiently.

The algorithm should:
- Handle negative numbers.
- Return an empty list if the input array is empty.
- Sort the integers in ascending order using a non-comparison-based approach.

Input: An array of integers (e.g., [-5, -10, 0, -3, 8, 5, -1, 10])
Output: A sorted array (e.g., [-10, -5, -3, -1, 0, 5, 8, 10])
"""


# Solution


def counting_sort(input_arr):
    if not input_arr:
        return []  # Return an empty list if input is empty

    min_val = min(input_arr)  # Find the smallest value in the array
    max_val = max(input_arr)  # Find the largest value in the array

    # Offset for negative numbers
    offset = -min_val  # Shift negative numbers to positive range

    # Create count array
    count_arr = [0] * (max_val - min_val + 1)  # Initialize count array based on range of values

    # Count occurrences
    for num in input_arr:
        count_arr[num + offset] += 1  # Shift numbers using offset to fit in count array

    # Build sorted array
    output_arr = []
    for i in range(len(count_arr)):
        output_arr.extend([i - offset] * count_arr[i])  # Shift back to original values

    return output_arr


# Example Test
print(counting_sort([-5, -10, 0, -3, 8, 5, -1, 10]))
