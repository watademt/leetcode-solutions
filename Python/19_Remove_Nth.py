# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Сложность: Medium (Time: O(L), Space: O(1))
# Тема: Linked List / Two Pointers

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        Удаляет n-й узел с конца списка за один проход по памяти.
        """
        dummy = ListNode(0, head)
        slow = dummy
        fast = head

        # 1. Создаем дистанцию (зазор) в n шагов между slow и fast
        for _ in range(n):
            fast = fast.next

        # 2. Двигаем обоих до конца списка
        while fast:
            slow = slow.next
            fast = fast.next

        # 3. Перепрыгиваем через целевой узел
        slow.next = slow.next.next

        return dummy.next