class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x in range(len(nums)):
            for  y in range(x+1,len(nums)):
                a = nums[x]+nums[y]
                if a == target:
                 return [x , y]
