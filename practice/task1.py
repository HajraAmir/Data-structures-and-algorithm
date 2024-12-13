class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head):
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    curr = head

    while curr:
        # Check for duplicates
        while curr.next and curr.val == curr.next.val:
            curr = curr.next

        # If no duplicates, move pointers
        if prev.next == curr:
            prev = prev.next
        else:
            prev.next = curr.next

        curr = curr.next

    return dummy.next

def printList(node):
    while node:
        print(node.val, end=" ")
        node = node.next

# Example usage:
# Create a sorted linked list with duplicates
head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(3)

print("Original list:")
printList(head)

# Remove duplicates
head = deleteDuplicates(head)

print("\nList after removing duplicates:")
printList(head)





"""dummy -> 0 -> 1 -> 1 -> 2 -> 3 -> 3
         ^
         |
        head
        
Initialize prev to point to the dummy node and curr to point to the head node.

Enter the loop:

curr is pointing to node with value 1, which is equal to the next node's value.
Move curr to the next node with different value: curr points to the second node with value 1.        
  dummy -> 0 -> 1 -> 1 -> 2 -> 3 -> 3
              ^
              |
             curr
prev.next is not equal to curr, so update prev.next to point to curr.next (which is node with value 2).
  dummy -> 0 -> 1 -> 2 -> 3 -> 3
         ^
         |
        prev
Move curr to the next node (node with value 2)
  dummy -> 0 -> 1 -> 2 -> 3 -> 3
                    ^
                    |
                   curr
Repeat the above steps:

curr is pointing to node with value 3, which is equal to the next node's value.
Move curr to the next node with different value: curr points to the second node with value 3.
rust
Copy code
dummy -> 0 -> 1 -> 2 -> 3 -> 3
                              ^
                              |
                             curr
prev.next is not equal to curr, so update prev.next to point to curr.next
(which is None, as it's the end of the list).



dummy -> 0 -> 1 -> 2 -> 3
                    ^
                    |
                   prev   """                                     