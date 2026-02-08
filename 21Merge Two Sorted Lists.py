# https://leetcode.com/problems/merge-two-sorted-lists/
# Сложность: Easy (Time: O(n + m), Space: O(1))
# Тема: Linked List / Recursion (Iterative)

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        Объединяет два отсортированных списка в один новый отсортированный список.
        """
        # Создаем технический узел-пустышку
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next  # Продвигаем рабочий указатель

        # Прицепливаем оставшийся хвост одного из списков
        tail.next = list1 or list2

        return dummy.next