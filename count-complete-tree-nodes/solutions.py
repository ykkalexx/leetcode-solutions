root = [1,2,3,4,5,6]

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def countNodes(root: TreeNode) -> int:
    if not root:
        return 0
    # use recursion to count the number of nodes in the left and right subtrees
    return 1 + countNodes(root.left) + countNodes(root.right)

print(countNodes(root))