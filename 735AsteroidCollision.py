class Solution:
     def asteroidCollision(self, asteroids: list[int]) -> list[int]:
         stack,n=[],len(asteroids)
         for i in range(n):
             if asteroids[i]>0:
                 stack.append(asteroids[i])
             else:
                 while stack and stack[-1]>0 and stack[-1]<abs(asteroids[i]):
                         stack.pop(-1)
                 if stack and stack[-1]==abs(asteroids[i]):
                     stack.pop()
                 else:
                     if stack and stack[-1]<0:
                         stack.append(asteroids[i])
                     elif not stack:
                         stack.append(asteroids[i])
         return stack 
class TestApp:
      def testing_case_one(self):
          assert Solution().asteroidCollision([5,10,-5])==[5,10]
      def testing_case_two(self):
          assert Solution().asteroidCollision([8,-8])==[]
      def testing_case_three(self):
          assert Solution().asteroidCollision([10,2,-5])==[10]
      def testing_case_four(self):
          assert Solution().asteroidCollision([-2,-1,1,2])==[-2,-1,1,2]