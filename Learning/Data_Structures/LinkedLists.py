# Linked Lists
# Python doesnt have built-in Linked List so you create them like this:

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    # Insert
    def insert(self, val):
        if not self.head:       # If the List is empty
            self.head = ListNode(val)   # Make the current head the first value
            return
        curr = self.head
        while curr.next:        # While there is a value on Next
            curr = curr.next    # Move to the next
        curr.next = ListNode(val)   # Make the pointer to the next the value

    # Delete
    def delete(self, val):
        curr = self.head
        if curr and curr.val == val:    # If there is something AND the current value is the one we are looking for
            self.head = curr.next       # Make the head the following node the head
            return
        prev = None
        while curr and curr.val != val:
            prev = curr
            curr = curr.next
        if curr:
            prev.next = curr.next

    # Read
    def read(self):
        curr = self.head
        while curr:
            print(curr.val)
            curr = curr.next

ll = LinkedList()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.delete(2)
ll.read()


