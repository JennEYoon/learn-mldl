"""
Scratch File - SVM, cs231n Assignment 1
filename: scratch.py
dir: C:\python\w_231\assignment1\

"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

####  Test reading CIFAR uncompressed file into memory.
# File already unzipped using MinGW tar command into 6 batches.
# File is binary format, pickle used to save in binary format.
####
import pickle

def unpickle(file):
    fo = open(file, 'rb')
    dict = pickle.load(fo, encoding='latin1')
    fo.close()
    return dict

file = "cs231n\datasets\cifar-10-batches-py\data_batch_1"

data = unpickle(file)    


""" Example code with pickle binary decoding into string, 
    latin-1 codec.

with open(mshelffile, 'rb') as f:
    d = pickle.load(f, encoding='latin1') 
"""
