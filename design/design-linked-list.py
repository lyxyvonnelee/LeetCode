class Node:
    
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
        
class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._head = Node(0)
        self._count = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index > self._count - 1:
            return -1
        
        prev_node = self._head
        for _ in range(index):
            prev_node = prev_node.next
            
        return prev_node.next.val
        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.addAtIndex(0,val)
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self._count,val)
        
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self._count:
            return
        
        self._count += 1
        
        prev_node = self._head
        
        #find prev node
        for i in range(index):
            prev_node = prev_node.next
          
        new_node = Node(val)
        
        new_node.next = prev_node.next
        prev_node.next = new_node
        
        return
            
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index > self._count-1:
            return
        
        self._count -= 1
        
        prev_node = self._head
        
        for _ in range(index):
            prev_node = prev_node.next
            
        del_node = prev_node.next
        prev_node.next = del_node.next
        
        return
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)