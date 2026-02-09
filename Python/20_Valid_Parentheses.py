# https://leetcode.com/problems/valid-parentheses/
# Сложность: Easy
# Тема: Stack / Hash Table (Dictionary)

class Solution(object):
    def isValid(self, s):
        """
        Проверка валидности строки со скобками (), [], {}.
        Используется Стек (LIFO) для отслеживания последних открытых скобок.
        """
        stack = []
        # Словарь пар: Ключ - закрывающая, Значение - открывающая скобка
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            # Если скобка открывающая — кладем в стек
            if char in mapping.values():
                stack.append(char)
            # Если скобка закрывающая
            elif char in mapping.keys():
                # Проверка: если стек пуст или верхний элемент не пара — ошибка
                if not stack or stack[-1] != mapping[char]:
                    return False
                # Если пара совпала — удаляем открывающую скобку из стека
                stack.pop()

        # В конце стек должен быть пустым
        return not stack


# --- Тесты для локальной проверки ---
if __name__ == "__main__":
    sol = Solution()
    print(f"Test '()[]{{}}': {sol.isValid('()[]{}')}")  # True
    print(f"Test '(]': {sol.isValid('(]')}")  # False
    print(f"Test '{{[]}}': {sol.isValid('{[]}')}")  # True