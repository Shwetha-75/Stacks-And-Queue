'''
Given a positive integer n, find the smallest integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive integer exists, return -1.

Note that the returned integer should fit in 32-bit integer, if there is a valid answer but it does not fit in 32-bit integer, return -1.

 

Example 1:

Input: n = 12
Output: 21
Example 2:

Input: n = 21
Output: -1
 

Constraints:

1 <= n <= 231 - 1

'''
class Solution:
    def __init__(self):
        self.array=set()
    def nextGreaterElement(self, n: int) -> int:
        total=2**31
        if n>total:
            return -1
        number=list(str(n))
        self.helper(0,number)
        array:list[int]=list(self.array)
        array.sort()
        for num in array:
            if num>n and num<total:
                return num 
        return -1
                
    def helper(self,index,number:list[str]):
        if index==len(number):
            self.array.add(int("".join(number[::])))
            return 
        for i in range(index,len(number)):
            number[index],number[i]=number[i],number[index]
            self.helper(index+1,number)
            number[index],number[i]=number[i],number[index]
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        #   find the next lexicographically greater element 
        if n>2**31:
            return -1
        result,temp=[],n 
        while temp:
              result.append(temp%10)
              temp//=10
        result.reverse()
        res=self.helper(result)
        return -1 if res<n else res      
 
    
    def helper(self,nums:list[int])->int:
        pivot,n=-1,len(nums)
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                pivot=i
                break 
        if pivot==-1:
            nums.reverse()
        else:
        #    swap with next greater element 
            for i in range(n-1,pivot,-1):
                 if nums[i]>nums[pivot]:
                     nums[i],nums[pivot]=nums[pivot],nums[i]
                     break 
            #  reverse 
            right,left=n-1,pivot+1
            while left<right:
                  nums[left],nums[right]=nums[right],nums[left]
                  left+=1
                  right-=1
        number=pow=0
        for num in nums:
            number=number*10+num 
            pow+=1
        return number        
            
class TestApp:
      def testing_case_one(self):
          assert Solution().nextGreaterElement(12)==21
      def testing_case_two(self):
          assert Solution().nextGreaterElement(21)==-1
      def testing_case_three(self):
          assert Solution().nextGreaterElement(144)==414        