# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, l: Optional[ListNode]) -> bool:
        if l is None:
          return True
        slow = fast = ListNode(0)
        slow.next = l
        
        while fast is not None:
          slow = slow.next
          fast = fast.next.next if fast.next else None
        
        slow = reverse(slow)
        
        while slow is not None:
          print(l.val, slow.val)
          if l.val != slow.val:
            return False
          l = l.next
          slow = slow.next
            
        return True
            


def reverse(node):
  if node is None or node.next is None:
    return node
    
  prev = None
  cur = node
  temp = node.next
  while temp is not None:
    cur.next = prev
    prev = cur
    cur = temp
    temp = temp.next
    
  cur.next = prev
    
  return cur
