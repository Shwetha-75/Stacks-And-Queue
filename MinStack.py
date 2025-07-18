class MinStack:
      def __init__(self):
          self.stack=[]
      def push(self,value):
          temp=self.getMin()
          if temp==None:
              self.stack.append([value,value])
          else:
              if temp<value:
                  self.stack.append([value,temp])
              else:
                  self.stack.append([value,value])
      def top(self):
          return self.stack[-1][0]
      def pop(self):
          temp=self.stack.pop(-1)
          return temp[0]
      def getMin(self):
          return None if not self.stack else self.stack[-1][1]
class MinStack:
      def __init__(self):
          self.stack=[]
          self.min=10**9
      def push(self,value):
          if not self.stack:
              self.stack.append(value)
              self.min=value
              return 
          if value<self.min:
              newVal=2*value-self.min
              self.stack.append(newVal)
              self.min=value 
          else:
              self.stack.append(value)
      def pop(self):
        # before updating
        if self.stack[-1]<self.min:
            temp=self.min
            self.min=2*self.min-self.stack[-1]
            return temp
        return self.stack.pop()

      def top(self):
          if self.min<self.stack[-1]:
              return self.stack[-1]
          else:
              return self.min 
      def getMin(self):
          return self.min
    
              
class TestApp:
      def testing_case_one(self):
          array=[['Initialization'],['push',10],['push',9],['push',11]
                 ,['pop'],['top'],['getMin'],['push',20],['getMin']
                 ]
          stack:MinStack=None
          result=[]
          for entry in array:
              if entry[0]=='Initialization':
                  stack=MinStack()
                  result.append('null')
              elif entry[0]=='push':
                  stack.push(entry[1])
                  result.append('null')
              elif entry[0]=='pop':
                   result.append(stack.pop())
              elif entry[0]=='getMin':
                  result.append(stack.getMin())
              elif entry[0]=='top':
                  result.append(stack.top())
          assert result==['null','null','null','null',11,9,9,'null',9]
          