def calPoints(ops):
    stack = []  # Create an empty stack to store valid points
    for op in ops:  # Iterate through each operation
        if op == "+":  # If the operation is '+'
            # Add the sum of the last two valid rounds to the stack
            stack.append(stack[-1] + stack[-2])
        elif op == "D":  # If the operation is 'D'
            # Double the last valid round's points and add to the stack
            stack.append(stack[-1] * 2)
        elif op == "C":  # If the operation is 'C'
            # Remove the last valid round's points from the stack
            stack.pop()
        else:  # If the operation is an integer (representing the score of a round)
            # Convert the string to integer and add to the stack
            stack.append(int(op))
    # Sum up all the points in the stack
    return sum(stack)

# Example usage:
ops = ["5","2","C","D","+"]
print(calPoints(ops))  # Output: 30



"""Initialize an empty stack: stack = [].
Iterate through each operation in the list ops.
For each operation:
For "5", it's an integer, so convert it to an integer and add to the stack: stack = [5].
For "2", similarly add it to the stack: stack = [5, 2].
For "C", remove the last valid round's points from the stack: stack = [5].
For "D", double the last valid round's points and add to the stack: stack = [5, 10].
For "+", add the sum of the last two valid rounds to the stack: stack = [5, 10, 15].
Sum up all the points in the stack: 5 + 10 + 15 = 30.
Return the total score, which is 30.
So, the output is 30"""