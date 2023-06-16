"""
Check if a Binary Tree is Balanced

Write a program that takes the root of a binary tree as input and checks whether the binary tree is balanced. A binary tree is balanced if the heights of its left and right subtrees differ by at most 1.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_balanced(root):
    def get_height(node):
        if not node:
            return 0

        left_height = get_height(node.left)
        right_height = get_height(node.right)

        if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
            return -1

        return max(left_height, right_height) + 1

    return get_height(root) != -1

# Create a binary tree
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# Check if the binary tree is balanced
balanced = is_balanced(root)

# Print the result
print("The binary tree is balanced:", balanced)
