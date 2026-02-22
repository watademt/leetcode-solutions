# https://leetcode.com/problems/longest-common-prefix/
# Сложность: Easy
# Тема: String / Array

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""

        # Берем первое слово за эталонный префикс
        prefix = strs[0]

        for st in strs:
            if prefix == "":
                return ""
            # Пока текущее слово не начинается с нашего префикса,
            # отрезаем от префикса по одной букве с конца
            while not st.startswith(prefix):
                prefix = prefix[:-1]

        return prefix