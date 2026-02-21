# https://leetcode.com/problems/first-unique-character-in-a-string/
# Сложность: Easy
# Тема: Hash Table / String / Counting

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        letter_counts = {}

        # Первый проход: собираем частоту каждого символа
        for char in s:
            letter_counts[char] = letter_counts.get(char, 0) + 1

        # Второй проход: находим первый уникальный
        for i, char in enumerate(s):
            if letter_counts[char] == 1:
                return i

        return -1