
# Time complexity : O(N2) , Space : O(1) 
class Solution:
      def maximumRainTrapped(self,buildings:list[int])->int:
          sum_value,n=0,len(buildings)
        #   max_LEFT_stack,max_right_stack=[],buildings[1::]
          for i in range(1,n-1):
              left_max=max(buildings[:i])
              right_max=max(buildings[i+1::])
             
              temp=min(left_max,right_max)-buildings[i]
              sum_value+=temp if temp>0 else 0
          return sum_value 
      
#Time Complexity O(N), Space Complexity : O(2N)

# Optimized Approach
class Solution:
      def maximumRainTrapped(self,buildings:list[int])->int:
          prefix_max=[0]*len(buildings)
          suffix_max=[0]*len(buildings)
          n=len(buildings)
          prefix_max[0]=buildings[0]
          for i in range(1,n):
              prefix_max[i]=max(prefix_max[i-1],buildings[i])
          suffix_max[-1]=buildings[-1]
          for i in range(n-2,-1,-1):
              suffix_max[i]=max(suffix_max[i+1],buildings[i])
          sum_value=0
          for i in range(1,n-1):
              left_max=prefix_max[i-1]
              right_max=suffix_max[i+1]
              if buildings[i]<left_max and buildings[i]<right_max:
                  temp=min(left_max,right_max)-buildings[i]
                  sum_value+=temp if temp>0 else 0
          return sum_value
#Time Complexity O(N), Space Complexity : O(N)
class Solution:
      def maximumRainTrapped(self,buildings:list[int])->int:
          n=len(buildings)
          suffix_sum=[0]*n 
          suffix_sum[-1]=buildings[-1]
          for i in range(n-2,-1,-1):
              suffix_sum[i]=max(suffix_sum[i+1],buildings[i])
          prefix_sum=buildings[0]
          sum_value=0 
          for i in range(1,n-1):
              temp=min(prefix_sum,suffix_sum[i+1])-buildings[i] 
              sum_value+=temp if temp>0 else 0 
              prefix_sum=max(buildings[i],prefix_sum)
          return sum_value 
                       
#Time Complexity O(N), Space Complexity : O(1)
class Solution:
      def maximumRainTrapped(self,buildings:list[int])->int:
          left_max=right_max=total=left=0
          right=len(buildings)-1
          while left<=right:
                
                if buildings[left]<=buildings[right]:
                   # increment left ptr
                   if left_max>=buildings[left]:
                      total+=left_max-buildings[left]
                   left_max=max(left_max,buildings[left])
                   left+=1
                else:
                    if right_max>=buildings[right]:
                        total+=right_max-buildings[right]
                    right_max=max(right_max,buildings[right])
                    right-=1
          return total
                   

class TestApp:
      def testing_case_one(self):
          assert Solution().maximumRainTrapped([0,1,0,2,1,0,1,3,2,1,2,1])==6
      def testing_case_two(self):
          assert Solution().maximumRainTrapped([4,2,0,3,2,5])==9