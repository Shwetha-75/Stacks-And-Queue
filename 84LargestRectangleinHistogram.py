'''

Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

 

Example 1:


Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
Example 2:


Input: heights = [2,4]
Output: 4
 

Constraints:

1 <= heights.length <= 105
0 <= heights[i] <= 104
'''
class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        max_area,n=0,len(heights)
        for i in range(n):
            count=1
            for j in range(i-1,-1,-1):
                if heights[j]<heights[i]:
                    break 
                else:
                    count+=1
            for j in range(i+1,n):
                if heights[j]<heights[i]:
                    break 
                else:
                    count+=1
                    
            max_area=max(heights[i]*count,max_area)
        return max_area 
# Precomputing pse, nse Time Complexity : O(3N) Space Complexity : O(4N)
class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        n=len(heights)
        pse,nse=[-1]*n,[n]*n 
        stack=[]
        for i in range(n):
            while stack and stack[-1][0]>heights[i]:
                stack.pop()
            if stack:
                pse[i]=stack[-1][1]
            stack.append([heights[i],i])
        stack=[]
        for i in range(n-1,-1,-1):
            while stack and stack[-1][0]>heights[i]:
                stack.pop()
            if stack:
                nse[i]=stack[-1][1]
            stack.append([heights[i],i])
        max_area=0
        for i in range(n):
            max_area=max(max_area,heights[i]*(nse[i]-pse[i]-1))
        return max_area            
# Without computing pse & nse 
class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        max_area,n=0,len(heights)
        stack=[]
        for i in range(n):
            # calculating the max_area 
            while stack and heights[stack[-1]]>=heights[i]:
                #   calculate the area 
                  value=heights[stack.pop()]
                  pse=stack[-1] if stack else -1
                  max_area=max(max_area,value*(i-pse-1))
            stack.append(i)
        while stack:
              value=heights[stack.pop()]
              pse=stack[-1] if stack else -1
              max_area=max(max_area,value*(n-pse-1))
        return max_area 
              
                
class TestApp:
      def testing_case_one(self):
          assert Solution().largestRectangleArea([2,1,5,6,2,3])==10 
      def testing_case_two(self):
          assert Solution().largestRectangleArea([2,4])==4 
      def testing_case_three(self):
          assert Solution().largestRectangleArea([2,1,5,6,2,3])==10
      def testing_case_four(self):
          assert Solution().largestRectangleArea([2,0,2])==2
