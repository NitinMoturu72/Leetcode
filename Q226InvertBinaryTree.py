# 226. Invert Binary Tree

# Easy

# Given the root of a binary tree, invert the tree, and return its root.

 

# Example 1:


# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]
# Example 2:


# Input: root = [2,1,3]
# Output: [2,3,1]
# Example 3:

# Input: root = []
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

# Recursive Solution DFS
# Base case: If the root is None, return None.
# use tmp variable to store the left child of the root.
# Set the left child of the root to be the right child of the root.
# Set the right child of the root to be the tmp variable.
# Recursively call the invertTree function on the left and right children of the root.
# Return the root of the inverted tree.
# Time complexity: O(n), where n is the number of nodes in the tree. We visit each node once.
# Space complexity: O(h), where h is the height of the tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        stack = [root]
        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return root
    
# Iterative Solution DFS
# We use a stack to perform a depth-first traversal of the tree. 
# For each node, we swap its left and right children, and then add its children to the stack if they exist.
# Time complexity: O(n), where n is the number of nodes in the tree. We visit each node once.
# Space complexity: O(h), where h is the height of the tree. In the worst case, the stack can contain all the nodes in a single path from the root to a leaf.