import pickle
from tdr import TDR

# Prompt the user to enter the file path of the pickled TDR object
file_path = input("Enter the file path of the saved TDR object: ")

# Load the TDR object from the file
with open(file_path, 'rb') as file:
    tdr_object = pickle.load(file)

# Assume `tdr_object` is an instance of `TDR`
start_time = 0.1
end_time = 0.5
filtered_data = tdr_object.filter_dataframe_by_time_range(start_time, end_time)

print("Filtered Data:")
print(filtered_data)


# Prompt the user to enter a partial string for searching
partial_string = input("Enter a partial string to search for: ")

# Search for the partial string within the random_strings attribute
matching_elements = tdr_object.search(partial_string)

# Display the matching elements
print("Matching Elements:")
print(matching_elements)

# Filter the DataFrame based on a specific time and variable name
some_time = input("Enter the time you are looking for")
# some_time = 0.3  # replace with your desired time
some_name = partial_string
#filtered_data = tdr_object.filter_dataframe(some_time, some_name)
filtered_data = tdr_object.filter_dataframe_by_time_range(some_time,some_name)

print("Filtered Data:")
print(filtered_data)

