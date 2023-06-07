import random
import string
import numpy as np
import pandas as pd
import pickle

# Prompt the user to enter a file path to save the object
file_path = input("Enter a file path to save the TDR object: ")

class TDR:
    def __init__(self, tdata, tpdata, random_strings, variable_Names, variable_Descriptions):
        self.tdata = tdata
        self.tpdata = tpdata
        self.random_strings = random_strings
        self.variable_Names = variable_Names
        self.variable_Descriptions = variable_Descriptions
        # Create the DataFrame
        self.df = self.create_dataframe()

    def create_dataframe(self):
        time_data = np.repeat(self.tdata['Time'].values, len(self.random_strings))
        variable_name_data = np.tile(self.random_strings, len(self.tdata))
        numerical_data = np.array(self.tpdata).flatten()
        df = pd.DataFrame({
            'Time': time_data,
            'VariableName': variable_name_data,
            'NumericalData': numerical_data
        })
        return df

    def search(self, partial_string):
        matching_elements = []
        for element in self.random_strings:
            if partial_string.lower() in element.lower():
                matching_elements.append(element)
        return matching_elements

    def filter_dataframe(self, some_time, some_name):
        return self.df[(self.df['Time'] == some_time) & (self.df['VariableName'] == some_name)]

    def save_to_file(self, file_path):
        with open(file_path, 'wb') as file:
            pickle.dump(self, file)

# Generate random strings and other data
def generate_random_string(length):
    characters = string.ascii_letters + string.digits + "!@#$%^&*()"
    return ''.join(random.choice(characters) for _ in range(length))

def generate_random_strings(numVars):
    result = []
    for _ in range(numVars):
        random_string_1 = "FTIICP.MOSS_ES_AS_EmitterTrackReport" + generate_random_string(10)
        random_string_2 = generate_random_string(100)
        result.append(random_string_1 + "Some.ActivityParameter" + random_string_2)
    return result

# Generate random strings
numVars = 1470
random_strings = generate_random_strings(numVars)

# Generate tdata and tpdata using numpy and pandas
num_rows = 100
num_cols = numVars
mean_time = 0.3
std_dev = 0.15
time_data = np.cumsum(np.random.normal(mean_time, std_dev, (num_rows, 1)))
tdata = pd.DataFrame(time_data, columns=['Time'])
tpdata = pd.DataFrame(np.random.normal(mean_time, std_dev, (num_rows, num_cols)))

# Create an instance of TDR and assign it to a global variable
tdr_object = TDR(tdata, tpdata, random_strings, None, None)

# Save the object to the specified file path
tdr_object.save_to_file(file_path)
