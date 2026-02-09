# https://leetcode.com/problems/middle-of-the-linked-list/
# Сложность: Easy
# Тема: Linked List (Two Pointers)

# Определение узла связанного списка
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def middleNode(self, head):
        """
        Находит середину связанного списка.
        Если в списке четное количество элементов, возвращает второй средний узел.
        """
        slow = head
        fast = head

        # Пока "заяц" (fast) не добежал до конца
        while fast and fast.next:
            slow = slow.next  # "Черепаха" делает 1 шаг
            fast = fast.next.next  # "Заяц" делает 2 шага

        # Когда заяц в конце, черепаха ровно на середине
        return slow


# --- Вспомогательные функции для проверки ---
def create_list(arr):
    if not arr: return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head


def print_list(head):
    res = []
    while head:
        res.append(str(head.val))
        head = head.next
    print(" -> ".join(res) + " -> None")


if __name__ == "__main__":
    sol = Solution()

    # Тест 1: Нечетное количество [1,2,3,4,5] -> Middle: 3
    test1 = create_list([1, 2, 3, 4, 5])
    mid1 = sol.middleNode(test1)
    print("Середина списка [1,2,3,4,5]:", mid1.val)

    # Тест 2: Четное количество [1,2,3,4,5,6] -> Middle: 4
    test2 = create_list([1, 2, 3, 4, 5, 6])
    mid2 = sol.middleNode(test2)
    print("Середина списка [1,2,3,4,5,6]:", mid2.val)