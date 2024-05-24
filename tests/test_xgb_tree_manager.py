import struct
import numpy as np

from xgb_tree import Tree
from xgb_tree_manager import XGB_tree_manager
import unittest

import xgboost as xgb





class TestTreeManager(unittest.TestCase):

    filepath1 = "./skin_vgg16_layer44_FPGA.json"

    def setUp(self) -> None:
        self.tm1 = XGB_tree_manager(self.filepath1)
        


        pass
        # return super().setUp()

    def test_load_tree_from_json(self):
        pass


    def test_tree_manager(self):
        # self.tm1 = XGB_tree_manager("./skin_vgg16_layer44_FPGA.json")
        # print(self.tm1.gen())
        pass

    def test_tm_gen_function(self):
        print(self.tm1.gen())
        pass

    def test_tm_cal_nodes_func(self):
        test_tree_data = [{"tree_prarm" : {"num_nodes" : 15}},{"tree_prarm" : {"num_nodes" : 15}},{"tree_prarm" : {"num_nodes" : 10}},{"tree_prarm" : {"num_nodes" : 10}}]
        # class_total_node_list = XGB_tree_manager._cal_threads_node_num(test_tree_data, 2)
        # print(class_total_node_list)
