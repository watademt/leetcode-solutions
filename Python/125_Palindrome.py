# https://leetcode.com/problems/valid-palindrome/
# Сложность: Easy
# Тема: Two Pointers (In-place)

class Solution(object):
    def isPalindrome(self, s):
        left = 0
        right = len(s) - 1

        while left < right:
            # Пропускаем небуквенно-цифровые символы слева
            while left < right and not s[left].isalnum():
                left += 1

            # Пропускаем небуквенно-цифровые символы справа
            while left < right and not s[right].isalnum():
                right -= 1

            # Сравниваем символы в нижнем регистре
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True


# --- Примеры для локальной проверки ---
if __name__ == "__main__":
    sol = Solution()
    print(f"Тест 1 ('A man...'): {sol.isPalindrome('A man, a plan, a canal: Panama')}")  # True
    print(f"Тест 2 ('race a car'): {sol.isPalindrome('race a car')}")  # False
    print(f"Тест 3 (пустая строка): {sol.isPalindrome(' ')}")  # True