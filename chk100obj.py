import pickle
import pandas as pd
from tdr import TDR

# Load the TDR object from the file
with open('test', 'rb') as file:
    tdr_object = pickle.load(file)
pd.set_option('display.max_rows', 10000)

# Print the properties of the tdr_object
print("tdata: ", tdr_object.tdata)
print("tpdata: ", tdr_object.tpdata)
print("random_strings: ", tdr_object.random_strings)
print("variable_Names: ", tdr_object.variable_Names)
print("variable_Descriptions: ", tdr_object.variable_Descriptions)

# Print the top 100 rows of the DataFrame
print("Top 100 rows of DataFrame: ")
print(tdr_object.df.head(10000))

