class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


node1=Node(10)
node2=Node(20)
node3=Node(30)

node1.next=node2
node1.next.next=node3

print(node1.data)
print(node1.next.data)
print(node1.next.next.data)
