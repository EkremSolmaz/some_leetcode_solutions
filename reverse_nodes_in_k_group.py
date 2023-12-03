
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print(self):
        a = []
        head = self
        while head is not None:
            a.append(head.val)
            head = head.next
        print(" -> ".join([str(x) for x in a]))

    def fromArray(arr):
        head = ListNode()
        i = 0
        x = head
        while i < len(arr) - 1:
            x.val = arr[i]
            x.next = ListNode()
            x = x.next
            i+=1

        x.val = arr[-1]
        x.next = None

        return head
    

class Solution:
    def reverse(self, head):
        head.print()
        if head is None or head.next is None:
            return head
        cur = head

        n = cur.next
        nn = n.next
        cur.next = None
        while nn is not None:
            n.next = cur
            cur = n
            n = nn
            nn = n.next

        n.next = cur

        n.print()
        return n


    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k < 2:
            return head
        cur: Optional[ListNode] = head
        i = 0
        new_head = None

        last = None
        while cur is not None:
            group_head = cur
            for i in range(k-1):
                if cur is None:
                    break
                cur = cur.next
            
            if cur is None:
                break
            next_group_head = cur.next
            cur.next = None
            cur = self.reverse(group_head)

            if last is not None:
                last.next = cur

            if new_head is None:
                new_head = cur

            while cur.next is not None:
                cur = cur.next
            cur.next = next_group_head


            last = cur
            cur = cur.next
            print(last.val)

        
        return new_head


ln = ListNode.fromArray([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
ln.print()
s = Solution()
ln = s.reverseKGroup(ln, 3)
ln.print()

