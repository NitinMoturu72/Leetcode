# 141. Linked List Cycle

# Easy


# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.

 

# Example 1:


# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
# Example 2:


# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
# Example 3:


# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.
 

# Constraints:

# The number of the nodes in the list is in the range [0, 104].
# -105 <= Node.val <= 105
# pos is -1 or a valid index in the linked-list.
 

# Follow up: Can you solve it using O(1) (i.e. constant) memory?


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        seen = set()
        while curr:
            if curr in seen:
                return True
            else:
                seen.add(curr)

            curr = curr.next
        
        return False
    

# Hash Set Solution:
# We use a hash set to keep track of the nodes we have seen as we traverse the linked list.
# For each node, we check if it is already in the set. If it is, then we have found a cycle and we return True.
# If it is not in the set, we add it to the set and continue traversing the list.
# If we reach the end of the list (curr becomes None) without finding a cycle, we return False.
# Time complexity is O(n) where n is the number of nodes in the list.
# Space complexity is O(n) in the worst case if there is no cycle, as we may end up storing all nodes in the set.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        
        return False
    

# Floyd's Tortoise and Hare Algorithm:
# We use two pointers, slow and fast. Slow moves one step at a time, while fast moves two steps at a time.
# If there is a cycle, the fast pointer will eventually meet the slow pointer. If there is no cycle, the fast pointer will reach the end of the list (None) before the slow pointer.
# Time complexity is O(n) where n is the number of nodes in the list.
# Space complexity is O(1) since we are using only a constant amount of extra space.