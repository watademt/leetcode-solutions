# https://leetcode.com/problems/palindrome-linked-list/
# Сложность: Easy (Time: O(n), Space: O(1))
# Тема: Linked List / Two Pointers / Reverse

class Solution(object):
    def isPalindrome(self, head):
        """
        Проверяет, является ли список палиндромом, используя O(1) дополнительной памяти.
        """
        # 1. Поиск середины (Заяц и Черепаха)
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Разворот второй половины списка
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        # 3. Сравнение первой и второй (развернутой) половин
        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next

        return True