def TreeSum(root):
    if root is None:
        return 0
    else:
        leftSum = TreeSum(root.left)
        rightSum = TreeSum(root.right)
        return root.val + leftSum + rightSum