stack = []

# PUSH operations
stack.append(10)
stack.append(20)
stack.append(30)

print("Stack after PUSH:", stack)

# PEEK (Top element)
print("Top element (PEEK):", stack[-1])

# POP operation
removed = stack.pop()
print("Popped element:", removed)

print("Stack after POP:", stack)