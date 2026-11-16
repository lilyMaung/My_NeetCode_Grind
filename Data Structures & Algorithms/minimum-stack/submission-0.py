class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack=[]
        self.size = 0
        

    def push(self, val: int) -> None:
        #everytime we push it to the stack we have to keep track of our minStack
        #if the stack is empty then the first one to push onto will be the min 
        if not self.minStack:
            curMin = val
        else:
            curMin = min(val, self.minStack[-1])

        self.minStack.append(curMin)
        self.stack.append(val)
        

    def pop(self) -> None:
        #if the stack is not empty then we pop it off
        self.stack.pop()
        self.minStack.pop()
    
    def top(self) -> int:
        #getting the top of the stack
        return self.stack[-1]
        
        
        
        

    def getMin(self) -> int:
        return self.minStack[-1]
        

        
