from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
  
        for x in range(len(nums)):
            for  y in range(x+1,len(nums)):
                a = nums[x]+nums[y]
                if a == target:
                 return [x , y]

solution = Solution()
result = solution.twoSum([2, 7, 11, 15], 9)
print(result)