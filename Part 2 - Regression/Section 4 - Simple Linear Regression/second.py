#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 09:49:58 2018

@author: rubyliu
"""
import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd


dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 3].values