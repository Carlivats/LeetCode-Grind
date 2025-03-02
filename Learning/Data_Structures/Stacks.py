stack = []

# Insert
stack.append(1)
stack.append(2)
stack.append(3)

# Delete
stack.pop()

# Read 
print(stack[-1])

stack.append(1)
stack.append(2)
stack.append(3)
stack.append(1)

print(stack[-1])
print(stack)