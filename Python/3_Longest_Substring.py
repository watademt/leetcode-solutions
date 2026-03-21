# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Сложность: Medium
# Тема: Sliding Window / Hash Table / String

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = 0
        char_set = set()
        max_len = 0

        # Цикл for отлично подходит для правого указателя, так как он всегда идет +1
        for right in range(len(s)):
            # Если символ уже есть в окне, сужаем окно слева, пока дубликат не исчезнет
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            # Теперь в окне точно нет дубликатов.
            # Добавляем текущий символ и проверяем, не побили ли мы рекорд
            char_set.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len