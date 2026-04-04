# https://leetcode.com/problems/group-anagrams/
# Сложность: Medium
# Тема: Hash Table / Sorting

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        grouped = {}

        for word in strs:
            # Сортируем буквы слова, чтобы создать универсальный ключ
            word_sort = ''.join(sorted(word))

            if word_sort not in grouped:
                grouped[word_sort] = []

            # Добавляем оригинальное слово в список анаграмм
            grouped[word_sort].append(word)

        return grouped.values()