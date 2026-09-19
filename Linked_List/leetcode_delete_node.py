class Node:

    def  __init__(self,data):
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
#delete logic is here 
def deletenode(node):
    node.data=node.next.data # node node 2 add the valude 40
    node.next=node.next.next  #skip the one node


deletenode(node2)

current=head

while current is not None:
    print(current.data)
    current=current.next


