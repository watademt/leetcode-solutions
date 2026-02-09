# https://leetcode.com/problems/first-bad-version/
# Сложность: Easy
# Тема: Binary Search (Поиск границы)

# Имитация внешнего API LeetCode для локального запуска
def isBadVersion(version):
    first_bad = 4  # Допустим, 4-я версия плохая
    return version >= first_bad


class Solution(object):
    def firstBadVersion(self, n):
        left = 1
        right = n

        while left < right:
            # Используем mid для поиска границы
            mid = (left + right) // 2

            if isBadVersion(mid):
                # Если версия плохая, ответ может быть mid или левее
                right = mid
            else:
                # Если версия хорошая, ответ точно правее
                left = mid + 1

        return left


# --- Примеры для локальной проверки ---
if __name__ == "__main__":
    sol = Solution()
    print(f"Первая плохая версия из 5: {sol.firstBadVersion(5)}")  # Ожидаемый вывод: 4