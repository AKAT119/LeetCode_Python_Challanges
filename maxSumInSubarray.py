
from typing import List
def maximumSubarraySum(nums:List[int], k: int ) -> int:
    seen = set()
    curr_sum, left, maxi_sum = 0, 0, 0 

    for right in range(len(nums)):
        while nums[right] in seen:
            seen.remove(nums[left])
            curr_sum -= nums[left]
            left += 1
        seen.add(nums[right])
        curr_sum += nums[right]

        if right - left + 1 == k:
            maxi_sum = max(maxi_sum, curr_sum)
            seen.remove(nums[left])
            curr_sum -= nums[left]
            left += 1

    return maxi_sum


a = [4,-1,4]
print(maximumSubarraySum(a, 2))