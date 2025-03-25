def treeMax(root):
    if root is None:
        return float("-inf")
    else:
        leftNode = treeMax(root.left)
        rightNode = treeMax(root.right)
        return max(root.val, leftNode, rightNode)