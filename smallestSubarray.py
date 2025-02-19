# Find the Smallest Subarray with a Sum ≥ k

#Given an array of positive integers nums and an integer k, 
#find the length of the smallest contiguous 
#subarray whose sum is at least k. If no such subarray exists, return 0.


def min_subarray_len(nums, k):
    from math import inf

    left = 0
    current_sum = 0
    min_length = inf

    for right in range(len(nums)):
        current_sum += nums[right]

        while current_sum >= k:
            min_length = min(min_length, right - left + 1)
            current_sum -= nums[left]
            left += 1

    return min_length if min_length != inf else 0

# Example usage:
nums = [2, 3, 1, 2, 4, 3]
k = 7
print(min_subarray_len(nums, k))  # Output: 2
