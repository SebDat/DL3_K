# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 17:33:58 2018

@author: SCatheline
"""

from model import Deeplabv3
deeplab_model = Deeplabv3(input_shape=(384,384,3), classes=2, OS=8)  
#use OS only for xception backbone


