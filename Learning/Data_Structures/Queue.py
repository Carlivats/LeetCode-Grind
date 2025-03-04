from collections import deque

queue = deque()

# Insert - Enqueue
queue.append(1)
queue.append(2)
queue.append(3)

# Delete - (Dequeue)
queue.popleft()

# Read
print(queue[0])
print(queue)