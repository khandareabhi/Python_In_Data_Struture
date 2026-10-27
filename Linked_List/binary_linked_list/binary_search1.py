
class node:

    def __init__(self,data,prev=None,next=None):
        self.data=data
        self.prev=None
        self.next=None



node1=node(10)
node2=node(20)
node3=node(30)
node4=node(40)
node5=node(50)

node1.next=node2
node2.prev=node1
node2.next=node3
node3.prev=node2
node3.next=node4
node4.prev=node3
node4.next=node5
node5.prev=node4

current=node1 #head node is that means first node

while current is not  None:
    print(current.data)
    current=current.next

\