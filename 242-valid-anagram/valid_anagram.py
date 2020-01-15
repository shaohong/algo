# https://leetcode.com/problems/valid-anagram

class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:
        s_sorted = sorted(s)
        t_sorted = sorted(t)
        return s_sorted == t_sorted

class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        from collections import Counter

        # buid the Coutner
        s_chars = Counter(s)
        t_chars = Counter(t)
        return s_chars == t_chars


class Solution3:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # build our own dictionary instead of using the 'collections.Counter'     
        s_chars, t_chars = {}, {}
        for c in s:
            s_chars[c] = s_chars.get(c, 0) + 1
        for c in t:
            t_chars[c] = t_chars.get(c, 0) + 1
        return s_chars == t_chars