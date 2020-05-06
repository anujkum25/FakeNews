import os
import pandas as pd
from utility_functions import read_stored_excel_and_combine, read_test_data
from source_selection import path, primary_tags, test_data_path
from sklearn.model_selection import train_test_split

def training_and_test_data():
    '''
    create train and test data from generated excels and testdata
    '''
    path1=path/str(primary_tags[0])
    path2=os.chdir(path1)

    input_df = read_stored_excel_and_combine(path2)
    input_df['label'] = [1]*len(input_df)

    path3=test_data_path
    path4= os.chdir(path3)

    test_df= read_test_data(path4)
    test_df['label'] = [0]*len(test_df)

    full_df= pd.concat([input_df, test_df], axis=0)
    full_df1=full_df.drop('url', axis=1)

    train, test= train_test_split(full_df1,  test_size=0.2)
    return (train, test)

