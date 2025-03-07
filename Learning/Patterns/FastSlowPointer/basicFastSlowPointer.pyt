# Basic Fast Slow Pointer
# Detect a Cycle on a Linked List
from ListNode import ListNode

def fastSlowPointer(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            print("This node is a cylce")
            return True
    print("This node is NOT a cylce")
    return False

# Example usage:
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

node1.next = node2
node2.next = node3
node3.next = node1  # Creates a cycle

print(fastSlowPointer(node1))  # Output: True