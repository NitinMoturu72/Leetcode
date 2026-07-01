# 98. Validate Binary Search Tree

# Medium

# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left subtree of a node contains only nodes with keys strictly less than the node's key.
# The right subtree of a node contains only nodes with keys strictly greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
 

# Example 1:


# Input: root = [2,1,3]
# Output: true
# Example 2:


# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -231 <= Node.val <= 231 - 1


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(node,left,right):
            if not node:
                return True
            if not (node.val > left and node.val < right):
                return False

            return (isValid(node.left, left, node.val) and isValid(node.right, node.val, right)) 
        
        return isValid(root, float("-inf"), float("inf"))
    

# Recursive DFS
# We can use a recursive depth-first search (DFS) approach to validate the binary search tree (BST). 
# The idea is to traverse the tree while keeping track of the valid range for each node's value.
# Time complexity: O(n), where n is the number of nodes in the tree. We visit each node once.
# Space complexity: O(h), where h is the height of the tree.
# In the worst case, the height can be equal to the number of nodes in the tree (O(n)), but in a balanced tree, it would be O(log n).



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = [[root, float("-inf"), float("inf")]]
        while stack:
            pair = stack.pop()
            node = pair[0]
            left = pair[1]
            right = pair[2]

            if not node:
                continue
            
            if not (node.val > left and node.val < right):
                return False
            stack.append([node.left,left, node.val])
            stack.append([node.right, node.val, right])

        return True   
    
# Iterative DFS
# We can also use an iterative depth-first search (DFS) approach to validate the binary search tree (BST).
# We use a stack to keep track of the nodes and their valid ranges. For each node, we check if its value is within the valid range. 
# If it is not, we return False. If it is, we add its children to the stack with their corresponding valid ranges.
# Time complexity: O(n), where n is the number of nodes in the tree. We visit each node once.
# Space complexity: O(h), where h is the height of the tree. 
# In the worst case, the height can be equal to the number of nodes in the tree (O(n)), but in a balanced tree, it would be O(log n).