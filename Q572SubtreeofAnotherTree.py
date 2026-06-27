# 572. Subtree of Another Tree

# Easy

# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

 

# Example 1:


# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true
# Example 2:


# Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
# Output: false
 

# Constraints:

# The number of nodes in the root tree is in the range [1, 2000].
# The number of nodes in the subRoot tree is in the range [1, 1000].
# -104 <= root.val <= 104
# -104 <= subRoot.val <= 104


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        
        stack = [root]
        check = False
        while stack:
            node = stack.pop()
            check = check or self.sameTree(node, subRoot)

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return check
    
    def sameTree(self, p, q):
        if not p and not q:
            return True
        
        if not p or not q or p.val!=q.val:
            return False
        
        return self.sameTree(p.left,q.left) and self.sameTree(p.right,q.right)

# Iterative DFS solution 
# The stack holds nodes still to visit. 
# Each iteration pops a node, checks whether the subtree rooted at that node matches subRoot (via sameTree), and folds the result into check with or — so once anything matches, check stays True. 
# Then it pushes the node's non-null children to keep the traversal going. When the stack empties, every node has been checked, and check holds the final answer.
# Time complexity: O(n*m) where n is the number of nodes in root and m is the number of nodes in subRoot. 
# In the worst case, we may have to check every node in root against every node in subRoot.
# Space complexity: O(n) for the stack, which in the worst case can hold all nodes of root.