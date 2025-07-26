'''
Given string num representing a non-negative integer num, and an integer k, 
return the smallest possible integer after removing k digits from num.

 

Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
 

Constraints:

1 <= k <= num.length <= 105
num consists of only digits.
num does not have any leading zeros except for the zero itself.

'''

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
             
         