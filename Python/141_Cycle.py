# https://leetcode.com/problems/linked-list-cycle/
# Сложность: Easy
# Тема: Linked List (Two Pointers / Floyd's Cycle-Finding)

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        Определяет наличие цикла в связанном списке.
        Использует два указателя: медленный (slow) и быстрый (fast).
        """
        slow = head
        fast = head

        # Пока быстрый указатель не встретит конец списка
        while fast and fast.next:
            slow = slow.next  # Черепаха идет на 1 шаг
            fast = fast.next.next  # Заяц бежит на 2 шага

            # Если указатели встретились в одном узле — цикл есть
            if slow == fast:
                return True

        # Если Заяц дошел до конца — цикла нет
        return False


# --- Пример для локальной проверки ---
if __name__ == "__main__":
    sol = Solution()

    # Создаем список 3 -> 2 -> 0 -> -4
    n1 = ListNode(3)
    n2 = ListNode(2)
    n3 = ListNode(0)
    n4 = ListNode(-4)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    # Зацикливаем: -4 указывает обратно на 2
    n4.next = n2

    print(f"Есть ли цикл в списке? {sol.hasCycle(n1)}")  # Ожидаемый вывод: True