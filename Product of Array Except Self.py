
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix = 1 
        for i in range(len(nums)):
            res[i] = prefix 
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            res[i]*= postfix
            postfix*= nums[i]
        return res




# from functools import reduce
# from operator import mul
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         tem_arr = [nums[:i] + nums[i+1:] for i in range(len(nums))]
#         answers = [ reduce(mul, tem_arr[i]) for i in range(len(tem_arr))]
#         return answers


# input : array nums of int 
# output : array answer 
# considtion : answer[i] is product of all nums except i 
# items to track : product of rest items - sliding window i guess

# answers = [i*i for i in range(len(nums))  if i!= i ]