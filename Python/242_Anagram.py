# https://leetcode.com/problems/valid-anagram/
# Сложность: Easy
# Тема: Hash Table / Dictionary

class Solution(object):
    def isAnagram(self, s, t):
        # Если длины разные, это точно не анаграммы
        if len(s) != len(t):
            return False

        seen_s = {}
        seen_t = {}

        # Считаем количество каждой буквы в первой строке
        for char in s:
            seen_s[char] = seen_s.get(char, 0) + 1

        # Считаем количество каждой буквы во второй строке
        for char in t:
            seen_t[char] = seen_t.get(char, 0) + 1

        # Сравниваем полученные карты частот
        return seen_s == seen_t


# --- Примеры для локальной проверки ---
if __name__ == "__main__":
    sol = Solution()
    print(f"Тест 1 (anagram/nagaram): {sol.isAnagram('anagram', 'nagaram')}")  # True
    print(f"Тест 2 (rat/car): {sol.isAnagram('rat', 'car')}")  # False