class Solution:
        def sumSubarrayMins(self,nums:list[int])->int:
            n=len(nums)
            prefix_nse=[-1]*n 
            suffix_nse=[n]*n 
            stack=[]
            for i in range(n):
                while stack and stack[-1][0]<=nums[i]:
                    stack.pop()
                if stack:
                    prefix_nse[i]=stack[-1][1]
                stack.append([nums[i],i])
            stack=[]
            for i in range(n-1,-1,-1):
                while stack and stack[-1][0]<nums[i]:
                    stack.pop()
                if stack:
                   suffix_nse[i]=stack[-1][1]
                stack.append([nums[i],i])    
            total=0
            for i in range(n):
                total=(total+(i-prefix_nse[i])*(suffix_nse[i]-i)*nums[i])%(10**9+7)
             
            return total 
class TestApp:
      def testing_case_one(self):
          assert Solution().sumSubarrayMins([1,4,3,2])==33 
      def testing_case_two(self):
          assert Solution().sumSubarrayMins([3,1,2,4])==30
        
        