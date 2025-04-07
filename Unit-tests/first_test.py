#!/usr/bin/env python3

from Code.getbest import *
import unittest

class test_getbest(unittest.TestCase):
    def test_getcols(self):
        f = open("Code/bestdat0.csv", "r")
        num_col, mark_col = getCols(f)        
        self.assertEqual(num_col, 1)
        self.assertEqual(mark_col, 2)
        print(str(num_col))
        print(str(mark_col))
        f.close()

    def test_findTop(self):
        f = open("Code/bestdat0.csv", "r")
        num_col, mark_col = getCols(f)
        f.seek(0)
        best_idx, best = findTop(f,num_col,mark_col)
        self.assertEqual(best, 90)
        self.assertEqual(best_idx, str(167381))
        f.close()

if __name__ == '__main__':
     unittest.main()