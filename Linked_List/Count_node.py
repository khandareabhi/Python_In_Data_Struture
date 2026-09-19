class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

node1=Node(10)
node2=Node(20)
node3=Node(30)

node1.next=node2
node1.next.next=node3
head=node1
current=head
count=0
while current is not None:
    print(current.data)
    count=count+1
    current=current.next


print("count the number in the Linked List",count)
