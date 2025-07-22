class Solution:
    def subArrayRanges(self, nums: list[int]) -> int:
        results,total,n=[],0,len(nums)
        for i in range(n):
            for j in range(i,n):
                results.append(nums[i:j+1])
        for result in results:
            min_value=max_value=result[0]
            for i in range(1,len(result)):
                if min_value>result[i]:
                    min_value=result[i]
                if max_value<result[i]:
                    max_value=result[i]
            total+=max_value-min_value
        return total
class  Solution:
        def subArrayRanges(self, nums: list[int]) -> int:
            max=self.sumOfSubArrayMaximum(nums)
            min=self.sumOfSubArrayMinimum(nums)
            return max-min
       
        def sumOfSubArrayMinimum(self,nums:list[int])->int:
            n=len(nums)
            prefix_nse,suffix_nse=[-1]*n,[n]*n
            stack=[]
            for i in range(n):
                while stack and stack[-1][0]>=nums[i]:
                    stack.pop()
                if stack:
                    prefix_nse[i]=stack[-1][1]
                stack.append([nums[i],i])
            stack=[]
            for i in range(n-1,-1,-1):
                while stack and stack[-1][0]>nums[i]:
                    stack.pop()
                if stack:
                    suffix_nse[i]=stack[-1][1]
                stack.append([nums[i],i])
            total=0
            for i in range(n):
                total=total+(i-prefix_nse[i])*(suffix_nse[i]-i)*nums[i]
            return total
        def sumOfSubArrayMaximum(self,nums:list[int])->int:
            n=len(nums)
            prefix_nse,suffix_nse=[-1]*n,[n]*n 
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
                total=total+(i-prefix_nse[i])*(suffix_nse[i]-i)*nums[i]
            return total
class TestApp:
      def testing_case_one(self):
          assert Solution().subArrayRanges([1,2,3])==4
      def testing_case_two(self):
          assert Solution().subArrayRanges([1,3,3])==4 
      def testing_case_three(self):
          assert Solution().subArrayRanges([4,-2,-3,4,1])==59