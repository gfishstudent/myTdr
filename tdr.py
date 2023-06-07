import random
import string
import numpy as np
import pandas as pd
import pickle

# def generate_random_string(length):
#     characters = string.ascii_letters + string.digits + "!@#$%^&*()"
#     return ''.join(random.choice(characters) for _ in range(length))

# def generate_random_strings(num_strings, length=300):
#     return [generate_random_string(length) for _ in range(num_strings)]

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



class TDR:
    def __init__(self, tdata, tpdata, random_strings, variable_Names, variable_Descriptions):
        self.tdata = tdata
        self.tpdata = tpdata
        self.random_strings = random_strings
        self.variable_Names = variable_Names
        self.variable_Descriptions = variable_Descriptions
        self.df = self.create_dataframe()

    # def create_dataframe(self):
    #     time_data = np.repeat(self.tdata, len(self.random_strings))
    #     variable_name_data = np.tile(self.random_strings, len(self.tdata))
    #     numerical_data = self.tpdata.flatten()

    #     df = pd.DataFrame({
    #         'Time': time_data,
    #         'VariableName': variable_name_data,
    #         'NumericalData': numerical_data
    #     })
    #     return df

    def create_dataframe(self):
        # Prepare data for DataFrame
        time_data = np.repeat(self.tdata.values.flatten(), len(self.random_strings))
        variable_name_data = np.tile(self.random_strings, len(self.tdata))
        numerical_data = self.tpdata.values.flatten()

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

    def filter_dataframe_by_time_range(self, start_time, end_time):
        return self.df[(self.df['Time'] >= start_time) & (self.df['Time'] <= end_time)]

    def filter_dataframe(self, some_time, some_name):
        return self.df[(self.df['Time'] == some_time) & (self.df['VariableName'] == some_name)]

    def save_to_file(self, file_path):
        with open(file_path, 'wb') as file:
            pickle.dump(self, file)
