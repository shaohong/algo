import unittest
from binaryTreeDepth import TreeNode, Solution

class TestBinaryTreeDepth(unittest.TestCase):
    def test_case_1(self):
        '''
        Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
        '''
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)

        sol = Solution()
        self.assertEqual(3, sol.maxDepth(root))
        pass

if __name__ == '__main__':
    unittest.main()