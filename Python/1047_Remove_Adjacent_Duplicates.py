# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
# Сложность: Easy
# Тема: Stack / String

class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for char in s:
            # Если стек не пустой и верхний элемент совпадает с текущим -> удаляем (схлопываем)
            if stack and stack[-1] == char:
                stack.pop()
            # Иначе -> добавляем в стек
            else:
                stack.append(char)

        # Собираем оставшиеся буквы обратно в строку
        return "".join(stack)