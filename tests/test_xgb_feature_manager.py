import struct
import numpy as np

import unittest

from xgb_feature_manager import XGB_feature_manager
from digit_helper_function import *



class TestFeatureManager(unittest.TestCase):

    testcase1 =  ["f3", "f0" , "f2", "f1",  "f5", "f4"]

    testcase2 =  []

    feature_data = [[2.0, -2.0, 1.0, 255.0, 0.0, 0.0, 0.0],
                    [2.0, -2.0, 1.0, 255.0, 0.0, 0.0, 0.0]]



    def setUp(self) :
        self.XGB_fm_1 = XGB_feature_manager(self.testcase1)
        self.XGB_fm_2 = XGB_feature_manager(self.testcase2)

        # return super().setUp()
        pass

    def test_feautre_idx(self):
       self.assertEqual(self.XGB_fm_1.feature_idx, [3,0,2,1,5,4])

    def test_gen_feature_func(self):
        # print(self.XGB_fm_1.feature_idx)
        # print(self.XGB_fm_1._gen_feature_data(self.feature_data[0]))
        # self.assertEqual(self.XGB_tree_1.list_of_subtree_size , [3,0,6,1,5,4])
        # self.assertEqual(self.XGB_tree_2.list_of_subtree_size , [])
        pass

    def test_gen_func(self):
        # print(self.XGB_fm_1.gen(self.feature_data, 1))
        pass

    def test_read_from_json(self):
        XGB_fm = XGB_feature_manager(".\skin_vgg16_layer44_FPGA.json")
        print(XGB_fm.gen(self.feature_data, [0,1]))
        pass

    def test_q_format_setter(self):
        self.XGB_fm_1.set_q_format([10,5])
        print(self.XGB_fm_1.q_format)



    # def test_lc_num(self):
    #     self.assertEqual(self.XGB_tree_1._get_lc_tree_size(0) , 1)
    #     self.assertEqual(self.XGB_tree_2._get_lc_tree_size(0) , 3)

    
    # def test_tree_node_gen_function(self):
    #     print("")
    #     # print(self.XGB_tree_1.nodes[0].gen())
    #     FPGA_tree_node = self.XGB_tree_2.nodes[0].gen()

    #     feature_idx = FPGA_tree_node[0:8]
    #     cmp_val = FPGA_tree_node[8:24]
    #     addr_to_next_child = FPGA_tree_node[25:31]
    #     is_leaf_node = FPGA_tree_node[31]

    #     self.assertEqual(b_to_i(feature_idx) , 255)
    #     self.assertEqual(b_to_i(is_leaf_node) , 0)
    #     self.assertEqual(b_to_i(addr_to_next_child) , 3)
    #     self.assertEqual(b_to_f(cmp_val) , -4.5)
    #     # print(self.XGB_tree_2.gen())

    # def test_leaf_node_gen_function(self):
    #     print("")
    #     # print(self.XGB_tree_1.nodes[0].gen())
    #     FPGA_tree_node = self.XGB_tree_2.nodes[3].gen()
        
    #     score_val = FPGA_tree_node[0:16]
    #     addr_to_next_tree = FPGA_tree_node[16:30]
    #     is_last_tree = FPGA_tree_node[30]
    #     is_leaf_node = FPGA_tree_node[31]

    #     self.assertEqual(b_to_f(score_val) , 256.25)
    #     self.assertEqual(b_to_i(addr_to_next_tree) , 2048 + 5)
    #     self.assertEqual(b_to_i(is_last_tree) , 0)
    #     self.assertEqual(b_to_i(is_leaf_node) , 1)

    #     pass

    # def test_b_to_h(self):
    #     b_str = i_to_b(25, 8)
    #     self.assertEqual(b_to_h(b_str), '00000019')

    # def test_tree_gen_func(self):
    #     print(self.XGB_tree_1.gen())
    #     pass


if __name__ == '__main__':
    unittest.main()