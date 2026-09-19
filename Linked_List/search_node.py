class Node:

    def __init__(self,data):
        self.data=data
        self.next=None

node1=Node(10)
node2=Node(20)
node3=Node(30)
node4=Node(40)

node1.next=node2
node2.next=node3
node3.next=node4

head=node1
current=head
search=30
found=0

while current is not None:
    print(current.data)
    if(current.data==search):
        found=1
    current=current.next


if(found==1):
    print("Element is Founded:",search)
else:
    print("Element is Not Founded")