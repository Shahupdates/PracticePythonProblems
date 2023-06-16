"""
Serialize and Deserialize a Binary Tree

Write a program that takes the root of a binary tree as input and performs the following operations:
- Serialize the binary tree into a string representation.
- Deserialize the string representation back into a binary tree.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    def preorder(node):
        if not node:
            values.append("None")
        else:
            values.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

    values = []
    preorder(root)
    return " ".join(values)

def deserialize(data):
    def build_tree():
        val = next(values)

        if val == "None":
            return None

        node = TreeNode(int(val))
        node.left = build_tree()
        node.right = build_tree()
        return node

    values = iter(data.split())
    return build_tree()

# Create a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

# Serialize the binary tree
serialized = serialize(root)
print("Serialized Tree:", serialized)

# Deserialize the string representation
deserialized = deserialize(serialized)
print("Deserialized Tree (In-order traversal):", serialize(deserialized))
