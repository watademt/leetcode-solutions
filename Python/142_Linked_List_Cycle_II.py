# https://leetcode.com/problems/linked-list-cycle-ii/
# Сложность: Medium
# Тема: Linked List / Two Pointers / Fast & Slow Pointers

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        fast = head

        # Этап 1: Ищем точку встречи (внутри цикла)
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break

        # Проверяем, был ли вообще цикл
        if fast == None or fast.next == None:
            return None
        else:
            # Этап 2: Ищем старт цикла
            fast = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow