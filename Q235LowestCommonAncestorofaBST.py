# 235. Lowest Common Ancestor of a Binary Search Tree

# Medium

# Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

# Example 1:


# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6.
# Example 2:


# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# Output: 2
# Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
# Example 3:

# Input: root = [2,1], p = 2, q = 1
# Output: 2
 

# Constraints:

# The number of nodes in the tree is in the range [2, 105].
# -109 <= Node.val <= 109
# All Node.val are unique.
# p != q
# p and q will exist in the BST.



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or not p or not q:
            return None
        
        if max(p.val,q.val) < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        elif min(p.val,q.val) > root.val:
            return self.lowestCommonAncestor(root.right,p,q)
        
        else:
            return root
        

# Recursive solution
# Return None if root is None or p is None or q is None. 
# If both p and q are less than root, search in the left subtree. 
# If both p and q are greater than root, search in the right subtree. 
# Otherwise, return root as it is the lowest common ancestor.
# Time Complexity: O(h), where h is the height of the tree.
#  In the worst case, h can be equal to n, where n is the number of nodes in the tree. 
# Space Complexity: O(h), where h is the height of the tree.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root

        while cur:
            if max(p.val,q.val) < cur.val:
                cur = cur.left
            elif min(p.val,q.val) > cur.val:
                cur = cur.right
            else:
                return cur
            
# Iterative solution
# Start from the root and traverse the tree.
# If both p and q are less than the current node, go to the left subtree.
# If both p and q are greater than the current node, go to the right subtree.
# Otherwise, the current node is the lowest common ancestor.
# Time Complexity: O(h), where h is the height of the tree.
# In the worst case, h can be equal to n, where n is the number of nodes in the tree.
# Space Complexity: O(1), as we are using constant space.