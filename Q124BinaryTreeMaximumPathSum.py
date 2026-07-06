# 124. Binary Tree Maximum Path Sum

# Hard

# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

# The path sum of a path is the sum of the node's values in the path.

# Given the root of a binary tree, return the maximum path sum of any non-empty path.

 

# Example 1:


# Input: root = [1,2,3]
# Output: 6
# Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
# Example 2:


# Input: root = [-10,9,20,null,null,15,7]
# Output: 42
# Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
 

# Constraints:

# The number of nodes in the tree is in the range [1, 3 * 104].
# -1000 <= Node.val <= 1000


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = root.val

        def dfs(node):
            nonlocal max_sum
            if not node:
                return 0
            left = 0
            right = 0
            if node.left:
                left = max(dfs(node.left), left)
            if node.right:
                right = max(dfs(node.right), right)

            current_path = node.val + left + right

            max_sum = max(max_sum, current_path)

            return node.val + max(left, right)

        dfs(root)
        return max_sum

# Recursive Approach
# The recursive approach involves performing a depth-first search (DFS) on the binary tree. 
# For each node, we calculate the maximum path sum that can be obtained by including that node and its left and right subtrees. 
# We keep track of the overall maximum path sum encountered during the traversal.
# Time complexity: O(n), where n is the number of nodes in the tree, as we visit each node once.
# Space complexity: O(h), where h is the height of the tree, due to the recursion stack. 
# In the worst case, the height can be equal to the number of nodes in the tree (O(n)) for a skewed tree.