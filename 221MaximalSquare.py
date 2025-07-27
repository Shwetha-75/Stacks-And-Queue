class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        # prefix sum 
        row,col=len(matrix),len(matrix[0])
        max_area=0
        for i in range(row):
            for j in range(col):
                if matrix[i][j]=='0':
                    matrix[i][j]=0
                    continue
                if i>0:
                    matrix[i][j]=int(matrix[i-1][j])+int(matrix[i][j])
                else:
                    matrix[i][j]=1 
                    max_area=1
 
        for mat in matrix:
            max_area=max(max_area,self.findLargestSquare(mat))
        return max_area
                    
    def findLargestSquare(self,heights:list[int]):
        max_area,stack=0,[] 
        n=len(heights)
        for i in range(n):
            while stack and stack[-1]!=heights[i]:
                  width=len(stack)
                  height=stack.pop()
                  if height==width:
                      max_area=max(max_area,height*width)
            stack.append(heights[i])
        while stack:
             width=len(stack)
             height=stack.pop()
             if width==height:
                 max_area=max(max_area,width*height)
        return max_area
class TestApp:
      def testing_case_one(self):
          assert Solution().maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])==4
      def testing_case_two(self):
          assert Solution().maximalSquare([["0","1"],["1","0"]])==1
      def testing_case_three(self):
          assert Solution().maximalSquare([["0"]])==0
      def testing_case_four(self):
          assert Solution().maximalSquare([["1","1"]])==1
      def testing_case_five(self):
          assert Solution().maximalSquare([["1"]])==1
      def testing_case_six(self):
          assert Solution().maximalSquare([["1","0"]])==1
      def testing_case_seven(self):
          assert Solution().maximalSquare([["1","1","1","1","1"],["1","1","1","1","1"],["0","0","0","0","0"],["1","1","1","1","1"],["1","1","1","1","1"]])==4