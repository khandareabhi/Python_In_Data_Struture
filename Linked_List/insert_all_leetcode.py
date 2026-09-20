class MyLinkedList(object):

    def __init__(self):
        self.head= ListNode(0)
        self.size=0

        

    def get(self, index):

        if(index>=self.size):
            return -1
        curr=self.head.next # use  the dami node

        for _ in range(index):
            curr=curr.next
        
        return curr.val
        """
        :type index: int
        :rtype: int
        """
        

    def addAtHead(self, val):
        node= ListNode(val)
        node.next=self.head.next
        self.head.next=node
        self.size+=1
        """
        :type val: int
        :rtype: None
        """
        

    def addAtTail(self, val):
        node=ListNode(val)
        curr=self.head

        while(curr.next):
            curr=curr.next
        
        curr.next=node
        self.size+=1


        """
        :type val: int
        :rtype: None
        """
        

    def addAtIndex(self, index,val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if(index>self.size):
            return 
        
        node=ListNode(val)
        curr=self.head

        for _ in range(index):
            curr=curr.next
        
        node.next=curr.next
        curr.next=node
        self.size+=1


        

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """

        if(index>=self.size):
            return 
        
        curr=self.head

        for _ in range(index):
            curr=curr.next

        curr.next=curr.next.next
        self.size-=1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)