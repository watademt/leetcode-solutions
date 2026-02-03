class Solution(object):
    def isAnagram(self, s, t):
        seen_s = {}
        seen_t = {}
        for i in s:
           seen_s[i] = seen_s.get(i, 0) + 1
        for i in t:
           seen_t[i] = seen_t.get(i, 0) + 1
        return seen_s == seen_t