# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 15:16:49 2022

@author: Matthew
"""

import torch
import pandas as pd

train = pd.read_csv("train.csv")
pd.set_option("display.precision", 2)



print (train.shape)
