import numpy as np
import pandas as pd


def get_data(filename):
    raw_data_set = pd.read_csv(filename)
    print(raw_data_set.shape)
