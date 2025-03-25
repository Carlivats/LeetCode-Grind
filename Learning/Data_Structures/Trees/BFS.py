from collections import deque

def bfs(root):
    if root is None:
        return []
    visited = []
    q = deque()

    q.append(root)
    currLevel = 0
    
    while q:
        visited.append([])

        for i in range(len(q)):
            node = q.popleft()
            visited[currLevel].append(node.val)

            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
        currLevel += 1
    return visited