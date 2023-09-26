import pandas as pd

def read_csv_to_dataframe(filepath):
    file_path = filepath    
    return pd.read_csv(file_path)

def write_to_csv(dataframe,file_name):
    dataframe.to_csv(file_name, index=False)




