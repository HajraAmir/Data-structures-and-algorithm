class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy = ListNode()  # Create a dummy node to start the result linked list
    current = dummy  # Initialize a current pointer to traverse the result linked list
    carry = 0  # Initialize carry to store the carryover from addition

    # Traverse both lists simultaneously until at least one of them reaches the end
    while l1 or l2:
        # Get the values from the current nodes of both lists or set to 0 if already at the end
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        # Calculate the sum including the carry from the previous operation
        total = val1 + val2 + carry

        # Update carry for the next calculation
        carry = total // 10

        # Create a new node with the digit value
        current.next = ListNode(total % 10)

        # Move to the next node in the result linked list
        current = current.next

        # Move to the next nodes in both input linked lists if they are not already at the end
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    # If there's still a carry after the last addition, create a new node with the carry value
    if carry > 0:
        current.next = ListNode(carry)

    # Return the next node after the dummy node, which contains the result linked list
    return dummy.next

def printList(node):
    while node:
        print(node.val, end=" ")
        node = node.next

# Example usage:
# Create two linked lists representing numbers 342 and 465 (reverse order)
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

print("Number 1:")
printList(l1)

print("\nNumber 2:")
printList(l2)

# Add the two numbers represented by the linked lists
result = addTwoNumbers(l1, l2)

print("\nResult after adding:")
printList(result)
