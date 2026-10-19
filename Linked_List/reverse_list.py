
class Listnode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reversed_list(head):
    prev = None
    curr = head

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev


head = Listnode(1)
head.next = Listnode(2)
head.next.next = Listnode(3)

head = reversed_list(head)

while head:
    print(head.val, end=" -> ")
    head = head.next

print("None")
