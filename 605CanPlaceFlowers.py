class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        if len(flowerbed)==1 and n==1:
            return flowerbed[0]==0
            
        length=len(flowerbed)
        for i in range(length-1):
            if i==0 and flowerbed[i]==0 and flowerbed[i+1]==0 and n:
                flowerbed[i]=1
                n-=1
            elif i==length-2 and flowerbed[i]==0 and flowerbed[i+1]==0 and n:
                 flowerbed[i]=1
                 n-=1
                 
            elif flowerbed[i-1]==0 and  flowerbed[i]==0 and flowerbed[i+1]==0 and n:
                flowerbed[i]=1
                n-=1
        for i in range(length-1):
            if flowerbed[i]==flowerbed[i+1]==1:
                return False
        return n==0
class TestApp:
      def testing_case_one(self):
          assert Solution().canPlaceFlowers([1,0,0,0,1],1)==True 
      def testing_case_two(self):
          assert Solution().canPlaceFlowers([1,0,0,0,1],2)==False
      def testing_case_three(self):
          assert Solution().canPlaceFlowers([0,0,1,0,1],1)==True
      def testing_case_four(self):
          assert Solution().canPlaceFlowers([0,0,1,0,0],1)==True
        