# https://leetcode.com/problems/reverse-linked-list/
# Сложность: Easy
# Тема: Linked List (Pointers)

# Определение узла связанного списка
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            next_node = curr.next  # Запоминаем следующий узел
            curr.next = prev  # Разворачиваем стрелку
            prev = curr  # Двигаем prev вперед
            curr = next_node  # Двигаем curr вперед
        return prev


# --- Вспомогательные функции для тестов ---
def print_list(head):
    res = []
    while head:
        res.append(str(head.val))
        head = head.next
    print(" -> ".join(res) + " -> None")


if __name__ == "__main__":
    # Создаем список 1 -> 2 -> 3
    node3 = ListNode(3)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)

    sol = Solution()
    print("Исходный список:")
    print_list(node1)

    reversed_head = sol.reverseList(node1)
    print("Развернутый список:")
    print_list(reversed_head)