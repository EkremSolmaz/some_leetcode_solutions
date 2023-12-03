# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def fromArray(arr):
        if(len(arr) == 0):
            return None
        
        root = ListNode()
        root.val = arr[0]
        root.next = ListNode.fromArray(arr[1:])
        return root

    def print(self):
        res = [str(self.val)]
        root = self
        while root.next is not None:
            res.append(str(root.next.val))
            root = root.next
            
        
        print(" -> ".join(res))

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        cur = head
        second = ListNode()
        sec_cur = second
        while cur.next is not None:
            sec_cur.next = cur.next
            cur.next = cur.next.next

            sec_cur = sec_cur.next
            cur = cur.next if cur.next is not None else cur

        sec_cur.next = None
        cur.next = second.next

        return head


ln = ListNode.fromArray([1,2,3,4,5,6])
ln.print()
new_ln = Solution().oddEvenList(ln)
new_ln.print()