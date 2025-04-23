from typing import List
import unittest


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        if n == 0:
            return True
        for i in range(len(flowerbed)):
            left = (i == 0 ) or (flowerbed[i - 1] ==0) 
            right = (i == len(flowerbed) - 1) or ( flowerbed[i+1] == 0)
            if left and right and flowerbed[i] == 0:
                flowerbed[i] = 1
                n-=1
                if n==0:
                    return True
        return False


class TestCanPlaceFlowers(unittest.TestCase):
    def test_example_true(self):
        sol = Solution()
        self.assertTrue(sol.canPlaceFlowers([1, 0, 0, 0, 1], 1))

    def test_example_false(self):
        sol = Solution()
        self.assertFalse(sol.canPlaceFlowers([1, 0, 0, 0, 1], 2))

    def test_all_empty(self):
        sol = Solution()
        self.assertTrue(sol.canPlaceFlowers([0, 0, 0, 0, 0], 2))

    def test_full_flowerbed(self):
        sol = Solution()
        self.assertFalse(sol.canPlaceFlowers([1, 1, 1, 1, 1], 1))

    def test_edge_case(self):
        sol = Solution()
        self.assertTrue(sol.canPlaceFlowers([0], 1))

    def test_no_new_flowers(self):
        sol = Solution()
        self.assertTrue(sol.canPlaceFlowers([1, 0, 1, 0, 1], 0))


if __name__ == '__main__':
    unittest.main()
       
        

   