from TreeSum import treeSum
from TreeMax import treeMax
from TreeHeight import treeHeight
from BFS import bfs

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Function to test TreeSum
def test_TreeSum():
    # Creating a test binary tree:
    #        5
    #       / \
    #      3   8
    #     / \   \
    #    1   4   10

    root = TreeNode(5)
    root.left = TreeNode(3, TreeNode(1), TreeNode(4))
    root.right = TreeNode(8, None, TreeNode(10))

    result = treeSum(root)
    print("TreeSum result:", result)

    result = treeMax(root)
    print("TreeMax result:", result)

    result = treeHeight(root)
    print("TreeHeight result:", result)

    result = bfs(root)
    print("BFS result:", result)

# Run the test
test_TreeSum()
