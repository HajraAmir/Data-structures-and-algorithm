class MinStack:
    def __init__(self):
        self.stack = []  # Stack to store elements
        self.min_stack = []  # Stack to store minimum values

    def push(self, val):
        self.stack.append(val)  # Add the element to the main stack

        # If the min_stack is empty or the new value is smaller than or equal to the current minimum,
        # append the new value to the min_stack.
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        # If the element to be popped is the current minimum, also pop from the min_stack.
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        return self.stack.pop()  # Pop the element from the main stack

    def top(self):
        return self.stack[-1]  # Return the top element of the main stack

    def getMin(self):
        return self.min_stack[-1]  # Return the top element of the min_stack (current minimum)

# Example usage:
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print("Minimum element:", minStack.getMin())  # Output: -3
minStack.pop()
print("Top element:", minStack.top())  # Output: 0
print("Minimum element:", minStack.getMin())  # Output: -2
