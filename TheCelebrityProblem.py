'''
A celebrity is a person who is known to all but does not know anyone at a party. 
A party is being organized by some people. A square matrix mat[][] (n*n) is used 
to represent people at the party such that if an element of row i and column j 
is set to 1 it means ith person knows jth person. You need to return the index 
of the celebrity in the party, if the celebrity does not exist, return -1.

Note: Follow 0-based indexing.

Examples:

Input: mat[][] = [[1, 1, 0], [0, 1, 0], [0, 1, 1]]
Output: 1
Explanation: 0th and 2nd person both know 1st person. Therefore, 1 is the celebrity person. 
Input: mat[][] = [[1, 1], [1, 1]]
Output: -1
Explanation: Since both the people at the party know each other. Hence none of them is a celebrity person.
Input: mat[][] = [[1]]
Output: 0
Constraints:
1 <= mat.size()<= 1000
0 <= mat[i][j]<= 1
mat[i][i] == 1

'''

# Brute Force Approach 
class Solution:
        def celebrity(self, mat):
            n=len(mat)
            followers=[0]*n 
            following=[0]*n 
            for i in range(n):
                for j in range(n):
                    if mat[i][j]==1:
                        following[i]+=1
                    if mat[j][i]==1:
                        
                        followers[i]+=1
            for i in range(n):
                if following[i]==1 and followers[i]==n:
                    return i 
            return -1

class Solution:
        def celebrity(self, mat):
            
            n=len(mat)
            if n==1:
                return 0 if mat[0][0] else -1
            for i in range(n):
                count_followers=count_following=0
                for j in range(n):
                    if mat[i][j]==1:
                        count_following+=1
                    if mat[j][i]==1:
                        count_followers+=1
                if not count_following and count_followers==n:
                    return i 
            return -1 
        
class Solution:
      def celebrity(self, mat):
          n=len(mat)
          top,bottom=0,n-1
          if n==1:
                return 0 if mat[0][0] else -1
          while top<bottom:
                if mat[top][bottom]==1:
                    top+=1
                elif mat[bottom][top]==1:
                    bottom-=1
                else:
                    top+=1
                    bottom-=1
          if top>bottom:
              return -1 
          countCol=0
          for i in range(n):
              if i!=top and mat[top][i]==0:
                  countCol+=1
          countRow=0
          for i in range(n):
              if i!=top and mat[i][top]==1:
                 countRow+=1
          return top if countCol==countRow==n-1 else -1
          
          
class TestApp:
      def testing_case_one(self):
          assert Solution().celebrity([[1, 1, 0], [0, 1, 0], [0, 1, 1]])==1
      def testing_case_two(self):
          assert Solution().celebrity([[1,1],[1,1]])==-1
        