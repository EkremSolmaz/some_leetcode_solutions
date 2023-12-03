# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if  head is None:
            return head
        
        cur = head
        counter = 0
        while counter < k:
            counter += 1
            if cur.next is not None:
                cur = cur.next
            else:
                k %= counter
                counter = 0
                cur = head

        keep = head
        while cur.next is not None:
            keep = keep.next
            cur = cur.next


        if keep.next is None:
            return head
        new_head = keep.next
        keep.next = None
        cur.next = head

        return new_head



s = Solution()
print("Expected: [4,5,1,2,3], Result:", s.rotateRight(head = [1,2,3,4,5], k = 2))