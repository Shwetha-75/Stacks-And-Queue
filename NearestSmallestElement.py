'''
Given an array arr[] of integers, for each element in the array, find the nearest smaller element on its left. If there is no such smaller element, return -1 for that position.

Input: arr[] = [1, 6, 2]
Output: [-1, 1, 1]
Explaination: 
There is no number to the left of 1, so we return -1. 
After that, the number is 6, and the nearest smaller number on its left is 1. 
Next, the number is 2, and the nearest smaller number on the left is also 1.
Input: arr[] = [1, 5, 0, 3, 4, 5]
Output: [-1, 1, -1, 0, 3, 4]
Explaination: 
There is no number to the left of 1,  so we return -1. 
After that, the number is 5,  and the nearest smaller number on its left is 1. 
 Next, the number is 0, and there is no smaller number on the left, so we return -1.
Then comes 3, and the nearest smaller number on its left is 0.
After that, the number is 4, and the nearest smaller number on the left is 3. 
Finally, the number is 5, and the nearest smaller number on its left is 4.
Constraints:
1 ≤ arr.size()≤ 106
1 ≤ arr[i] ≤ 103 



'''

class Solution:
      def nearestSmallestElement(self,nums:list[int])->list[int]:
          n=len(nums)
          result=[-1]*n
          for i in range(1,n):
              for j in range(i-1,-1,-1):
                  if nums[j]<nums[i]:
                      result[i]=nums[j]
                      break 
          return result 

# Using Monotonic stack 
class Solution:
     def nearestSmallestElement(self,nums:list[int])->list[int]:
         n=len(nums)
         stack,result=[],[-1]*n
         for i in range(n):
             while stack and stack[-1]>=nums[i]:
                   stack.pop(-1)
             if stack:
                 result[i]=stack[-1]
             stack.append(nums[i])
         print(result)
         return result
Solution().nearestSmallestElement([10,10])
class TestApp:
      def testing_case_one(self):
          assert Solution().nearestSmallestElement([1, 5, 0, 3,4,5])==[-1, 1, -1, 0, 3, 4]
      def testing_case_two(self):
          assert Solution().nearestSmallestElement([1,6,2])==[-1,1,1]