'''
Given a rows x cols binary matrix filled with 0's and 1's, 
find the largest rectangle containing only 1's and return its area.

 

Example 1:


Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.
Example 2:

Input: matrix = [["0"]]
Output: 0
Example 3:

Input: matrix = [["1"]]
Output: 1
 

Constraints:

rows == matrix.length
cols == matrix[i].length
1 <= row, cols <= 200
matrix[i][j] is '0' or '1'.

'''

class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        row,col=len(matrix),len(matrix[0])
        for i in range(row):
            for j in range(col):
                if matrix[i][j]=='0':
                   matrix[i][j]=int(matrix[i][j])
                   continue
                if i>0:
                    matrix[i][j]=int(matrix[i][j])+int(matrix[i-1][j])
                else:
                    matrix[i][j]=int(matrix[i][j])
        max_area=0
        for histogram in matrix:
            max_area=max(max_area,self.findLargestRectangleInHistogram(histogram))
        return max_area 
    def findLargestRectangleInHistogram(self,heights:list[int]):
        stack,max_area=[],0
        n=len(heights)
        for i in range(n):
            while stack and  heights[stack[-1]]>heights[i]:
                  # calculate area 
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
          assert Solution().maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])==6
      def testing_case_two(self):
          assert Solution().maximalRectangle([["0"]])==0
      def testing_case_three(self):
          assert Solution().maximalRectangle([["1"]])==1