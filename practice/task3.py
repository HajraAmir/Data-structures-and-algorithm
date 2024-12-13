class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head):
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    while prev.next and prev.next.next:
        # Nodes to be swapped
        node1 = prev.next
        node2 = prev.next.next

        # Swapping
        prev.next = node2
        node1.next = node2.next
        node2.next = node1

        # Move prev to the next pair
        prev = node1

    return dummy.next

def printList(node):
    while node:
        print(node.val, end=" ")
        node = node.next

# Example usage:
# Create a linked list
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

print("Original list:")
printList(head)

# Swap nodes in pairs
head = swapPairs(head)

print("\nList after swapping pairs:")
printList(head)
