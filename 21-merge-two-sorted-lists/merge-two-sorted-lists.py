#Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = list1
        if(not list1):
            head = list2
        while(list1 and list2):
            if(list2.val < list1.val and list1 == head):
                temp = list1
                list1 = list2
                list2 = temp
                head = list1
            elif(list2.val >= list1.val and not list1.next):
                list1.next = list2
                break
            elif(list2.val >= list1.val and list2.val < list1.next.val):
                node = ListNode(list2.val, list1.next)
                list1.next = node
                list2 = list2.next
                list1 = list1.next
            else:
                list1 = list1.next
        return head