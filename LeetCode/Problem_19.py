# 19. Remove Nth Node From End of List
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
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
 

# Follow up: Could you do this in one pass?


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        temp=head
        count=0
        while(True):
            if temp==None:
                break
            else:
                count+=1
                if temp.next==None:
                    break
                else:
                    temp=temp.next
        
        if count==1:    
            return None
        
        if count==n:
            return head.next
        
        temp=head
        for i in range(count-n-1):
            temp=temp.next
        temp.next=temp.next.next

        return head