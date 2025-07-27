class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        stack=[]
        n=len(nums)
        for i in range(n-k+1):
            stack.append(max(nums[i:i+k]))
        return stack 
    
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        stack,n,result=[],len(nums),[]
        for i in range(n):
            while stack and nums[stack[-1]]<=nums[i]:
                stack.pop()
            stack.append(i)
            if i+1>=k:
                result.append(nums[stack[0]])
        return result   

        
class TestApp:
      def testing_case_one(self):
          assert Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7],3)== [3,3,5,5,6,7]
      def testing_case_two(self):
          assert Solution().maxSlidingWindow([1],1)==[1]