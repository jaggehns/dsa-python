class Node:
    def __init__(self, value=None, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev # if doubly linked list

class LinkedList:
    def __init__(self):
        self.head = None
    
    # we can add methods for insert, delete etc. here
    def insert():
     pass

    def delete():
     pass

# initialising nodes
n1 = Node(3)
n2 = Node(7)
n3 = Node(2)
n4 = Node(9)

# creating linked list and assigning head and next values
LL = LinkedList()
LL.head = n1
n1.next = n2
n2.next = n3
n3.next = n4