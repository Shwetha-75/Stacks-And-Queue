import sys
class Solution:
     def removeKdigits(self, num: str, k: int) -> str:
         stack,n=[],len(num)
         for i in range(n):
             while stack and stack[-1]>num[i] and k:
                  stack.pop()
                  k-=1
             stack.append(num[i])
         while k:
             stack.pop()
             k-=1
         sys.set_int_max_str_digits(50000)
         return str(int("".join(stack))) if stack else "0"

class TestApp:
      def testing_case_one(self):
          assert Solution().removeKdigits("1432219",3)=="1219"
      def testing_case_teo(self):
          assert Solution().removeKdigits("10200",1)=="200"
      def testing_case_three(self):
          assert Solution().removeKdigits("9",1)=="0"
      def testing_case_four(self):
          assert Solution().removeKdigits("112",1)=="11"
             
         