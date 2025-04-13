from typing import List

def maxsum_subarray(nums,k):
    def shrink_window():
        nonlocal curr_sum, left
        seen.remove(nums[left])
        curr_sum -= nums[left]
        left +=1

    seen = set()
    curr_sum, left, maxi_sum = 0,0,0
    #cheking duplicate 
    for right in range(len(nums)):
        while nums[right] in seen:
            shrink_window()
            
        seen.add(nums[right])
        curr_sum +=nums[right]
        
        #evaliate the k limitation
        if right - left +1 ==k:
            maxi_sum = max(maxi_sum, curr_sum)
            shrink_window()
    return maxi_sum


a = [4,-1,4]
print(maxsum_subarray(a, 2))

