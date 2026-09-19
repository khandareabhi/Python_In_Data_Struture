class Node:

    def __init__(self,data):
        self.data=data
        self.next=None


node1=Node(20)
node2=Node(30)
node3=Node(40)
node4=Node(50)

node1.next=node2
node2.next=node3
node3.next=node4

head=node1

new_node=Node(10)

#new node is connect to before node

new_node.next=head
head=new_node # head assigning the do the new_node

current=head

while current is not None:
    print(current.data)
    current=current.next

