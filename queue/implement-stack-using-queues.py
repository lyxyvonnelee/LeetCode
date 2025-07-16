class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.que1 = deque()
        self.que2 = deque()
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.que1.append(x)
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        size = len(self.que1)
        size -= 1
        while size>0:            
            self.que2.append(self.que1.popleft())
            size -= 1
        result = self.que1.popleft()
        self.que1, self.que2 = self.que2, self.que1
        return result
        

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.que1[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.que1)==0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()