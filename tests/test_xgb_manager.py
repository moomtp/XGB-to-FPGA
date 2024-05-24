import struct
import numpy as np

import unittest

from xgb_manager import XGB_manager
from digit_helper_function import *



class TestXGBManager(unittest.TestCase):


    feature_data = [[2.0, -2.0, 1.0, 255.0, 0.0, 0.0, 0.0],
                    [2.0, -2.0, 1.0, 255.0, 0.0, 0.0, 0.0]]
    label_data = [0,1]
    
    

    def setUp(self) :
        # return super().setUp()
        self.xm1 = XGB_manager("skin_vgg16_layer44_FPGA.json")
        pass

    def test_xgb_manager(self):
        self.xm1.create_vhdl_code("ham_v16_lyr44.vhd", self.feature_data)
        self.xm1.create_vhdl_labeling_code("ham_v16_lyr44.vhd", self.feature_data, self.label_data)
        
        pass


if __name__ == '__main__':
    unittest.main()