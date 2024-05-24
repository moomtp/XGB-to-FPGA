import struct
import numpy as np

import unittest

from xgb_tree import *
from digit_helper_function import *



class TestTree(unittest.TestCase):

    testcase1 =  [[2**31 -1 , 0 , 0],
                    [2 , -1 , -1],
                    [1 , -1 , -1],
                    [65503.0, 65408.0, 2.5],
                    [255, 0, 0],
                    0,
                    False]

    testcase2 =  [[2**31 -1 , 0 , 0, 1, 1],
                    [2 , 4 , -1, -1, -1], # rc
                    [1 , 3 , -1, -1, -1],   # lc
                    [-4.5, 5.0, 0.5, -0.5, 256.25],  # node val
                    [255, 127, 0, 0, 0],  # feautre idx 0 for dont care
                    2048,
                    False]



    def setUp(self) :
        self.XGB_tree_1 = Tree(*self.testcase1)
        self.XGB_tree_2 = Tree(*self.testcase2)

        # return super().setUp()
        pass


    def test_total_num(self):
        self.assertEqual(self.XGB_tree_1.list_of_subtree_size , [3,1,1])
        self.assertEqual(self.XGB_tree_2.list_of_subtree_size , [5,3,1,1,1])


    def test_lc_num(self):
        self.assertEqual(self.XGB_tree_1._get_lc_tree_size(0) , 1)
        self.assertEqual(self.XGB_tree_2._get_lc_tree_size(0) , 3)

    
    def test_tree_node_gen_function(self):
        print("")
        # print(self.XGB_tree_1.nodes[0].gen())
        FPGA_tree_node = self.XGB_tree_2.nodes[0].gen()

        feature_idx = FPGA_tree_node[0:8]
        cmp_val = FPGA_tree_node[8:24]
        addr_to_next_child = FPGA_tree_node[25:31]
        is_leaf_node = FPGA_tree_node[31]

        self.assertEqual(b_to_i(feature_idx) , 255)
        self.assertEqual(b_to_i(is_leaf_node) , 0)
        self.assertEqual(b_to_i(addr_to_next_child) , 3)
        self.assertEqual(b_to_f(cmp_val) , -4.5)
        # print(self.XGB_tree_2.gen())

    def test_leaf_node_gen_function(self):
        print("")
        # print(self.XGB_tree_1.nodes[0].gen())
        FPGA_tree_node = self.XGB_tree_2.nodes[3].gen()
        
        score_val = FPGA_tree_node[0:16]
        addr_to_next_tree = FPGA_tree_node[16:30]
        is_last_tree = FPGA_tree_node[30]
        is_leaf_node = FPGA_tree_node[31]

        self.assertEqual(b_to_f(score_val) , 256.25)
        self.assertEqual(b_to_i(addr_to_next_tree) , 2048 + 5)
        self.assertEqual(b_to_i(is_last_tree) , 0)
        self.assertEqual(b_to_i(is_leaf_node) , 1)

        pass

    def test_b_to_h(self):
        b_str = i_to_b(25, 8)
        self.assertEqual(b_to_h(b_str), '00000019')

    def test_tree_gen_func(self):
        # print(self.XGB_tree_1.gen())
        pass

    def test_threadTree(self):
        thread_tree = ThreadTree(15)
        # print(thread_tree.gen())
        pass

    def test_ClassEndTree(self):
        thread_tree = ClassEndTree(15)
        # print(thread_tree.gen())

    def test_ClassesEndTree(self):
        thread_tree = ClassesEndTree(15)
        # print(thread_tree.gen())

if __name__ == '__main__':
    unittest.main()