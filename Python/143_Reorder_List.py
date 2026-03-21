# https://leetcode.com/problems/reorder-list/
# Сложность: Medium
# Тема: Linked List / Two Pointers / Stack

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        # Фаза 1: Ищем середину списка (Заяц и Черепаха)
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Фаза 2: Разворачиваем вторую половину списка
        curr = slow.next
        prev = None
        slow.next = None  # Важно: отрубаем конец первой половины, чтобы не было цикла!

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # Фаза 3: Слияние "змейкой" (zipper merge)
        first = head
        second = prev  # prev сейчас указывает на голову перевернутой второй половины

        while second:
            # Делаем "закладки" на следующие узлы
            f = first.next
            s = second.next

            # Перекидываем стрелки друг на друга
            first.next = second
            second.next = f

            # Сдвигаем оба указателя вперед
            first = f
            second = s