'''
Given a string s, return the lexicographically smallest subsequence of s that contains all the distinct characters of s exactly once.

 

Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"
 

Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters.
 

Note: This question is the same as 316: https://leetcode.com/problems/remove-duplicate-letters/

'''

class Solution:     
    def smallestSubsequence(self, s: str) -> str:
        alphabets,n=[[False,-1] for _ in range(26)],len(s)
        for i in range(n):
            value=ord(s[i])-97
            alphabets[value][1]=i 
        stack=[]
        for i in range(n):
            curr=ord(s[i])-97 
            if alphabets[curr][0]:
                continue 
            while stack and stack[-1]>s[i] and alphabets[ord(stack[-1])-97][1]>i:
                  alphabets[ord(stack[-1])-97][0]=False
                  stack.pop()
            alphabets[ord(s[i])-97][0]=True      
            stack.append(s[i])
        return "".join(stack)
Solution().removeDuplicateLetters("bcabc")
class TestApp:
      def testing_case_one(self):
          assert  Solution().removeDuplicateLetters("bcabc")=="abc"
      def testing_case_two(self):
          assert Solution().removeDuplicateLetters("cbacdcbc")=="acdb"
                 
        

        
        