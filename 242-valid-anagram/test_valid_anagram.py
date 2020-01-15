import unittest
from valid_anagram import Solution1, Solution2, Solution3


class TestLC(unittest.TestCase):

    def test_case_1(self):
        s = "anagram"
        t = "nagaram"
        sol = Solution1()
        self.assertEqual(True, sol.isAnagram(s, t))

    def test_case_2(self):
        s = "rat"
        t = "car"
        sol = Solution1()
        self.assertEqual(False, sol.isAnagram(s, t))

class TestSolution2(unittest.TestCase):
    def test_case_1(self):
        s = "anagram"
        t = "nagaram"
        sol = Solution3()
        self.assertEqual(True, sol.isAnagram(s, t))

    def test_case_2(self):
        s = "rat"
        t = "car"
        sol = Solution3()
        self.assertEqual(False, sol.isAnagram(s, t))

class TestSolution3(unittest.TestCase):
    def test_case_1(self):
        s = "anagram"
        t = "nagaram"
        sol = Solution2()
        self.assertEqual(True, sol.isAnagram(s, t))

    def test_case_2(self):
        s = "rat"
        t = "car"
        sol = Solution2()
        self.assertEqual(False, sol.isAnagram(s, t))

if __name__ == '__main__':
    unittest.main()
