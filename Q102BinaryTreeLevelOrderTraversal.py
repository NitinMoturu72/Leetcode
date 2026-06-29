# 102. Binary Tree Level Order Traversal

# Medium

# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
# Example 2:

# Input: root = [1]
# Output: [[1]]
# Example 3:

# Input: root = []
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 2000].
# -1000 <= Node.val <= 1000



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q = deque()
        q.append(root)
        res = []

        while q:
            qlen = len(q)
            level = []
            for i in range(qlen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        return res

# Breadth first search
# We use a deque to keep track of the nodes at each level. 
# For each level, we iterate through the nodes, adding their values to a list and appending their children to the deque for the next level. 
# We continue this process until there are no more nodes to process.
# time complexity: O(n), where n is the number of nodes in the tree. We visit each node once.
# space complexity: O(n), where n is the number of nodes in the tree. 
# In the worst case, we may have to store all nodes in the deque at once (for example, if the tree is a complete binary tree).



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        stack = [[root, 0]]
        res = []
        while stack:
            pair = stack.pop()
            node = pair[0]
            level = pair[1]
            if node:
                stack.append([node.right, level+1])
                stack.append([node.left, level+1])
                if level <= len(res)-1:
                    res[level].append(node.val)
                else:
                    res.append([node.val])
        
        return res

# Depth first search
# We use a stack to keep track of the nodes and their levels.
# For each node, we add its value to the corresponding level in the result list.
# We then add its children to the stack with their corresponding levels.
# If the level does not exist in the result list, we create a new list for that level.
# Else, we append the value to the existing list for that level.
# time complexity: O(n), where n is the number of nodes in the tree. We visit each node once.
# space complexity: O(n), where n is the number of nodes in the tree.


