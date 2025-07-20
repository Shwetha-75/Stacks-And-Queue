'''
Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

Return true if there is a 132 pattern in nums, otherwise, return false.

 

Example 1:

Input: nums = [1,2,3,4]
Output: false
Explanation: There is no 132 pattern in the sequence.
Example 2:

Input: nums = [3,1,4,2]
Output: true
Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
Example 3:

Input: nums = [-1,3,2,0]
Output: true
Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
 

Constraints:

n == nums.length
1 <= n <= 2 * 105
-109 <= nums[i] <= 109

'''
class Solution:
    def find132pattern(self, nums: list[int]) -> bool:
        n=len(nums)
        # find the prev_smallest 
        prev_nearest_smallest=self.findNearestSmallestElement(n,nums)
        stack=[]
        for i in range(n-1,-1,-1):
            if nums[i]<=prev_nearest_smallest[i]:
               continue
            while stack and stack[-1]<=prev_nearest_smallest[i]:
                stack.pop()
            if stack and stack[-1]<nums[i] and prev_nearest_smallest[i]<stack[-1]:
                return True 
            stack.append(nums[i]) 
                
        return False 
         
    def findNearestSmallestElement(self,n,nums:list[int]):
        result=[0]*n 
        result[0]=nums[0]
        for i in range(1,n):
            result[i]=min(result[i-1],nums[i])
        return result
# Solution().find132pattern([-1,3,2,0])
class TestApp:
      def testing_case_one(self):
          assert Solution().find132pattern([1,2,3,4])==False 
      def testing_case_two(self):
          assert Solution().find132pattern([3,1,4,2])==True 
      def testing_case_three(self):
          assert Solution().find132pattern([-1,3,2,0])==True
      def testing_case_four(self):
          assert Solution().find132pattern([1,0,1,-4,-3])==False
      def testing_case_five(self):
          assert Solution().find132pattern([-2,1,2,-2,1,2])==True
       
        