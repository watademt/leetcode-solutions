# https://leetcode.com/problems/daily-temperatures/
# Сложность: Medium
# Тема: Array / Stack / Monotonic Stack

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        # Инициализируем стек для хранения индексов дней
        stack = []
        # Результирующий массив, заполненный нулями по умолчанию
        answer = [0] * len(temperatures)

        # Проходим по всем дням и их температурам
        for i, t in enumerate(temperatures):
            # Если текущая температура больше температуры на вершине стека
            while stack and t > temperatures[stack[-1]]:
                # Извлекаем предыдущий день из стека
                prev_day = stack.pop()
                # Вычисляем разницу в днях и записываем в ответ
                answer[prev_day] = i - prev_day

            # Добавляем текущий день в стек для поиска более теплого дня в будущем
            stack.append(i)

        return answer