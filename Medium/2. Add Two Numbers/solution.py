# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = []
        num2 = []
        result = 0
        
        while l1 != None:
            num1.append(l1.val)
            l1 = l1.next
        
        while l2 != None:
            num2.append(l2.val)
            l2 = l2.next
        
        if len(num1) > len(num2): length = len(num1)
        else: length = len(num2)
            
        temp_result = 0
        for i in range(length):
            if i >= len(num1):
                temp_result += (0 + num2[i]) * (10 ** i)
                continue
            elif i >= len(num2):
                temp_result += (num1[i] + 0) * (10 ** i)
                continue
            else:
                temp_result += (num1[i] + num2[i]) * (10 ** i)
            
        result = str(temp_result)[::-1]
        
        linked = ListNode(0)
        r = linked
        print(linked.val)
        for c in range(len(result)):
            if c == 0:
                linked.val = int(result[c])
                continue
                
            linked.next = ListNode(int(result[c]))
            linked = linked.next
            
        return r