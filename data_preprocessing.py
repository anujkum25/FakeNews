import os
import pandas as pd
from utility_functions import read_stored_exceL_and_combine
from source_selection import path, primary_tags

path1=os.path.join(path, str(primary_tags[0]))

input_df = read_stored_exceL_and_combine(path1)
print(input_df.shape)

def NER_features():
    return()




def symantic_features():
    return()

def sentatic_features():
    return()