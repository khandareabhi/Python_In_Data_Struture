class node:

    def __init__(self,data,prev=None,next=None):
        self.data=data
        self.prev=prev
        self.next=next


class Doubly_list:

    def __init__(self):
        self.head=None

    def insert_begin(self,data):
        new_node=node(data)

        if self.head is None:
            self.head=new_node
            return

        new_node.next=self.head
        self.head.prev=new_node
        self.head=new_node
    
    def display(self):
        temp=self.head

        while temp:
            print(temp.data,end="<->")
            temp=temp.next
        print("None")



node1=node(10)
node2=node(20)
node3=node(30)
node4=node(40)

node1.next=node2
node2.prev=node1
node2.next=node3
node3.prev=node2
node3.next=node4
node4.prev=node3

dll = Doubly_list()
dll.head = node1

dll.insert_begin(50)

dll.display()


