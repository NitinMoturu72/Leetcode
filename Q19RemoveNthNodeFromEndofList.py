# 19. Remove Nth Node From End of List
# Medium

# Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

# Example 1:


# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:

# Input: head = [1], n = 1
# Output: []
# Example 3:

# Input: head = [1,2], n = 1
# Output: [1]
 

# Constraints:

# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []

        curr = head

        while curr:
            nodes.append(curr)
            curr = curr.next
        
        size = len(nodes)
        indx = size - n 

        if indx == 0:
            return head.next
        
        nodes[indx-1].next = nodes[indx].next

        return head

#Brute Force Solution
# We convert the linked list to an array, remove the nth element, and reconstruct the linked list.
# The time complexity of this approach is O(n) due to the traversal of the linked list and reconstruction, 
# and the space complexity is also O(n) due to the additional list used to store the nodes.