#Write a Python function to rotate a given list to the right by k steps.
#Input: nums = [1, 2, 3, 4, 5], k = 2
#Output: [4, 5, 1, 2, 3]

def rotate_list_items(nums,k):
    # # Handle cases where k is larger than the list length
    k = k% len(nums)
      # Slice the list into two parts and combine them
    rotated_list = nums[-k:] + nums[:-k]

    return  rotated_list





nums = [1, 2, 3, 4, 5]
k =6
result = rotate_list_items(nums, k)
print("Rotated list:", result)