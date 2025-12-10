#I have an integer array height, lenght n. (number of lines)
#There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
#Return the maximum amount of water a container can store.
# Notice that you may not slant the container.

#I want to choose 2 lines
#Height = shorter of two heights
# Width = difdistance btw. two lines



from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i,j = 0, len(height)-1
        max_area=0
      
        while i < j:
            area = min(height[i], height [j]) * (j-i)
            max_area = max(max_area, area)

            if height[i] < height[j]:
                i= i+1
            else:
                j= j-1

        return max_area

print(Solution().maxArea([1,8,6,2,5,4,8,3,4]))

      