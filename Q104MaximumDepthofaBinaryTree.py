# 104. Maximum Depth of Binary Tree

# Easy

# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: 3
# Example 2:

# Input: root = [1,null,2]
# Output: 2
 

# Constraints:

# The number of nodes in the tree is in the range [0, 104].
# -100 <= Node.val <= 100


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [[root,1]]
        depth  = 1

        while stack:
            pair = stack.pop()
            node = pair[0]
            count = pair[1]

            if node.left:
                stack.append([node.left, count+1])
            if node.right:
                stack.append([node.right, count+1])
            if count > depth:
                depth = count
        
        return depth
    
# Iterative Solution DFS
# Base case: If the root is None, return 0.
# Initialize a stack with the root node and its depth (1).
# Initialize a variable depth to keep track of the maximum depth found so far.
# While the stack is not empty, pop a node and its depth from the stack.
# If the node has a left child, push it onto the stack with its depth incremented by 1.
# If the node has a right child, push it onto the stack with its depth incremented by 1.
# If the current depth is greater than the maximum depth found so far, update the maximum depth
# Return the maximum depth found.
# Time complexity: O(n), where n is the number of nodes in the tree. We visit each node once.
# Space complexity: O(h), where h is the height of the tree. In the worst case, the stack will contain all the nodes in a single path from the root to a leaf node.




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
# Recursive Solution DFS
# Base case: If the root is None, return 0.
# Recursively call the maxDepth function on the left and right children of the root.
# Return 1 plus the maximum of the depths of the left and right subtrees.
# Time complexity: O(n), where n is the number of nodes in the tree. We visit each node once.
# Space complexity: O(h), where h is the height of the tree. In the worst case, the recursion stack will contain all the nodes in a single path from the root to a leaf node.