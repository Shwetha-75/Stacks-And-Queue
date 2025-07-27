class LRUCache:
        def __init__(self,capacity:int):
           self.capacity=capacity
           self.hash_map={}
          
        def get(self,key:int)->int:
            if key in self.hash_map:
               value=self.hash_map[key]
               del self.hash_map[key]
               self.hash_map[key]=value 
               return value 
            return -1

            
        def put(self,key:int,value:int)->None:
            if len(self.hash_map)>=self.capacity and key not in self.hash_map:
                temp=list(self.hash_map.items())[0]
                del self.hash_map[temp[0]]
                self.hash_map[key]=value 
            elif key in self.hash_map:
                 del self.hash_map[key]
                 self.hash_map[key]=value 
            else:
                self.hash_map[key]=value