'''
Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] 
is nums[0]), 
return the next greater number for every element in nums.

The next greater number of a number x is the first greater number to its 
traversing-order next in the array, which means you could search circularly to find its 

next greater number. If it doesn't exist, return -1 for this number.

 

Example 1:

Input: nums = [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number. 
The second 1's next greater number needs to search circularly, which is also 2.
Example 2:

Input: nums = [1,2,3,4,3]
Output: [2,3,4,-1,4]
 

Constraints:

1 <= nums.length <= 104
-109 <= nums[i] <= 109

'''
class Solution:
      def nextGreaterElements(self, nums: list[int]) -> list[int]:
          result=[]
          n=len(nums)
          nums+=nums
          for i in range(n):
              flag=True
              for j in range(i+1,len(nums)):
                  if nums[j]>nums[i]:
                      result.append(nums[j])
                      flag=False 
                      break 
              if flag:
                  result.append(-1)
          return result
class Solution:
      def nextGreaterElements(self, nums: list[int]) -> list[int]:
          stack,n,result=nums[::-1],len(nums),[]
          for i in range(n-1,-1,-1):
              while stack and stack[-1]<=nums[i]:
                    stack.pop()
              if stack:
                  result.append(stack[-1])
              else:
                  result.append(-1)
              stack.append(nums[i])
          return result[::-1]
              
class TestApp:
      def testing_case_case(self):
          assert Solution().nextGreaterElements([1,2,1])==[2,-1,2]
      def testing_case_two(self):
          assert Solution().nextGreaterElements([1,2,3,4,3])==[2,3,4,-1,4]
      def testing_case_three(self):
          assert Solution().nextGreaterElements([1,5,3,6,8])==[5,6,6,8,-1]
      def testing_case_four(self):
          assert Solution().nextGreaterElements([5,4,3,2,1])==[-1,5,5,5,5]
        
      