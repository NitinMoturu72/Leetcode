# 100. Same Tree

# Easy

# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

# Example 1:


# Input: p = [1,2,3], q = [1,2,3]
# Output: true
# Example 2:


# Input: p = [1,2], q = [1,null,2]
# Output: false
# Example 3:


# Input: p = [1,2,1], q = [1,1,2]
# Output: false
 

# Constraints:

# The number of nodes in both trees is in the range [0, 100].
# -104 <= Node.val <= 104

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        
        stack = [[p,q]]

        while stack:
            pair = stack.pop()
            n1 = pair[0]
            n2 = pair[1]

            if not n1 and not n2:
                continue
            
            if not n1 or not n2 or n1.val != n2.val:
                return False
            
            stack.append([n1.left, n2.left])
            stack.append([n1.right, n2.right])

        return True

# Iterative Solution DFS
# Base case: If both trees are None, return True.
# Initialize a stack with the root nodes of both trees.
# While the stack is not empty, pop a pair of nodes from the stack.
# If both nodes are None, continue to the next iteration.
# If one of the nodes is None or their values are not equal, return False.
# Push the left children of both nodes onto the stack.
# Push the right children of both nodes onto the stack.
# If the loop completes without returning False, return True, indicating that the trees are the same.
# Time Complexity: O(n), where n is the number of nodes in the trees. We visit each node once.
# Space Complexity: O(h), where h is the height of the trees. In the worst case, the stack will contain all the nodes in a single path from the root to a leaf node.



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if p and q and p.val==q.val:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        
        else:
            return False
        

# Recursive Solution DFS
# Base case: If both trees are None, return True.
# If one of the trees is None or their root values are not equal, return False.
# Recursively call the isSameTree function on the left children of both trees and the right children of both trees.
# Return the logical AND of the results of the recursive calls.
# Time Complexity: O(n), where n is the number of nodes in the trees. We visit each node once.
# Space Complexity: O(h), where h is the height of the trees. In the worst case, the recursion stack will contain all the nodes in a single path from the root to a leaf node.